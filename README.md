django-html5-bootstrap-project
==============================

Django project template with HTML5 boilerplate and Twitter bootstrap. It also contains configurations for 2 deployment environments (development and production). It includes configurations for [Nginx](http://nginx.org/), [Supervisor](http://supervisord.org/) and [Gunicorn](http://gunicorn.org/).


Usage
-----

Having Django 1.4+ installed in your system you can run this line:

    django-admin.py startproject --template=https://github.com/juliomenendez/django-html5-bootstrap-project/zipball/master --extension=py,html,conf your_new_project
    
This will create a ```your_new_project``` directory in your current directory with all the settings and configurations defined in this template ready for your project.

The development environment uses basic authorization so outsiders cannot see your new shinning feature. The password file is ```conf/dev/basic_auth```