#Django--web application framework
'''
Free and open source web framework
framework:combination of certain packages and components
for example if we want to build a web application..we will
not be building from scratch will be using some readymade here
 we use frameworks.
 example of web applications:
 Amazon
 Flipkart
 Meesho
 ola
 uber
 If we want to build these, we use Django,
 But to build websites we use HTML,CSS,Javascript
 HTML---design the page
 CSS----improve our design and to have uniformity in our design
 Javascript-- to make our website interact with us
 In front-end----HTML,CSS,Javascript

 Backend part-- suppose take facebook everyone will not see the
 same page.
 take amazon buy some things and make payment online certain processing
 done on backend part.
 That's where we need some languages backend part
 when it comes to web application framework:
 MVC(Model View Controller) is famous
 doesnt matter which  language we learn may be Java,PHP,ASP
 MVC is common in all
 Model---data
 view--HTML format
 controller--control the operations on screen.
 In general MVC will help to build good web application.
 In Django MVT(Model View Template) similar to MVC.
 replacing controller with template

 why to choose if we have other frameworks:
 1.Fast(not spend more time on configuration)
 -----helps to build applications faster.
 2.components(Advantage and disadvantage)
 eg:if we need to record a video..we need mike,camera,audio etc.,
 eg1:if we want to build a web application..we need login and database connectivity
 and all these comes bundled in Django
 3.security
 4.scalability
 what if ..if we want to have multiple users and multiple features,Django gives this.
 Here we are using Django 2.2 version.
 If we want to work with Django 2.2 version we require python versions starting from 3.4.
 To check python version:
 command prompt
 python --version
 if we install django it will be available for the entire machines.
 what if.. if we want to have different configurations for different projects.
 if we want to have isolated space which will not be effecting other projects.
 The way we can do is by installing virtual environment.
 pip install virtualenvwrapper-win

 create the enviroment

 mkvirtualenv

 to check whether the virtualenv is activated......workon name










in command prompt or terminal:
 ------pip install virtualenvwrapper-win
 --------mkvirtualenv test
 next installing django
 --------pip install django
 if we want to deactivate the virtualenv we create... deactivate
 if we want to get that back activated .........workon name
To check Django Version:
django-admin --version
4.0.1

#django is available only in our environment not in our system...we dont want to
disturb our entire system for our project.

#creating a project:
creating a folder in terminal  ...........mkdir projects
then next command ...........cd projects
#then we can see we are in that project
#To use that project .. need to use command again
that command is.........django-admin startproject name_of_the_project
#Before clicking enter we need to check the project is empty or not by going that location.
#now our folder is created in the location we specified.


#my project steps:

mkdir project2
cd project2
django-admin startproject firstproj
cd firstproj.......here we are in our proj firstproj
if we type ......dir # we see manage.py
#to run the server.....here we run the server without any coding
python manage.py runserver  .........https://127.0.0.1:8000
8000 is the port number and we can change it
then we can see .......The install worked successfully!congratulations!



To build a web applications:
two types:1.static page 2.Dynamic page
static page:same page for everyone
Dynamic page:different pages for different one.Eg:Facebook,Bank balance etc.,


initially we have to work on the same virual environment
workon srilekha2
python manage.py startapp calc



 '''








