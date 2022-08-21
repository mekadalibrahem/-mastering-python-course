'''
====================================
-- 118 - Databases – SQLite Create Database And Connect 
-- link : https://www.youtube.com/watch?v=UokVrMqeu4o&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------------------------------
# -- Databases =&gt; SQLite =&gt; Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Create The Tables and Fields
db.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")

# Close Database
db.close()