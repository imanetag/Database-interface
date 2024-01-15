from os import system
import re
import mysql.connector
import os
# Making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="Ghost.Orchid45d", database="DATABASE-SQL_PROJECT")

# Make a regular expression for validating an Email
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# Make a regular expression for validating a Phone Number
phone_pattern = re.compile(r"\d{6,10}")


# Function to Add_Client
def Add_Client():
    print("{:>60}".format("-->> Add Client Record <<--"))
    ClientID = input("Enter Client ID: ")
    # Check if Project ID already exists
    if check_client(ClientID):
        print("Client ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Client()
    Nom = input("Enter Client Name: ")
    Prenom = input("Enter Client Last Name: ")
    Adresse = input("Enter Client Address: ")
    Adresse_email = input("Enter Client Email: ")
    Numero_de_telephone = input("Enter Client Phone Number: ")

    # Inserting Client Details into the Client table
    data = (ClientID, Nom, Prenom, Adresse, Adresse_email, Numero_de_telephone)
    sql = 'INSERT INTO Client VALUES (%s, %s, %s, %s, %s, %s)'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Added Client Record")
    except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")
        print("Client ID is already in use. Please choose a different ID.")

    press = input("Press Any Key To Continue..")
    main_menu()



# Function to Check if Client With given ID Exists or Not
def check_client(client_id):
    # Query to select all Rows from Client table
    sql = 'SELECT * FROM Client WHERE ClientID = %s'
    cursor = con.cursor(buffered=True)
    data = (client_id,)

    # Execute the SQL Query
    cursor.execute(sql, data)

    # Fetch the first row
    record = cursor.fetchone()

    if record:
        print("Client ID: ", record[0])
        print("Client Name: ", record[1])
        print("Client Last Name: ", record[2])
        print("Client Address: ", record[3])
        print("Client Email: ", record[4])
        print("Client Phone Number: ", record[5])
        print("\n")
        return True  # Client found

    else:
        print("Client not found.")
        return False  # Client not found



# Function to Display_Clients
def Display_Clients():
    print("{:>60}".format("-->> Display Client Records <<--"))
    # Query to select all rows from the Client Table
    sql = 'SELECT * FROM Client'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql)

    # Fetching all details of all the Clients
    records = cursor.fetchall()
    for record in records:
        print("Client ID: ", record[0])
        print("Client Name: ", record[1])
        print("Client Last Name: ", record[2])
        print("Client Address: ", record[3])
        print("Client Email: ", record[4])
        print("Client Phone Number: ", record[5])
        print("\n")
    press = input("Press Any key To Continue..")
    main_menu()

