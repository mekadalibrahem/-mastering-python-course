'''
====================================
-- 121 - Databases – SQLite Training’s On Everything 
-- link : https://www.youtube.com/watch?v=4dhxFHgsLyY&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ---------------------------------------------------
# -- Databases =&gt; SQLite =&gt; Training On Everything --
# ---------------------------------------------------

import sqlite3

def get_all_data():

  try:

    # Connect To Database
    db = sqlite3.connect("app.db")

    # Print Success Message
    print("Connected To Database Successfully")

    # Setting Up The Cursor
    cr = db.cursor()

    # Fetch Data From Database
    cr.execute("select * from users")

    # Assign Data To Variable
    results = cr.fetchall()

    # Print Number Of Rows
    print(f"Database Has {len(results)} Rows.")

    # Printing Message
    print("Showing Data:")

    # Loop On Results
    for row in results:

      print(f"UserID =&gt; {row[0]},", end=" ")

      print(f"Username =&gt; {row[1]}")

  except sqlite3.Error as er:

    print(f"Error Reading Data {er}")

  finally:

    if (db):

      # Close Database Connection
      db.close()

      print("Connection To Database Is Closed")

get_all_data()