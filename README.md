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

The following considerations are for a production environment using an Apache web server.

First install mod_wsgi from source or from your distribution repository.

**Important** Be shure the mod_wsgi version is compatible with python version you use (2 or 3)

fisrt go to your server root directory and clone the project than run the following commands:

```
cd /srv/www/htdocs
git clone https://github.com/marcotcal/tkprj
cd tkprj
python3 -m virtualenv venv
source venv/bin/activate
pip3 install django
pip3 install django-bootstrap3
pip3 install django-bootstrap-static
pip3 install psycopg2-binary
```

This is the time to create you production database and a schema named tickets

```
python3 manage.py migrate
python3 manage.py makemigrations tickets
python3 manage.py migrate tickets
python3 manage.py loaddata tickets/initial_data/db.status.json
python3 manage.py loaddata tickets/initial_data/db.priority.json
python3 manage.py loaddata tickets/initial_data/db.type.json 
```

If there is an error message comment the trigger creation sequence (I did not fixed it yet, I'm accepting sugestions)
run the last sequence, uncoment and run the last sequence again

Continuing:

```
python3 manage.py createsuperuser
```

Follow the instructions (name, email, passwords)

Test the instalation:

```
python3 manage.py runserver

[crtl]+[c]
```

if it is ok...

```
deactivate
```

**Now you have to configure the Apache server.**

This is my virtual host configuration

```
<VirtualHost *:80>

    ServerName  www.mysite.com
    ServerAdmin marco.castro@mysite.com

    Alias /static/  /srv/www/htdocs/tkprj/tickets/static/

    Alias /media/  /srv/www/htdocs/tkprj/run/media/

    WSGIScriptAlias / /srv/www/htdocs/tkprj/tkprj/wsgi.py

    WSGIDaemonProcess   tkprj  python-path=/srv/www/htdocs/tkprj:/srv/www/htdocs/tkprj/venv/lib64/python3.4/site-packages

    WSGIProcessGroup    tkprj

    <Directory /srv/www/htdocs/tkprj/run/static>
        Options -Indexes
        Order deny,allow
        Allow from all
    </Directory>

    <Directory /srv/www/htdocs/tkprj/run/media>
        Options -Indexes
        Order deny,allow
        Allow from all
    </Directory>

    LogLevel warn

    ErrorLog    /srv/www/htdocs/tkprj/tkprj_error.log
    CustomLog   /srv/www/htdocs/tkprj/tkprj_access.log combined
</VirtualHost>

```  

Make shure you have a this on your apache configuration

(you must adatp it to your server system)

```
LoadModule wsgi_module                    /usr/lib64/apache2/mod_wsgi.so
```  

include this lines on your settings file: 

This is important for the css and javascript static files 

```
STATIC_ROOT = '/srv/www/htdocs/tkprj/tickets/static'
STATIC_URL = '/static/'
```

run on the virtual environment


```
python3 manage.py collectstatic
```



## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - Programming language used at this project
* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
* [PostgreSQL](https://www.postgresql.org/) - The world's most advanced open source database
* [Vi](https://www.vim.org/) - «Using a free version of vi is not a sin but a penance.» (Richard Stallman, a priest of Church of Emacs)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/marcotcal/tkprj/tags). 

## Authors

* **Marco Túlio Castro** - *Initial work* - [marcotcal](https://github.com/marcotcal)

See also the list of [contributors](https://github.com/marcotcal/tkprj/contributors) who participated in this project.

## License

This project is licensed under the GPL 3 License - see the [GNU Public License V3](https://www.gnu.org/licenses/gpl-3.0.txt) file for details

## Acknowledgments

* Dum Dum for all the support. 





