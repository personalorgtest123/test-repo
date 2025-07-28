query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))