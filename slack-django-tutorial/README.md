Ask leave bot
========
A slack bot to ask could you go from work or not.
<hr>

Requirements
------------

All you need - to clone repository, have python (python3 recommended), create virtual environment in project folder:

    $ python3 -m venv env_name

install there dependencies:

    $ . env_name/bin/activate
    $ pip install -r requirements.txt


Finally do migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

then create superuser for the project:

    $ python manage.py createsuperuser

and run in 2 separate terminals (each one in virtual environment):

    # first
    $ python manage.py runserver
    # second
    $ ./ngrok http 8000

Then change ngrok url in host parameters in settings.py

Ready! Go to 127.0.0.1:8000 and enjoy)

Using
-----

 /ask_leave/botv1.5 'your message' - to send message
 start new thread - to answer the message

<hr>
