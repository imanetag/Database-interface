import tkinter as tk
from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__, static_folder='static')

# Replace these with your MySQL credentials
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ghost.Orchid45d",
    database="DATABASE-SQL_PROJECT"
)

cursor = con.cursor()
# Database Connection Context Manager
class DatabaseConnection:
    def __enter__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ghost.Orchid45d",
            database="DATABASE-SQL_PROJECT"
        )
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.connection.close()
# Assuming you have a simple user authentication mechanism
def authenticate(username, password):
    # Replace this with your actual authentication logic
    valid_username = "admin"
    valid_password = "adminx"

    return username == valid_username and password == valid_password

@app.route('/')
def login_page():
    return render_template('login.html', error_message=None)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if authenticate(username, password):
        # Successful login, redirect to the admin dashboard
        return redirect(url_for('admin_dashboard'))
    else:
        # Incorrect credentials, render login page with an error message
        error_message = "Invalid username or password. Please try again."
        return render_template('login.html', error_message=error_message)

@app.route('/admin/dashboard')
def admin_dashboard():
    # Render the admin dashboard with functionalities
    return render_template('admin_dashboard.html')

# Define routes
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/client_operations')
def client_operations():
    clients = display_clients()  # Replace with your actual function
    return render_template('client_operations.html', clients=clients)



# Client Operations
def check_client(client_id):
    sql = 'SELECT * FROM Client WHERE ClientID = %s'
    cursor.execute(sql, (client_id,))
    record = cursor.fetchone()
    return bool(record)

# Client Operations
def display_clients():
    print("{:>60}".format("-->> Display Client Records <<--"))
    # Query to select all rows from the Client Table
    sql = 'SELECT * FROM Client'
    cursor.execute(sql)

    # Fetching all details of all the Clients
    records = cursor.fetchall()

    # Print entire record for debugging
    for record in records:
        print("Client Record:", record)

    return records





@app.route('/display_clients')
def display_clients_route():
    clients = display_clients()
    return render_template('display_clients.html', clients=clients)


def add_client(client_id, nom, prenom, adresse, email, telephone):
    with DatabaseConnection() as db_connection:
        try:
            sql = 'INSERT INTO Client VALUES (%s, %s, %s, %s, %s, %s)'
            data = (client_id, nom, prenom, adresse, email, telephone)
            db_connection.cursor.execute(sql, data)
            return True
        except mysql.connector.IntegrityError:
            return False

def update_client(client_id, nom, prenom, adresse, email, telephone):
    with DatabaseConnection() as db_connection:
        try:
            sql = 'UPDATE Client SET Nom=%s, Prenom=%s, Adresse=%s, Adresse_email=%s, Numero_de_telephone=%s WHERE ClientID=%s'
            data = (nom, prenom, adresse, email, telephone, client_id)
            db_connection.cursor.execute(sql, data)
            return True
        except mysql.connector.Error:
            return False

def delete_client(client_id):
    with DatabaseConnection() as db_connection:
        try:
            sql = 'DELETE FROM Client WHERE ClientID=%s'
            db_connection.cursor.execute(sql, (client_id,))
            return True
        except mysql.connector.Error:
            return False

# Flask App Routes

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/add_client', methods=['GET', 'POST'])
def add_client_route():
    if request.method == 'POST':
        client_id = request.form['clientID']
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        email = request.form['email']
        telephone = request.form['telephone']

        if check_client(client_id):
            error_message = "Client ID already exists. Try again with a different ID."
            return render_template('add_client.html', error_message=error_message)

        if add_client(client_id, nom, prenom, adresse, email, telephone):
            return redirect(url_for('display_clients_route'))
        else:
            error_message = "Error adding client. Please check the provided data."
            return render_template('add_client.html', error_message=error_message)

    return render_template('add_client.html', error_message=None)

@app.route('/update_client', methods=['GET', 'POST'])
def update_client_route():
    if request.method == 'POST':
        client_id = request.form['clientID']
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']
        email = request.form['email']
        telephone = request.form['telephone']

        if update_client(client_id, nom, prenom, adresse, email, telephone):
            return redirect(url_for('display_clients_route'))
        else:
            error_message = "Failed to update client. Please check the provided data."
            return render_template('update_client.html', error_message=error_message)

    return render_template('update_client.html')

@app.route('/delete_client', methods=['GET', 'POST'])
def delete_client_route():
    if request.method == 'POST':
        client_id = request.form['clientID']

        if delete_client(client_id):
            return redirect(url_for('display_clients_route'))
        else:
            error_message = "Failed to delete client. Please try again."
            return render_template('delete_client.html', error_message=error_message)

    return render_template('delete_client.html')

if __name__ == '__main__':
    app.run(debug=True)