# Function to Add_Projet
def Add_Projet():
    print("{:>60}".format("-->> Add Project Record <<--"))
    ProjetID = input("Enter Project ID: ")
    # Check if Project ID already exists
    if check_projet(ProjetID):
        print("Project ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Projet()
    Nom_du_Projet = input("Enter Project Name: ")
    Date_de_debut = input("Enter Project Start Date (YYYY-MM-DD HH:MM:SS): ")
    Date_de_fin_prevue = input("Enter Project Expected End Date (YYYY-MM-DD HH:MM:SS): ")
    Statut = input("Enter Project Status: ")
    Description = input("Enter Project Description: ")
    ClientID = input("Enter Client ID for the Project: ")
    
    # Inserting Project Details into the Projet table
    data = (ProjetID, Nom_du_Projet, Date_de_debut, Date_de_fin_prevue, Statut, Description, ClientID)
    sql = 'INSERT INTO Projet VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Added Project Record")
    except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")
        print("Project ID is already in use. Please choose a different ID.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if Project With given ID Exists or Not
def check_projet(projet_id):
    # Query to select all Rows from Projet table
    sql = 'SELECT * FROM Projet WHERE ProjetID = %s'
    cursor = con.cursor()
    data = (projet_id,)

    # Execute the SQL Query
    cursor.execute(sql, data)

    # Fetch the first row
    record = cursor.fetchone()

    if record is not None:
        print("Project ID: ", record[0])
        print("Project Name: ", record[1])
        print("Start Date: ", record[2])
        print("Expected End Date: ", record[3])
        print("Status: ", record[4])
        print("Description: ", record[5])
        print("Client ID: ", record[6])
        print("\n")
        return True  # Project found
    else:
        print("Project not found.")
        return False  # Project not found


# Function to Display_Projets
def Display_Projets():
    print("{:>60}".format("-->> Display Project Records <<--"))
    # Query to select all rows from the Projet Table
    sql = 'SELECT * FROM Projet'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql)

    # Fetching all details of all the Projects
    records = cursor.fetchall()
    for record in records:
        print("Project ID: ", record[0])
        print("Project Name: ", record[1])
        print("Start Date: ", record[2])
        print("Expected End Date: ", record[3])
        print("Status: ", record[4])
        print("Description: ", record[5])
        print("Client ID: ", record[6])
        print("\n")
    press = input("Press Any key To Continue..")
    main_menu()

# Function to Add_Employe
def Add_Employe():
    print("{:>60}".format("-->> Add Employee Record <<--"))
    EmployeeID = input("Enter Employee ID: ")
    # Check if Employee ID already exists
    if check_employe(EmployeeID):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employe()
    Nom = input("Enter Employee Name: ")
    Prenom = input("Enter Employee Last Name: ")
    Adresse = input("Enter Employee Address: ")
    Adresse_email = input("Enter Employee Email: ")
    if re.fullmatch(email_regex, Adresse_email):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employe()
    Numero_de_telephone = input("Enter Employee Phone Number: ")
    if phone_pattern.match(Numero_de_telephone):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employe()
    Poste = input("Enter Employee Position: ")
    Salaire = input("Enter Employee Salary: ")
    Date_embauche = input("Enter Employee Hiring Date (YYYY-MM-DD HH:MM:SS): ")
    
    # Inserting Employee Details into the Employe table
    data = (EmployeeID, Nom, Prenom, Adresse, Adresse_email, Numero_de_telephone, Poste, Salaire, Date_embauche)
    sql = 'INSERT INTO Employe VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Added Employee Record")
    except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")
        print("Employee ID is already in use. Please choose a different ID.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if Employee With given ID Exists or Not
def check_employe(employe_id):
    # Query to select all Rows from Employe table
    sql = 'SELECT * FROM Employe WHERE EmployeeID = %s'
    cursor = con.cursor()
    data = (employe_id,)

    # Execute the SQL Query
    cursor.execute(sql, data)

    # Fetch the first row
    record = cursor.fetchone()

    if record is not None:
        print("Employee ID: ", record[0])
        print("Employee Name: ", record[1])
        print("Employee Last Name: ", record[2])
        print("Employee Address: ", record[3])
        print("Employee Email: ", record[4])
        print("Employee Phone Number: ", record[5])
        print("Employee Position: ", record[6])
        print("Employee Salary: ", record[7])
        print("Hiring Date: ", record[8])
        print("\n")
        return True  # Employee found
    else:
        print("Employee not found.")
        return False  # Employee not found


# Function to Display_Employes
def Display_Employes():
    print("{:>60}".format("-->> Display Employee Records <<--"))
    # Query to select all rows from the Employe Table
    sql = 'SELECT * FROM Employe'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql)

    # Fetching all details of all the Employees
    records = cursor.fetchall()
    for record in records:
        print("Employee ID: ", record[0])
        print("Employee Name: ", record[1])
        print("Employee Last Name: ", record[2])
        print("Employee Address: ", record[3])
        print("Employee Email: ", record[4])
        print("Employee Phone Number: ", record[5])
        print("Employee Position: ", record[6])
        print("Employee Salary: ", record[7])
        print("Hiring Date: ", record[8])
        print("\n")
    press = input("Press Any key To Continue..")
    main_menu()



# Function to Add_Tache
def Add_Tache():
    print("{:>60}".format("-->> Add Task Record <<--"))
    TacheID = input("Enter Task ID: ")
    Description_de_la_tache = input("Enter Task Description: ")
    Date_de_debut = input("Enter Task Start Date (YYYY-MM-DD HH:MM:SS): ")
    Date_de_fin_prevue = input("Enter Task Expected End Date (YYYY-MM-DD HH:MM:SS): ")
    Statut = input("Enter Task Status: ")
    Responsable = input("Enter Responsible Employee ID: ")

    # Inserting Task Details into the Tache table
    data = (TacheID, Description_de_la_tache, Date_de_debut, Date_de_fin_prevue, Statut, Responsable)
    sql = 'INSERT INTO Tache VALUES (%s, %s, %s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Task Record")
    press = input("Press Any Key To Continue..")
    main_menu()

def Display_All_Tasks():
    print("{:>60}".format("-->> Display All Tasks <<--"))
    sql = 'SELECT * FROM Tache'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        tasks = cursor.fetchall()

        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print("Task ID:", task[0])
                print("Task Description:", task[1])
                print("Start Date:", task[2])
                print("Expected End Date:", task[3])
                print("Status:", task[4])
                print("Responsible Employee ID:", task[5])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display tasks.")

    press = input("Press Any Key To Continue..")
    main_menu()

def check_task(task_id):
    sql = 'SELECT * FROM Tache WHERE TacheID=%s'
    data = (task_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        task = cursor.fetchone()

        if task:
            print("Task ID:", task[0])
            print("Task Description:", task[1])
            print("Start Date:", task[2])
            print("Expected End Date:", task[3])
            print("Status:", task[4])
            print("Responsible Employee ID:", task[5])
            print("Task exists.")
            return True
        else:
            print("Task doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check task existence.")

    return False


# Function to Add_Utilisateur
def Add_Utilisateur():
    print("{:>60}".format("-->> Add User Record <<--"))
    UtilisateurID = input("Enter User ID: ")
    Nom_d_utilisateur = input("Enter Username: ")
    Mot_de_passe = input("Enter Password: ")
    EmployeeID = input("Enter Employee ID: ")

    # Inserting User Details into the Utilisateur table
    data = (UtilisateurID, Nom_d_utilisateur, Mot_de_passe, EmployeeID)
    sql = 'INSERT INTO Utilisateur VALUES (%s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added User Record")
    press = input("Press Any Key To Continue..")
    main_menu()

def Display_All_Users():
    print("{:>60}".format("-->> Display All Users <<--"))
    sql = 'SELECT * FROM Utilisateur'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        users = cursor.fetchall()

        if not users:
            print("No users found.")
        else:
            for user in users:
                print("User ID:", user[0])
                print("Username:", user[1])
                print("Employee ID:", user[3])
                print("Passwords:", user[2])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display users.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if User With given ID Exists or Not
def check_user(user_id):
    sql = 'SELECT * FROM Utilisateur WHERE UtilisateurID=%s'
    data = (user_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        user = cursor.fetchone()

        if user:
            print("User ID:", user[0])
            print("Username:", user[1])
            print("Employee ID:", user[3])
            print("Passwords:", user[2])
            print("User exists.")
            return True
        else:
            print("User doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check user existence.")

    return False



# Function to Add_Paiement
def Add_Paiement():
    print("{:>60}".format("-->> Add Payment Record <<--"))
    PaiementID = input("Enter Payment ID: ")
    ClientID = input("Enter Client ID: ")
    Montant = input("Enter Amount: ")
    Date_de_paiement = input("Enter Payment Date (YYYY-MM-DD HH:MM:SS): ")
    Mode_paiement = input("Enter Payment Mode: ")

    # Inserting Payment Details into the Paiement table
    data = (PaiementID, ClientID, Montant, Date_de_paiement, Mode_paiement)
    sql = 'INSERT INTO Paiement VALUES (%s, %s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Payment Record")
    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Display All Payments
def Display_All_Payments():
    print("{:>60}".format("-->> Display All Payments <<--"))
    sql = 'SELECT * FROM Paiement'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        payments = cursor.fetchall()

        if not payments:
            print("No payments found.")
        else:
            for payment in payments:
                print("Payment ID:", payment[0])
                print("Client ID:", payment[1])
                print("Amount:", payment[2])
                print("Payment Date:", payment[3])
                print("Payment Mode:", payment[4])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display payments.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if Payment With given ID Exists or Not
def check_payment(payment_id):
    sql = 'SELECT * FROM Paiement WHERE PaiementID=%s'
    data = (payment_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        payment = cursor.fetchone()

        if payment:
            print("Payment ID:", payment[0])
            print("Client ID:", payment[1])
            print("Amount:", payment[2])
            print("Payment Date:", payment[3])
            print("Payment Mode:", payment[4])
            print("Payment exists.")
            return True
        else:
            print("Payment doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check payment existence.")

    return False


# Function to Add_Facture
def Add_Facture():
    print("{:>60}".format("-->> Add Invoice Record <<--"))
    FactureID = input("Enter Invoice ID: ")
    Montant = input("Enter Amount: ")
    Date_emission = input("Enter Issue Date (YYYY-MM-DD HH:MM:SS): ")
    Date_echeance = input("Enter Due Date (YYYY-MM-DD HH:MM:SS): ")
    Statut = input("Enter Status: ")
    ClientID = input("Enter Client ID: ")

    # Inserting Invoice Details into the Facture table
    data = (FactureID, Montant, Date_emission, Date_echeance, Statut, ClientID)
    sql = 'INSERT INTO Facture VALUES (%s, %s, %s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Invoice Record")
    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Display All Invoices
def Display_All_Invoices():
    print("{:>60}".format("-->> Display All Invoices <<--"))
    sql = 'SELECT * FROM Facture'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        invoices = cursor.fetchall()

        if not invoices:
            print("No invoices found.")
        else:
            for invoice in invoices:
                print("Invoice ID:", invoice[0])
                print("Amount:", invoice[1])
                print("Issue Date:", invoice[2])
                print("Due Date:", invoice[3])
                print("Status:", invoice[4])
                print("Client ID:", invoice[5])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display invoices.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if Invoice With given ID Exists or Not
def check_invoice(invoice_id):
    sql = 'SELECT * FROM Facture WHERE FactureID=%s'
    data = (invoice_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        invoice = cursor.fetchone()

        if invoice:
            print("Invoice ID:", invoice[0])
            print("Amount:", invoice[1])
            print("Issue Date:", invoice[2])
            print("Due Date:", invoice[3])
            print("Status:", invoice[4])
            print("Client ID:", invoice[5])
            print("Invoice exists.")
            return True
        else:
            print("Invoice doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check invoice existence.")

    return False


# Function to Add_Equipe
def Add_Equipe():
    print("{:>60}".format("-->> Add Team Record <<--"))
    EquipeID = input("Enter Team ID: ")
    Nom_de_l_Equipe = input("Enter Team Name: ")
    Description = input("Enter Team Description: ")
    Chef_d_Equipe = input("Enter Team Leader ID: ")

    # Inserting Team Details into the Equipe table
    data = (EquipeID, Nom_de_l_Equipe, Description, Chef_d_Equipe)
    sql = 'INSERT INTO Equipe VALUES (%s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Team Record")
    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Display All Teams
def Display_All_Teams():
    print("{:>60}".format("-->> Display All Teams <<--"))
    sql = 'SELECT * FROM Equipe'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        teams = cursor.fetchall()

        if not teams:
            print("No teams found.")
        else:
            for team in teams:
                print("Team ID:", team[0])
                print("Team Name:", team[1])
                print("Team Description:", team[2])
                print("Team Leader ID:", team[3])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display teams.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if Team With given ID Exists or Not
def check_team(team_id):
    sql = 'SELECT * FROM Equipe WHERE EquipeID=%s'
    data = (team_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        team = cursor.fetchone()

        if team:
            print("Team ID:", team[0])
            print("Team Name:", team[1])
            print("Team Description:", team[2])
            print("Team Leader ID:", team[3])
            print("Team exists.")
            return True
        else:
            print("Team doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check team existence.")

    return False


# Function to Add_Membre_de_l_Equipe
def Add_Membre_de_l_Equipe():
    print("{:>60}".format("-->> Add Team Member Record <<--"))
    MembreID = input("Enter Team Member ID: ")
    Nom = input("Enter First Name: ")
    Prenom = input("Enter Last Name: ")
    Adresse = input("Enter Address: ")
    Email = input("Enter Email: ")
    Telephone = input("Enter Phone Number: ")
    Competences = input("Enter Skills: ")
    Date_de_Debut_dans_l_Equipe = input("Enter Joining Date (YYYY-MM-DD HH:MM:SS): ")
    Date_de_Fin_dans_l_Equipe = input("Enter Leaving Date (YYYY-MM-DD HH:MM:SS): ")
    EquipeID = input("Enter Team ID: ")

    # Inserting Team Member Details into the Membre_de_l_Equipe table
    data = (MembreID, Nom, Prenom, Adresse, Email, Telephone, Competences,
            Date_de_Debut_dans_l_Equipe, Date_de_Fin_dans_l_Equipe, EquipeID)
    sql = 'INSERT INTO Membre_de_l_Equipe VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Team Member Record")
    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Add_Module
def Add_Module():
    print("{:>60}".format("-->> Add Module Record <<--"))
    ModuleID = input("Enter Module ID: ")
    Nom_du_Module = input("Enter Module Name: ")
    Description = input("Enter Module Description: ")
    Technologie_utilisee = input("Enter Used Technology ID: ")

    # Inserting Module Details into the Module table
    data = (ModuleID, Nom_du_Module, Description, Technologie_utilisee)
    sql = 'INSERT INTO Module VALUES (%s, %s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Module Record")
    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Display All Modules
def Display_All_Modules():
    print("{:>60}".format("-->> Display All Modules <<--"))
    sql = 'SELECT * FROM Module'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        modules = cursor.fetchall()

        if not modules:
            print("No modules found.")
        else:
            for module in modules:
                print("Module ID:", module[0])
                print("Module Name:", module[1])
                print("Module Description:", module[2])
                print("Used Technology ID:", module[3])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display modules.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Check if Module With given ID Exists or Not
def check_module(module_id):
    sql = 'SELECT * FROM Module WHERE ModuleID=%s'
    data = (module_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        module = cursor.fetchone()

        if module:
            print("Module ID:", module[0])
            print("Module Name:", module[1])
            print("Module Description:", module[2])
            print("Used Technology ID:", module[3])
            print("Module exists.")
            return True
        else:
            print("Module doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check module existence.")

    return False


def Add_Technologie():
    print("{:>60}".format("-->> Add Technology Record <<--"))
    TechnologieID = input("Enter Technology ID: ")
    # Check if Technology ID already exists
    if check_technologie(TechnologieID):
        print("Technology ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Technologie()
    Nom_de_la_technologie = input("Enter Technology Name: ")
    Description = input("Enter Technology Description: ")
    
    # Inserting Technology Details into the Technologie table
    data = (TechnologieID, Nom_de_la_technologie, Description)
    sql = 'INSERT INTO Technologie VALUES (%s, %s, %s)'
    cursor = con.cursor()

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Technology Record")
    press = input("Press Any Key To Continue..")
    main_menu()
# Function to Check if Technology With given ID Exists or Not# Function to Display Technologies
def Display_Technologies():
    print("{:>60}".format("-->> Display Technology Records <<--"))
    # Query to select all rows from the Technologie Table
    sql = 'SELECT * FROM Technologie'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        # Fetching all details of all the Technologies
        records = cursor.fetchall()

        if not records:
            print("No technologies found.")
        else:
            for record in records:
                print("Technology ID: ", record[0])
                print("Technology Name: ", record[1])
                print("Technology Description: ", record[2])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display technologies.")

    press = input("Press Any key To Continue..")
    main_menu()

# Function to Check if Technology With given ID Exists or Not
def check_technologie(technologie_id):
    # Query to select all Rows from Technologie table
    sql = 'SELECT * FROM Technologie WHERE TechnologieID = %s'
    cursor = con.cursor(buffered=True)
    data = (technologie_id,)

    try:
        # Execute the SQL Query
        cursor.execute(sql, data)
        # Fetch the first row
        record = cursor.fetchone()

        if record is not None:
            print("Technology ID: ", record[0])
            print("Technology Name: ", record[1])
            print("Technology Description: ", record[2])
            print("Technology exists.")
            return True  # Technology found
        else:
            print("Technology doesn't exist.")
            return False  # Technology not found

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check technology existence.")

    return False



# Function to Update_Client
def Update_Client():
    print("{:>60}".format("-->> Update Client Record <<--"))
    ClientID = input("Enter Client ID to update: ")

    # Check if Client ID exists
    if not check_client(ClientID):
        print("Client ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom = input("Enter updated Client Name: ")
    Prenom = input("Enter updated Client Last Name: ")
    Adresse = input("Enter updated Client Address: ")
    Adresse_email = input("Enter updated Client Email: ")
    Numero_de_telephone = input("Enter updated Client Phone Number: ")

    # Update Client Details in the Client table
    sql = 'UPDATE Client SET Nom=%s, Prenom=%s, Adresse=%s, Adresse_email=%s, Numero_de_telephone=%s WHERE ClientID=%s'
    data = (Nom, Prenom, Adresse, Adresse_email, Numero_de_telephone, ClientID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Client Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Client Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Client
def Delete_Client():
    print("{:>60}".format("-->> Delete Client Record <<--"))
    ClientID = input("Enter Client ID to delete: ")

    # Check if Client ID exists
    if not check_client(ClientID):
        print("Client ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this client? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Client Record from the Client table
    sql = 'DELETE FROM Client WHERE ClientID=%s'
    data = (ClientID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Client Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Client Record.")

    press = input("Press Any Key To Continue..")
    main_menu()


# Function to Update_Project
def Update_Project():
    print("{:>60}".format("-->> Update Project Record <<--"))
    ProjectID = input("Enter Project ID to update: ")

    # Check if Project ID exists
    if not check_projet(ProjectID):
        print("Project ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom_du_Projet = input("Enter updated Project Name: ")
    Date_de_debut = input("Enter updated Project Start Date (YYYY-MM-DD HH:MM:SS): ")
    Date_de_fin_prevue = input("Enter updated Project Expected End Date (YYYY-MM-DD HH:MM:SS): ")
    Statut = input("Enter updated Project Status: ")
    Description = input("Enter updated Project Description: ")
    ClientID = input("Enter updated Client ID for the Project: ")

    # Update Project Details in the Projet table
    sql = 'UPDATE Projet SET Nom_du_Projet=%s, Date_de_debut=%s, Date_de_fin_prevue=%s, Statut=%s, Description=%s, ClientID=%s WHERE ProjetID=%s'
    data = (Nom_du_Projet, Date_de_debut, Date_de_fin_prevue, Statut, Description, ClientID, ProjectID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Project Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Project Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Project
def Delete_Project():
    print("{:>60}".format("-->> Delete Project Record <<--"))
    ProjectID = input("Enter Project ID to delete: ")

    # Check if Project ID exists
    if not check_projet(ProjectID):
        print("Project ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this project? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Project Record from the Projet table
    sql = 'DELETE FROM Projet WHERE ProjetID=%s'
    data = (ProjectID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Project Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Project Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Update_Employee
def Update_Employee():
    print("{:>60}".format("-->> Update Employee Record <<--"))
    EmployeeID = input("Enter Employee ID to update: ")

    # Check if Employee ID exists
    if not check_employe(EmployeeID):
        print("Employee ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom = input("Enter updated Employee Name: ")
    Prenom = input("Enter updated Employee Last Name: ")
    Adresse = input("Enter updated Employee Address: ")
    Adresse_email = input("Enter updated Employee Email: ")
    Numero_de_telephone = input("Enter updated Employee Phone Number: ")
    Poste = input("Enter updated Employee Position: ")
    Salaire = input("Enter updated Employee Salary: ")
    Date_embauche = input("Enter updated Employee Hiring Date (YYYY-MM-DD HH:MM:SS): ")

    # Update Employee Details in the Employe table
    sql = 'UPDATE Employe SET Nom=%s, Prenom=%s, Adresse=%s, Adresse_email=%s, Numero_de_telephone=%s, Poste=%s, Salaire=%s, Date_embauche=%s WHERE EmployeeID=%s'
    data = (Nom, Prenom, Adresse, Adresse_email, Numero_de_telephone, Poste, Salaire, Date_embauche, EmployeeID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Employee Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Employee Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Employee
def Delete_Employee():
    print("{:>60}".format("-->> Delete Employee Record <<--"))
    EmployeeID = input("Enter Employee ID to delete: ")

    # Check if Employee ID exists
    if not check_employe(EmployeeID):
        print("Employee ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this employee? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Employee Record from the Employe table
    sql = 'DELETE FROM Employe WHERE EmployeeID=%s'
    data = (EmployeeID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Employee Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Employee Record.")

    press = input("Press Any Key To Continue..")
    main_menu()


# Function to Update_Technology
def Update_Technology():
    print("{:>60}".format("-->> Update Technology Record <<--"))
    TechnologieID = input("Enter Technology ID to update: ")

    # Check if Technology ID exists
    if not check_technologie(TechnologieID):
        print("Technology ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom_de_la_technologie = input("Enter updated Technology Name: ")
    Description = input("Enter updated Technology Description: ")

    # Update Technology Details in the Technologie table
    sql = 'UPDATE Technologie SET Nom_de_la_technologie=%s, Description=%s WHERE TechnologieID=%s'
    data = (Nom_de_la_technologie, Description, TechnologieID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Technology Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Technology Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Technology
def Delete_Technology():
    print("{:>60}".format("-->> Delete Technology Record <<--"))
    TechnologieID = input("Enter Technology ID to delete: ")

    # Check if Technology ID exists
    if not check_technologie(TechnologieID):
        print("Technology ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this technology? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Technology Record from the Technologie table
    sql = 'DELETE FROM Technologie WHERE TechnologieID=%s'
    data = (TechnologieID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Technology Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Technology Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Update_User
def Update_User():
    print("{:>60}".format("-->> Update User Record <<--"))
    UtilisateurID = input("Enter User ID to update: ")

    # Check if User ID exists
    if not check_user(UtilisateurID):
        print("User ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom_d_utilisateur = input("Enter updated Username: ")
    Mot_de_passe = input("Enter updated Password: ")
    EmployeeID = input("Enter updated Employee ID: ")

    # Update User Details in the Utilisateur table
    sql = 'UPDATE Utilisateur SET Nom_d_utilisateur=%s, Mot_de_passe=%s, EmployeeID=%s WHERE UtilisateurID=%s'
    data = (Nom_d_utilisateur, Mot_de_passe, EmployeeID, UtilisateurID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated User Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update User Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_User
def Delete_User():
    print("{:>60}".format("-->> Delete User Record <<--"))
    UtilisateurID = input("Enter User ID to delete: ")

    # Check if User ID exists
    if not check_user(UtilisateurID):
        print("User ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this user? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete User Record from the Utilisateur table
    sql = 'DELETE FROM Utilisateur WHERE UtilisateurID=%s'
    data = (UtilisateurID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted User Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete User Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Update_Payment
def Update_Payment():
    print("{:>60}".format("-->> Update Payment Record <<--"))
    PaiementID = input("Enter Payment ID to update: ")

    # Check if Payment ID exists
    if not check_payment(PaiementID):
        print("Payment ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    ClientID = input("Enter updated Client ID: ")
    Montant = input("Enter updated Amount: ")
    Date_de_paiement = input("Enter updated Payment Date (YYYY-MM-DD HH:MM:SS): ")
    Mode_paiement = input("Enter updated Payment Mode: ")

    # Update Payment Details in the Paiement table
    sql = 'UPDATE Paiement SET ClientID=%s, Montant=%s, Date_de_paiement=%s, Mode_paiement=%s WHERE PaiementID=%s'
    data = (ClientID, Montant, Date_de_paiement, Mode_paiement, PaiementID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Payment Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Payment Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Payment
def Delete_Payment():
    print("{:>60}".format("-->> Delete Payment Record <<--"))
    PaiementID = input("Enter Payment ID to delete: ")

    # Check if Payment ID exists
    if not check_payment(PaiementID):
        print("Payment ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this payment? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Payment Record from the Paiement table
    sql = 'DELETE FROM Paiement WHERE PaiementID=%s'
    data = (PaiementID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Payment Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Payment Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Update_Invoice
def Update_Invoice():
    print("{:>60}".format("-->> Update Invoice Record <<--"))
    FactureID = input("Enter Invoice ID to update: ")

    # Check if Invoice ID exists
    if not check_invoice(FactureID):
        print("Invoice ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    ClientID = input("Enter updated Client ID: ")
    Date_de_facturation = input("Enter updated Invoice Date (YYYY-MM-DD HH:MM:SS): ")
    Montant = input("Enter updated Amount: ")
    Date_de_paiement = input("Enter updated Payment Date (YYYY-MM-DD HH:MM:SS): ")

    # Update Invoice Details in the Facture table
    sql = 'UPDATE Facture SET ClientID=%s, Date_de_facturation=%s, Montant=%s, Date_de_paiement=%s WHERE FactureID=%s'
    data = (ClientID, Date_de_facturation, Montant, Date_de_paiement, FactureID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Invoice Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Invoice Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Invoice
def Delete_Invoice():
    print("{:>60}".format("-->> Delete Invoice Record <<--"))
    FactureID = input("Enter Invoice ID to delete: ")

    # Check if Invoice ID exists
    if not check_invoice(FactureID):
        print("Invoice ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this invoice? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Invoice Record from the Facture table
    sql = 'DELETE FROM Facture WHERE FactureID=%s'
    data = (FactureID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Invoice Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Invoice Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Update_Team
def Update_Team():
    print("{:>60}".format("-->> Update Team Record <<--"))
    EquipeID = input("Enter Team ID to update: ")

    # Check if Team ID exists
    if not check_team(EquipeID):
        print("Team ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom_de_lequipe = input("Enter updated Team Name: ")
    Description = input("Enter updated Team Description: ")

    # Update Team Details in the Equipe table
    sql = 'UPDATE Equipe SET Nom_de_lequipe=%s, Description=%s WHERE EquipeID=%s'
    data = (Nom_de_lequipe, Description, EquipeID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Team Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Team Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Team
def Delete_Team():
    print("{:>60}".format("-->> Delete Team Record <<--"))
    EquipeID = input("Enter Team ID to delete: ")

    # Check if Team ID exists
    if not check_team(EquipeID):
        print("Team ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this team? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Team Record from the Equipe table
    sql = 'DELETE FROM Equipe WHERE EquipeID=%s'
    data = (EquipeID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Team Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Team Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

def Display_All_Team_Members():
    print("{:>60}".format("-->> Display All Team Members <<--"))
    sql = 'SELECT * FROM Membre_de_l_Equipe'
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql)
        team_members = cursor.fetchall()

        if not team_members:
            print("No team members found.")
        else:
            for member in team_members:
                print("Team Member ID:", member[0])
                print("First Name:", member[1])
                print("Last Name:", member[2])
                print("Address:", member[3])
                print("Email:", member[4])
                print("Phone Number:", member[5])
                print("Skills:", member[6])
                print("Joining Date:", member[7])
                print("Leaving Date:", member[8])
                print("Team ID:", member[9])
                print("-----------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to display team members.")

    press = input("Press Any Key To Continue..")
    main_menu()

def check_team_member(member_id):
    sql = 'SELECT * FROM Membre_de_l_Equipe WHERE MembreID=%s'
    data = (member_id,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        member = cursor.fetchone()

        if member:
            print("Team Member ID:", member[0])
            print("First Name:", member[1])
            print("Last Name:", member[2])
            print("Address:", member[3])
            print("Email:", member[4])
            print("Phone Number:", member[5])
            print("Skills:", member[6])
            print("Joining Date:", member[7])
            print("Leaving Date:", member[8])
            print("Team ID:", member[9])
            print("Team member exists.")
            return True
        else:
            print("Team member doesn't exist.")
            return False

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to check team member existence.")

    return False



# Function to Update_Team_Member
def Update_Team_Member():
    print("{:>60}".format("-->> Update Team Member Record <<--"))
    MembreID = input("Enter Team Member ID to update: ")

    # Check if Team Member ID exists
    if not check_team_member(MembreID):
        print("Team Member ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom = input("Enter updated First Name: ")
    Prenom = input("Enter updated Last Name: ")
    Adresse = input("Enter updated Address: ")
    Email = input("Enter updated Email: ")
    Telephone = input("Enter updated Phone Number: ")
    Competences = input("Enter updated Skills: ")
    Date_de_Debut_dans_l_Equipe = input("Enter updated Joining Date (YYYY-MM-DD HH:MM:SS): ")
    Date_de_Fin_dans_l_Equipe = input("Enter updated Leaving Date (YYYY-MM-DD HH:MM:SS): ")
    EquipeID = input("Enter updated Team ID: ")

    # Update Team Member Details in the Membre_de_l_Equipe table
    sql = 'UPDATE Membre_de_l_Equipe SET Nom=%s, Prenom=%s, Adresse=%s, Email=%s, Telephone=%s, Competences=%s, Date_de_Debut_dans_l_Equipe=%s, Date_de_Fin_dans_l_Equipe=%s, EquipeID=%s WHERE MembreID=%s'
    data = (Nom, Prenom, Adresse, Email, Telephone, Competences, Date_de_Debut_dans_l_Equipe, Date_de_Fin_dans_l_Equipe, EquipeID, MembreID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Team Member Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Team Member Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Team_Member
def Delete_Team_Member():
    print("{:>60}".format("-->> Delete Team Member Record <<--"))
    MembreID = input("Enter Team Member ID to delete: ")

    # Check if Team Member ID exists
    if not check_team_member(MembreID):
        print("Team Member ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this team member? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Team Member Record from the Membre_de_l_Equipe table
    sql = 'DELETE FROM Membre_de_l_Equipe WHERE MembreID=%s'
    data = (MembreID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Team Member Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Team Member Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Update_Module
def Update_Module():
    print("{:>60}".format("-->> Update Module Record <<--"))
    ModuleID = input("Enter Module ID to update: ")

    # Check if Module ID exists
    if not check_module(ModuleID):
        print("Module ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom_du_Module = input("Enter updated Module Name: ")
    Description = input("Enter updated Module Description: ")
    Technologie_utilisee = input("Enter updated Used Technology ID: ")

    # Update Module Details in the Module table
    sql = 'UPDATE Module SET Nom_du_Module=%s, Description=%s, Technologie_utilisee=%s WHERE ModuleID=%s'
    data = (Nom_du_Module, Description, Technologie_utilisee, ModuleID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Module Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Module Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Module
def Delete_Module():
    print("{:>60}".format("-->> Delete Module Record <<--"))
    ModuleID = input("Enter Module ID to delete: ")

    # Check if Module ID exists
    if not check_module(ModuleID):
        print("Module ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this module? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Module Record from the Module table
    sql = 'DELETE FROM Module WHERE ModuleID=%s'
    data = (ModuleID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Module Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Module Record.")

    press = input("Press Any Key To Continue..")
    main_menu()


# Function to Update_Task
def Update_Task():
    print("{:>60}".format("-->> Update Task Record <<--"))
    TacheID = input("Enter Task ID to update: ")

    # Check if Task ID exists
    if not check_task(TacheID):
        print("Task ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Get updated information from the user
    Nom_de_la_Tache = input("Enter updated Task Name: ")
    Description = input("Enter updated Task Description: ")
    Date_de_Debut = input("Enter updated Start Date (YYYY-MM-DD HH:MM:SS): ")
    Date_de_Fin = input("Enter updated End Date (YYYY-MM-DD HH:MM:SS): ")
    ModuleID = input("Enter updated Module ID: ")
    MembreID = input("Enter updated Team Member ID: ")

    # Update Task Details in the Tache table
    sql = 'UPDATE Tache SET Nom_de_la_Tache=%s, Description=%s, Date_de_Debut=%s, Date_de_Fin=%s, ModuleID=%s, MembreID=%s WHERE TacheID=%s'
    data = (Nom_de_la_Tache, Description, Date_de_Debut, Date_de_Fin, ModuleID, MembreID, TacheID)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Updated Task Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to update Task Record.")

    press = input("Press Any Key To Continue..")
    main_menu()

# Function to Delete_Task
def Delete_Task():
    print("{:>60}".format("-->> Delete Task Record <<--"))
    TacheID = input("Enter Task ID to delete: ")

    # Check if Task ID exists
    if not check_task(TacheID):
        print("Task ID not found.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Confirm deletion
    confirmation = input("Are you sure you want to delete this task? (yes/no): ").lower()
    if confirmation != "yes":
        print("Deletion canceled.")
        press = input("Press Any Key To Continue..")
        main_menu()

    # Delete Task Record from the Tache table
    sql = 'DELETE FROM Tache WHERE TacheID=%s'
    data = (TacheID,)
    cursor = con.cursor()

    try:
        # Executing the SQL Query
        cursor.execute(sql, data)
        # Commit() method to make changes in the table
        con.commit()
        print("Successfully Deleted Task Record")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        print("Failed to delete Task Record.")

    press = input("Press Any Key To Continue..")
    main_menu()


# Main Menu function
def main_menu():
    while True:
        print("\n{:^60}".format("<< Main Menu >>"))
        print("1. Manage Clients")
        print("2. Manage Projects")
        print("3. Manage Employees")
        print("4. Manage Technologies")
        print("5. Manage Users")
        print("6. Manage Payments")
        print("7. Manage Invoices")
        print("8. Manage Teams")
        print("9. Manage Team Members")
        print("10. Manage Modules")
        print("11. Manage Tasks")
        print("0. Exit")
        
        choice = input("Enter your choice (0-11): ")

        if choice == '1':
            client_menu()
        elif choice == '2':
            project_menu()
        elif choice == '3':
            employee_menu()
        elif choice == '4':
            technology_menu()
        elif choice == '5':
            user_menu()
        elif choice == '6':
            payment_menu()
        elif choice == '7':
            invoice_menu()
        elif choice == '8':
            team_menu()
        elif choice == '9':
            team_member_menu()
        elif choice == '10':
            module_menu()
        elif choice == '11':
            task_menu()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 11.")

# Example sub-menu (you need to define these functions)
def client_menu():
    while True:
        print("\n{:^60}".format("<< Client Menu >>"))
        print("1. Add Client")
        print("2. Update Client")
        print("3. Delete Client")
        print("4. Check_clients")
        print("5. Display_clients")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Client()
        elif choice == '2':
            Update_Client()
        elif choice == '3':
            Delete_Client()
        elif choice == '4':
            client_id = input("Enter Client ID to check: ")
            check_client(client_id)
        elif choice == '5':
            Display_Clients()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for projects
def project_menu():
    while True:
        print("\n{:^60}".format("<< Project Menu >>"))
        print("1. Add Project")
        print("2. Update Project")
        print("3. Delete Project")
        print("4. Check Projects")
        print("5. Display Projects")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Projet()
        elif choice == '2':
            Update_Project()
        elif choice == '3':
            Delete_Project()
        elif choice == '4':
            projet_id = input("Enter Project ID to check: ")
            check_projet(projet_id)
        elif choice == '5':
            Display_Projets()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for employees
def employee_menu():
    while True:
        print("\n{:^60}".format("<< Employee Menu >>"))
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Check Employees")
        print("5. Display  Employees")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Employe()
        elif choice == '2':
            Update_Employee()
        elif choice == '3':
            Delete_Employee()
        elif choice == '4':
            employe_id = input("Enter Employee ID to check: ")
            check_employe(employe_id)
        elif choice == '5':
            Display_Employes()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

# Define sub-menus for technologies, users, payments, invoices, teams, team members, modules, and tasks similarly.

# Example sub-menu for technologies
def technology_menu():
    while True:
        print("\n{:^60}".format("<< Technology Menu >>"))
        print("1. Add Technology")
        print("2. Update Technology")
        print("3. Delete Technology")
        print("4. Check Technology")
        print("5. Display Technology")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Technologie()
        elif choice == '2':
            Update_Technology()
        elif choice == '3':
            Delete_Technology()
        elif choice == '4' :
            technologie_id = input("Enter Technology ID to check: ")
            check_technologie(technologie_id)
        elif choice == '5' :
            Display_Technologies()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

# Define sub-menus for users, payments, invoices, teams, team members, modules, and tasks similarly.

# Example sub-menu for users
def user_menu():
    while True:
        print("\n{:^60}".format("<< User Menu >>"))
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Display All Users")
        print("5. Check All users")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Utilisateur()
        elif choice == '2':
            Update_User()
        elif choice == '3':
            Delete_User()
        elif choice == '4':
            Display_All_Users()
        elif choice == '5':
            user_id = input("Enter User ID to check: ")
            check_user(user_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for payments
def payment_menu():
    while True:
        print("\n{:^60}".format("<< Payment Menu >>"))
        print("1. Add Payment")
        print("2. Update Payment")
        print("3. Delete Payment")
        print("4. Display All Payments")
        print("5. Check All Payments")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Paiement()
        elif choice == '2':
            Update_Payment()
        elif choice == '3':
            Delete_Payment()
        elif choice == '4':
            Display_All_Payments()
        elif choice == '5':
            payment_id = input("Enter Payment ID to check: ")
            check_payment(payment_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for invoices
def invoice_menu():
    while True:
        print("\n{:^60}".format("<< Invoice Menu >>"))
        print("1. Add Invoice")
        print("2. Update Invoice")
        print("3. Delete Invoice")
        print("4. Display Invoice")
        print("5. Check Invoice")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Facture()
        elif choice == '2':
            Update_Invoice()
        elif choice == '3':
            Delete_Invoice()
        elif choice == '4':
            Display_All_Invoices()
        elif choice == '5':
            invoice_id = input("Enter Invoice ID to check: ")
            check_invoice(invoice_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

# Define sub-menus for teams, team members, modules, and tasks similarly.

# Example sub-menu for teams
def team_menu():
    while True:
        print("\n{:^60}".format("<< Team Menu >>"))
        print("1. Add Team")
        print("2. Update Team")
        print("3. Delete Team")
        print("4. Display Team")
        print("5. Check Teams")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Equipe()
        elif choice == '2':
            Update_Team()
        elif choice == '3':
            Delete_Team()
        elif choice == '4':
            Display_All_Teams()
        elif choice == '5':
            team_id = input("Enter Team ID to check: ")
            check_team(team_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for team members
def team_member_menu():
    while True:
        print("\n{:^60}".format("<< Team Member Menu >>"))
        print("1. Add Team Member")
        print("2. Update Team Member")
        print("3. Delete Team Member")
        print("4. Display Team Member")
        print("5. Check Team Members")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Membre_de_l_Equipe()
        elif choice == '2':
            Update_Team_Member()
        elif choice == '3':
            Delete_Team_Member()
        elif choice == '4':
            Display_All_Team_Members()
        elif choice == '5':
            team_member_id = input("Enter Team Member ID to check: ")
            check_team_member(team_member_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for modules
def module_menu():
    while True:
        print("\n{:^60}".format("<< Module Menu >>"))
        print("1. Add Module")
        print("2. Update Module")
        print("3. Delete Module")
        print("4. Display Modules")
        print("5. Check Modules")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Module()
        elif choice == '2':
            Update_Module()
        elif choice == '3':
            Delete_Module()
        elif choice == '4':
            Display_All_Modules()
        elif choice == '5':
            module_id = input("Enter Module ID to check: ")
            check_module(module_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


# Example sub-menu for tasks
def task_menu():
    while True:
        print("\n{:^60}".format("<< Task Menu >>"))
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Display All Tasks")
        print("5. Check Tasks")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            Add_Tache()
        elif choice == '2':
            Update_Task()
        elif choice == '3':
            Delete_Task()
        elif choice == '4':
            Display_All_Tasks()
        elif choice == '5':
            task_id = input("Enter Task ID to check: ")
            check_task(task_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

main_menu()
