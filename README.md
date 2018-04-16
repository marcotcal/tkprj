# Ticket Project

This is a ticket application based on DJango Framework. 
Although it is possible to use any Database Manager this application is being developed using PostgreSQL.
If you want to port the application to another database you have to rewrite the triggers of the create_triggers.sql file

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this program you will need Python Version >= 3.4.5, Django 

```
pip3 install django-appconf
pip3 install django-bootstrap-static
pip3 install django-bootstrap3
pip3 install django-picklefield
pip3 install django-schemas
pip3 install django-storages
pip3 install django-tenant-schemas

```

### Installing

## Development Environment

Folow this steps:

use git clone to obtain tkprj and go to ./tkprj directory

create a database called tkprj on your local PostgreSQL server or use a remote one.
In case of using a remote database modify the settings.py to configure the connection

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tkprj',
        'HOST': '127.0.0.1',
        'USER': 'username', 
        'PASSWORD': 'password',
	'PORT': '5432',	
    }
}
```
The database must have a **tickets** schema so, you have to create it ! :)

execute the  following commands: 
```
python3 manage.py migrate
python3 manage.py makemigrations tickets
python3 manage.py migrate tickets
python3 manage.py loaddata tickets/initial_data/db.status.json
python3 manage.py loaddata tickets/initial_data/db.priority.json
python3 manage.py loaddata tickets/initial_data/db.type.json
python3 manage.py createsuperuser (follow the instructions)

python3 manage.py runserver
```

use 
```
http://localhost:80000/admin
``` 
to create the other users and groups.

If you have more than one company create a group for each company and assign the group for the users of that company.
If you have one company and various departments create one group for each department and assign the users of that department.

At this point you will can go to your browser and use the URL:

http://localhost:8000/tickets

Enjoy :)

## Production Environment

Coming soon !!



