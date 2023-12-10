<!DOCTYPE html>
<html>
<head>
 <title>Add Mobile</title>
</head>
<body>
 <h1>Add Mobile</h1>
 <form action="/add" method="post">
 <label>Title:</label>
 <input type="text" name="title" required><br>
 <label>Release Year:</label>
 <input type="number" name="release_year" required><br>
 <label>Company:</label>
 <select name="company_id">
 % for company in companies:
 <option value="{{ company[0] }}">{{ company[1] }}</option>
 % end
 </select><br>
 <input type="submit" value="Add">
 </form>
 <p><a href="/">Back to List</a></p>
</body>
</html>
