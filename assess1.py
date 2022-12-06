import psycopg2 # import

# Create connection

conn = psycopg2.connect(
   host="localhost",
   database="assessmentdb",
   user="postgres",
   password="Andre9119" # Change to your pasword
)

# Functions

def fetch_data(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM view_contacts;")
    rows = cur.fetchall()
    cur.close()
    return rows


def insert_contact(connection, first_name, last_name, title, organization):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO contacts (first_name, last_name, title, organization) VALUES ('{first_name}', '{last_name}', '{title}', '{organization}');")
    cur.close()

def list_contacts(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    return rows

def delete_contact(connection, contact_id):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM contacts WHERE id = '{contact_id}';")
    cur.close()

# 3.4
view_contacts = fetch_data(conn)
for row in view_contacts:
    print(row)
# 3.5 Main program
keep_going = True
while keep_going:
    command = input('Options: LIST, INSERT, DELETE, QUIT    Enter your choise:')
    if command == 'LIST':
        rows = list_contacts(conn)
        for row in rows:
            print(row)
    elif command == 'INSERT':
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        title = input('Enter title: ')
        organization = input('Enter organization: ')
        insert_contact(conn, first_name, last_name, title, organization)
    elif command == 'DELETE':
        contact_id = input('Enter the id you want to delete: ')
        delete_contact(conn, contact_id)
    elif command == 'QUIT':
        print('Have a nice day')
        conn.commit()
        conn.close()
        keep_going = False
    else:
        print('Invalid option')
