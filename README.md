# ScoVille

## Steps to get This project started:

* Clone down the repo and `cd` into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv scovillenv`
  * `source ./scovillenv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv scovilleenv`
  * `source ./scovilleenv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`
* If you get this message: `Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.`

  *`winpty python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (NOTE: every time you run this it will remove existing data and repopulate it) 

  * `python manage.py loaddata scoville_scales`
  * `python manage.py loaddata blog_posts`

* Enjoy ScoVille!

  * `python manage.py runserver`
  
  * Navigate to http://localhost:8000/


## ERD

https://www.lucidchart.com/documents/edit/6cdecc2d-e9b5-4fbf-9799-6ba1368aebdd/0_0
