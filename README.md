# Drainomote
 
Drainomote is a small Python/Django web application to enable users to enable and disable real servers (a.k.a Draining) in KEMP Loadmaster load balancers. It possible to restrict users to drain specific real servers which is benefitial in a shared environment.
 
## Installation
 
It is best to run this in a Python virtual environement in order to avoid affecting system libraries.

**Requirements**

* Python 3
* Django
* Postgresql

Create virtualenv

> virtualenv -p python3 virtualenv

Activate your virtual environment and install following packages

> pip install django

In order to install psycopg2 you need the postgresql server dev package

> sudo apt-get install postgresql-server-dev-9.3  
> pip install psycopg2

Install python requests module

> pip install requests

### Database creation

Connect to postgresql using psql

> sudo -u postgres -H psql

Create a user and database

> CREATE USER "drainomote_user" WITH PASSWORD 'secret';  
> CREATE DATABASE "drainomote" OWNER "drainomote_user";

Set the database name and credentials in settings.py

Run Django migrations to initialize the database

> python manage.py migrate

## Usage
 
First step is to create your users and groups through the admin interface.

Then add the real server, and then assign which real servers should be available to each group.

Browse to the site, login and drain your servers.
 
## Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
 
## History
 
**0.8**  
Initial release, it's works but have some ruff edges here and there.
 
## License
 
> Copyright (C) 2014  Roger Steneteg
>
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
>
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <http://www.gnu.org/licenses/>.
