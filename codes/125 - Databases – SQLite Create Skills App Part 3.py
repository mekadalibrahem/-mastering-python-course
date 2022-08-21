'''
====================================
-- 125 - Databases – SQLite Create Skills App Part 3 
-- link : https://www.youtube.com/watch?v=Bi5BMs9fc80&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# -----------------------------------------------------
# -- Databases =&gt; SQLite =&gt; Create Skills App Part 3 --
# -----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

def commit_and_close():
  """Commit Changes and Close Connection To Database"""
  db.commit()  # Save (Commit) Changes
  db.close()  # Close Database
  print("Connection To Database Is Closed")

# My User ID
uid = 2

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" =&gt; Show All Skills
"a" =&gt; Add New Skill
"d" =&gt; Delete A Skill
"u" =&gt; Update Skill Progress
"q" =&gt; Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():

  cr.execute(f"select * from skills where user_id = '{uid}'")

  results = cr.fetchall()

  print(f"You Have {len(results)} Skills.")

  if len(results) &gt; 0:

    print("Showing Skills With Progress: ")

  for row in results:

    print(f"Skill =&gt; {row[0]},", end=" ")

    print(f"Progress =&gt; {row[1]}%")

  commit_and_close()

def add_skill():

  sk = input("Write Skill Name: ").strip().capitalize()

  prog = input("Write Skill Progress ").strip()

  cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{uid}')")

  commit_and_close()

def delete_skill():

  sk = input("Write Skill Name: ").strip().capitalize()

  cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")

  commit_and_close()

def update_skill():

  print("Update Skill Progress")

  commit_and_close()

# Check If Command Is Exists
if user_input in commands_list:

  # print(f"Command Found {user_input}")

  if user_input == "s":

    show_skills()

  elif user_input == "a":

    add_skill()

  elif user_input == "d":

    delete_skill()

  elif user_input == "u":

    update_skill()

  else:

    print("App Is Closed.")

    commit_and_close()

else:

  print(f"Sorry This Command \"{user_input}\" Is Not Found")