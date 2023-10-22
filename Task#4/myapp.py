from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from passlib.context import CryptContext
from uuid import uuid4

app = FastAPI()

users_db = {}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

registration_form = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Registration</title>
  </head>
  <body>
    <h1>Registration</h1>
    <form method="post" action="/register">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
  </body>
</html>
"""

login_form = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Login</title>
  </head>
  <body>
    <h1>Login</h1>
    <form method="post" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
  </body>
</html>
"""


@app.get("/register", response_class=HTMLResponse)
async def show_registration_form():
    return registration_form


@app.post("/register", response_class=HTMLResponse)
async def register(username: str = Form(...), password: str = Form(...)):
    hashed_password = pwd_context.hash(password)
    user_id = str(uuid4())
    users_db[user_id] = {
        "username": username,
        "password": hashed_password
    }
    return RedirectResponse(url="/login")

@app.get("/login", response_class=HTMLResponse)
async def show_login_form():
    return login_form

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = next((user_data for user_data in users_db.values() if user_data["username"] == username), None)
    if user and pwd_context.verify(password, user["password"]):
        # Implement your authentication logic here
        # For example, you can generate a JWT token for the user
        # For demonstration purposes, redirect to the user dashboard
        return RedirectResponse(url="/dashboard", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/dashboard", response_class=HTMLResponse)
async def user_dashboard():
    # Generate HTML for the table rows using registered users' data
    table_rows = ""
    for user_id, user_data in users_db.items():
        table_rows += f"<tr><td>{user_id}</td><td>{user_data['username']}</td></tr>"

    user_dashboard_html = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>User Dashboard</title>
      </head>
      <body>
        <h1>Welcome to Your Dashboard</h1>
        <p>You are logged in!</p>
        <h2>Registered Users</h2>
        <table border="1">
          <tr>
            <th>User ID</th>
            <th>Username</th>
          </tr>
          {table_rows}
        </table>
      </body>
    </html>
    """

    return HTMLResponse(content=user_dashboard_html)
