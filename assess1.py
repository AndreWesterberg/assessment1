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



# 3.4
view_contacts = fetch_data(conn)
for row in view_contacts:
    print(row)
# 3.5 Main program
keep_going = True
while keep_going:
    command = input('Options: LIST, INSERT, DELETE, QUIT    Enter your choise:')
    if command == 'LIST':
        pass
    elif command == 'INSERT':
        pass
    elif command == 'DELETE':
        pass
    elif command == 'QUIT':
        print('Have a nice day')
        keep_going = False
    else:
        print('Invalid option')
