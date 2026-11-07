from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages, session
import sqlite3
import requests

app = Flask(__name__)
app.secret_key="ewdjefhuehfuhfefkofjefhjhh"

# Function to connect to database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
with get_db_connection() as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()

@app.route("/")
def home():
    name = session.get("username")
    return render_template("index.html",name = name)
   

@app.route("/register.html/", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        if name and email and password:
            try:
                with get_db_connection() as conn:
                    conn.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
                    conn.commit()
                flash("Registered Successfully! Please login.")
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash("Email already registered.")
                return render_template("register.html")
        else:
            flash("Please fill all fields.")
            return render_template("register.html")
    
    return render_template("register.html")


@app.route("/login.html/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        with get_db_connection() as conn:
            user = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password)).fetchone()
        
        if user:
            flash("Login Successful!!")
            session['username'] = user['name'] 
            return redirect(url_for("home"))
        else:
            flash("Login failed")
            error_message = "Invalid email or password."
            return render_template("login.html", error_message=error_message)
    
    return render_template("login.html")

@app.route("/logout/", methods = ['GET'])
def logout():
    session.clear()  # Sab session data hata do
    flash("You have been succesfully logged out.")
    return redirect(url_for('home'))

@app.route("/subscription.html/", methods=['GET', 'POST'])
def subscription():
    return render_template("subscription.html")


@app.route('/select_plan')   #methods = get is optional here becasue by default flask interprets method as get method so not required

def select_plan():
    return redirect(url_for('icici'))

@app.route('/icici')
def icici():
    return render_template('icici.html')

@app.route('/proceed_to_pay')
def proceed_to_pay():
    return redirect(url_for('payment_success'))

@app.route('/payment_success')
def payment_success():
    return render_template('payment_success.html')

@app.route('/session_expired')
def session_expired():
    return render_template('session_expired.html')

@app.route('/explore.html', methods = ["GET","POST"])
def explore():
    if request.method=="POST":
       search_term = request.form.get('search_term')
    else:
        search_term = "sports or technology"

    api = "4fc8a20028a64ce5869e744142d8210a"
    url = f"https://newsapi.org/v2/everything?q={search_term}&apiKey={api}"
    
    r = requests.get(url)
    data = r.json()
    articles = data["articles"]
    
    
    return render_template('explore.html', news = articles)




if __name__ == "__main__":
    app.run(debug=True, port=5000)
