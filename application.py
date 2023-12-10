from bottle import Bottle, run, template, request, redirect
import sqlite3

app = Bottle()

conn = sqlite3.connect('mobile_company.db')
cursor = conn.cursor()

@app.route('/')
def index():
    search_term = request.query.get('search', '')
    query = '''
    SELECT mobiles.id, mobiles.title, mobiles.release_year, companies.name
    FROM mobiles
    JOIN companies ON mobiles.company_id = companies.id
    WHERE mobiles.title LIKE ? OR companies.name LIKE ?
    '''
    cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
    result = cursor.fetchall()
    return template('index', mobiles=result)

@app.route('/add')
def add_form():
    cursor.execute('SELECT * FROM companies')
    companies = cursor.fetchall()
    return template('insert', companies=companies)

@app.route('/add', method='POST')
def add():
    title = request.forms.get('title')
    release_year = request.forms.get('release_year')
    company_id = request.forms.get('company_id')
    cursor.execute("INSERT INTO mobiles (title, release_year, company_id) VALUES (?, ?, ?)",
                   (title, release_year, company_id))
    conn.commit()
    redirect('/')

@app.route('/edit/<mobile_id>')
def edit_form(mobile_id):
    cursor.execute("SELECT * FROM mobiles WHERE id=?", (mobile_id,))
    mobile = cursor.fetchone()
    cursor.execute('SELECT * FROM companies')
    companies = cursor.fetchall()
    return template('edit', mobile=mobile, companies=companies)

@app.route('/edit/<mobile_id>', method='POST')
def edit(mobile_id):
    title = request.forms.get('title')
    release_year = request.forms.get('release_year')
    company_id = request.forms.get('company_id')
    cursor.execute("UPDATE mobiles SET title=?, release_year=?, company_id=? WHERE id=?",
                   (title, release_year, company_id, mobile_id))
    conn.commit()
    redirect('/')

@app.route('/delete/<mobile_id>')
def delete(mobile_id):
    cursor.execute("DELETE FROM mobiles WHERE id=?", (mobile_id,))
    conn.commit()
    redirect('/')

if __name__ == '__main__':
    run(app, host='localhost', port=8090)
