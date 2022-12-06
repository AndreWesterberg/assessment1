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

# Main program
view_contacts = fetch_data(conn)
for row in view_contacts:
    print(row)
