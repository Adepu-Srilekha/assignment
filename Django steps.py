'''#create new project
python --version

pip install virtualenvwrapper-win
mkvirtualenv name

workon name

pip install django

django-admin --version

mkdir projects

cd projects

django-admin startproject name_of_the_project

from the pycharm open the project we created

we need on work on the same environement
workon srilekha2

python manage.py startapp calc

calc is created in our project

#creating a homepage that displays hello world



In the views: function
in calc url:route
firstproj/url:
we are bringing that and putting that function url in firstproj/url
Django Template Language(DTL):
In template we can have dynamic content and we can change the data in it
#how to call this home.html
go to settings.....DIRS
and specify the path in the
.......template
[os.path .join(BASE_DIR,'templates')]

#then we have to change views.py



If want to have our name dynamic..
#to fetch the name from database
go to views
in return  use {}



'''