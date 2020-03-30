##Instructions for using ScoVille
In your terminal, clone down the repo: git@github.com:CPJackson777/ScoVille.git

Cd into the repo: cd scoville

Create a virtual environment:
Windows:
python -m venv scovillenv
source ./scovilleenv/Scripts/activate
Mac:
python -m venv scovilleenv
source ./scovilleenv/bin/activate

Install dependencies: pip install -r requirements.txt

Create a database:
python manage.py makemigrations
python manage.py migrate

Load the scoville scale and blog post data in the database from fixtures:
python manage.py loaddata scoville_scales
python manage.py loaddata blog_posts

Run the server: python manage.py runserver

Navigate to http://localhost:8000/
