<!DOCTYPE html>
<html>
<head>
 <title>Mobiles and Companies</title>
</head>
<body>
 <form action="/" method="get">
 <label>Search:</label>
 <input type="text" name="search" placeholder="Enter title or company">
 <input type="submit" value="Search">
 </form>
 <h1>Mobiles and Companies</h1>
 <table border="1">
 <tr>
 <th>S.NO</th>
 <th>Model</th>
 <th>Release Year</th>
 <th>Company</th>
 <th>Edit</th>
 <th>Delete</th>
 </tr>
 % for mobile in mobiles:
 <tr>
 <td>{{ mobile[0] }}</td>
 <td>{{ mobile[1] }}</td>
 <td>{{ mobile[2] }}</td>
 <td>{{ mobile[3] }}</td>
 <td><a href="/edit/{{ mobile[0] }}">Edit</a></td>
 <td><a href="/delete/{{ mobile[0] }}" onclick="return confirm('Are you sure you want 
to delete this item?');">Delete</a></td>
 </tr>
 % end
 </table>
 <p><a href="/add">Add Mobile</a></p>
</body>
</html>
