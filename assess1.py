import psycopg2 # import

# Create connection
conn = psycopg2.connect(
   host="localhost",
   database="assessmentdb",
   user="postgres",
   password="Andre9119"
)
