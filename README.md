
# Run before 
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


# Migrate databases
python manage.py migrate