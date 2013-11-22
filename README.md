URL Shortener
========================

A very simple URL shortener written in Python/Django.

Installation
------------
1. Install all 3rd-party libs with pip:
<i>pip install -r requirements.txt</i>
2. Run syncdb:
<i>python manage.py syncdb</i>
3. Run the local web server:
<i>python manage.py runserver</i>


Usage
-----
Visit the main page at http://localhost:8000 to start using the app.

The admin site is located at http://localhost:8000/admin/ (note the trailing
slash).

<b>Some Notes:</b>
* The app checks whether a URL is already in the database and won't create
a new entry if it does.  It will simply display the corresponding short URL.
* The app also checks whether a URL is already shortened and will notify the
user if true.
