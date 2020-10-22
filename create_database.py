'''
Create database with Python and subprocess.

https://gist.github.com/rg3915/4ffb0bfdccf1a205ee1761185730411d
'''
import subprocess
from getpass import getpass

# DDL - data definition language

# Remove user and database
# subprocess.call('psql -U postgres -c "DROP DATABASE my_db;"', shell=True)
# subprocess.call('psql -U postgres -c "DROP USER my_user;"', shell=True)

# Create user ad hoc, P is password, E is ENCRYPTED.
# subprocess.call("createuser -U postgres -PE my_user_test", shell=True)

# Create database ad hoc with postgres user.
# subprocess.call("createdb -U postgres my_db_test", shell=True)

# input will be hidden
password = getpass('Type password: ')

# Tip: use python-decouple to define password on .env file.

# Create role user with password typed.
create_role = f"CREATE ROLE my_user ENCRYPTED PASSWORD '{password}' login;"
subprocess.call(f'psql -U postgres -c "{create_role}"', shell=True)

# Create database
create_db = "CREATE DATABASE my_db OWNER my_user;"
subprocess.call(f'psql -U postgres -c "{create_db}"', shell=True)
