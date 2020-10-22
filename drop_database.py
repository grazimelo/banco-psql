'''
Drop database with Python and subprocess.

https://gist.github.com/rg3915/4ffb0bfdccf1a205ee1761185730411d
'''
import subprocess

# Remove user and database
subprocess.call('psql -U postgres -c "DROP DATABASE my_db;"', shell=True)
subprocess.call('psql -U postgres -c "DROP USER my_user;"', shell=True)
