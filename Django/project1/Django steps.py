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


#if we want to go to the exact location in the terminal
dir
cd locationname
and it should be in the same virtual envirorment we are using previously



#creating a homepage that displays hello world
creating a base.html from that we are giving background color
to access that background color
{% extends 'base.html' %}

{% block content %}
{% endblock %}



#addition of two numbers
creating a form in home.html
in the views we are writing a function
and giving url mapping in calc/urls and we get result in browser.

3.third part of Django session
GET vs POST
HTTP Methods



Http Protocol
Request Methods

client--------->server
here we are sending request from client to server
and we get response from server to client.

#when we send a request here we have  methods GET,POST,PUT,DELETE,HEAD,CONNECT,OPTION,TRACE,PATCH.
These are all the Request methods.
eg:suppose when you click on the link and we want the image---That is the GET REQUEST
that means we are expecting something from server.
here we are sending the request to server .. and response we get is send to the client,

supposing we are filling a form and sending to the server .. that's where we are submittign the data to the server.
here we use POST.
POST method is used for adding the new data to the server
GET method is used for fetching the data
PUT is to update the resource or the data to the server.
DELETE for deleting.


#In the addition example
we used the request type is GET.
in the address bar in the browser the data is not secure
in the address bar we have this for addition example but this is not secure
 http://127.0.0.1:8000/add?num1=5&num2=7
 To achieve that we should not be using GET ,use POST.
 suppose if want to send multiple data,many fields.. we dont want everything coming in
 address bar.
 Technically for submitting data we should always use POST.

 If we want to use POST method :
 go to html page
 <form action="add" method ='post'>

 and in the views : change to POST
 def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])

then run and see the address bar then we don't be getting the data in the address bar





TO FETCH DATA-------GET
TO SUBMIT DATA------POST


4.MODEL VIEW TEMPLATE(MVT/MTV)
as a user we go to particular website and fetch particular page that page can be static page
1.static page
in static page
1.Layout--designed in HTML,CSS,JavaScript
2.Data--data coming from database
3.Logic

we can build a page where we have Layout,Data,Logic
but sometimes it is better to sperate from one another is called separation of concerns.


Model View Template
Model-For data
Template--layout- -HTML,DTL-Django Template Language(To introduce dynamic data)

In views we will write the logic and views will use the Model object and Template










'''