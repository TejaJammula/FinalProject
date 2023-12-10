<!DOCTYPE html>
<html>
<head>
 <title>Edit Mobile</title>
</head>
<body>
 <h1>Edit Mobile</h1>
 <form action="/edit/{{ mobile[0] }}" method="post">
 <label>Title:</label>
 <input type="text" name="title" value="{{ mobile[1] }}" required><br>
 <label>Release Year:</label>
 <input type="number" name="release_year" value="{{ mobile[2] }}" required><br>
 <label>Company:</label>
 <select name="company_id">
 % for company in companies:
 % if company[0] == mobile[3]:
 <option value="{{ company[0] }}" selected>{{ company[1] }}</option>
 % else:
 <option value="{{ company[0] }}">{{ company[1] }}</option>
 % end
 % end
 </select><br>
 <input type="submit" value="Save">
 </form>
 <p><a href="/">Back to List</a></p>
</body>
</html>
