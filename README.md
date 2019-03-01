# Bangazon-LLC
This is an API for Bangazon LLC. This API will allow user to GET/POST/PUT and (sometimes) DELETE items from the Bangazon Database. Before you can utilize the database, there are a few things you need to make sure you have installed.

## Link to ERD

![Bangazon-ERD](/images/Bangazon-ERD.png "Bangazon-ERD")

# Core Technologies

## SQLite
### Installation of SQLite (if needed)

To get started, type the following command to check if you already have SQLite installed.

```bash
$ sqlite3
```

And you should see:

```
SQLite version 3.7.15.2 2014-08-15 11:53:05
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

If you do not see above result, then it means you do not have SQLite installed on your machine. Follow the appropriate instructions below.

#### For Windows

Go to [SQLite Download page](http://www.sqlite.org/download.html) and download the precompiled binaries for your machine. You will need to download `sqlite-shell-win32-*.zip` and `sqlite-dll-win32-*.zip` zipped files.

Create a folder `C:\sqlite` and unzip the files in this folder which will give you `sqlite3.def`, `sqlite3.dll` and `sqlite3.exe` files.

Add `C:\sqlite` to your [PATH environment variable](http://dustindavis.me/update-windows-path-without-rebooting/) and finally go to the command prompt and issue `sqlite3` command.

#### For Mac

First, try to install via Homebrew:

```
brew install sqlite3
```

If not, download the package from above. After downloading the files, follow these steps:

```
$tar -xvzf sqlite-autoconf-3071502.tar.gz
$cd sqlite-autoconf-3071502
$./configure --prefix=/usr/local
$make
$make install
```

#### For Linux

```
sudo apt-get update
sudo apt-get install sqlite3
```

## SQL Browser  - DB Browser

The [DB browser for SQLite](http://sqlitebrowser.org/) will let you view, query and manage your databases during the course.

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/download) is Microsoft's cross-platform editor that we'll be using during orientation for writing Python and building Django applications. Make sure you add the [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension immediately after installation completes.

## Python

This project uses Python and its web framework Django.

[Python Getting Started](https://www.python.org/about/gettingstarted/)

[Download Python](https://www.python.org/downloads/)

If you are using a Mac, see the [Python for Mac OS X](https://www.python.org/downloads/mac-osx/) page. MacOS 10.2 (Jaguar), 10.3 (Panther), 10.4 (Tiger) and 10.5 (Leopard) already include various versions of Python.

If you're running Windows: the most stable Windows downloads are available from the [Python for Windows](https://www.python.org/downloads/windows/) page.


## Setup Virtual Environment 

Enable a virtual environment at the level above your project.

Use the following commands in your terminal:
```
virtualenv env
source env/bin/activate
```
## Dependencies

Activate your vim and run `pip install -r requirements.txt`


### Django Project / Django App

Django is a Python Web framework. This project uses Django and requires Python to be installed. See above note on installing Python.

[Django Install](https://docs.djangoproject.com/en/2.1/topics/install/)

[Django for Windows](https://docs.djangoproject.com/en/2.1/howto/windows/)

### Django safedelete

[Django safedelete](https://django-safedelete.readthedocs.io/en/latest/)

You can choose what happens when you delete an object :

    * it can be masked from your database (soft delete, the default behavior)

    * it can be masked from your database and mask any dependent models. (cascading soft delete)

    * it can be normally deleted (hard delete)

    * it can be hard-deleted, but if its deletion would delete other objects, it will only be masked

    * it can be never deleted or masked from your database (no delete, use with caution)

**This project uses SOFT_DELETE_CASCADE**

example

```
# imports
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

# Models

# We create a new model, with the given policy : Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.
class Article(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=100)

class Order(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=100)
    articles = models.ManyToManyField(Article)
```


# Installing Bangazon

As of now, the database is going to be hosted on your local computer. There are a few things you need to make sure are in place before the database can be up and running.

1. Fork and clone the repo on to you local machine. 

2. Run makemigrations
`python manage.py makemigrations website`

3. Run migrate
`python manage.py migrate`
>This will create all the migrations needed for Django Framework to post items to the database based on the models in the Models/ directory

4. Add initial data
`python manage.py loaddata db.json`
>This will load data from the project's json file to your local database

## Run Server

`python manage.py runserver 8000`
Ctrl+C to quit

## Using the API
For now, all calls to the API will be made from `http://localhost:8000/api/v1` as the domain. All calls will be made from here. 

It should look like this:
![API-Root](/images/API-Root.png "API-Root")


### Each Module

* GET You can access a list of all employees by running a Get call to `http://localhost:8000/api/v1/{module_name}`
* GET one You can get the information on a single instance by runnning a Get call to `http://localhost:8000/website/{module_name}/{module_id}`
>Note you need to have a instance unique ID number to get the correct information or you can click on a URL provided in the corresponding list.

![Customers-Post](/images/Customers-Post.png "Customers-Post")


* PUT You can update the info on a specific instance by running a Put call to `http://localhost:8000/api/v1/{module_name}/{module_id}`.

![Customers-Post](/images/Customers-Post.png "Customers-Post")
    * From here, you can edit the existing information of this specific customer then click PUT to submit the edited customer.


* POST You can enter a new payment type by navigating to `http://localhost:8000/api/v1/{module_name}/`

![Customers-Post](/images/Customers-Post.png "Customers-Post")
    * Enter the relevant information then click POST to generate a new instance of this.

### Specific Search Queries

1. Customers: `http://localhost:8000/api/v1/customers`

* If the query string parameter of `?_include=products` is provided, then any products that the customer is selling should be included in the response.
* If the query string parameter of `?_include=payments` is provided, then any payment types that the customer has used to pay for an order should be included in the response.
* If the query string parameter of `q` is provided when querying the list of customers, then any customer that has property value that matches the pattern should be returned.

If `/customers?q=mic` is requested, then any customer whose first name is Michelle, or Michael, or Domicio should be returned. Any customer whose last name is Michaelangelo, or Omici, Dibromic should be returned.  Every property of the customer object should be checked for a match.

2. Orders:  `http://localhost:8000/api/v1/orders`

* Should be able to filter out completed orders with the ?completed=false query string parameter. If the parameter value is true, then only completed order should be returned.
* If the query string parameter of ?_include=products is in the URL, then the list of products in the order should be returned.
* If the query string parameter of ?_include=customers is in the URL, then the customer representation should be included in the response.

3. Departments: `http://localhost:8000/api/v1/departments`

* If the query string parameter of ?_include=employees is provided, then all employees in the department(s) should be included in the response.
* If the query string parameters of ?_filter=budget&_gt=300000 is provided on a request for the list of departments, then any department whose budget is $300,000, or greater, should be in the response.

This repo created by the Talkative Tangs of Cohort 28:

4. Training Programs: `http://localhost:8000/api/v1/training_programs`

* Should be able to view only programs starting today, or in the future, with the ?completed=false query string parameter.

[Bryan Nilsen](https://github.com/BryanNilsen)

[Lesley Boyd](https://github.com/laboyd001)

[Ousama Elayan](https://github.com/ousamasama/) - Team Leader

[Robby Hecht](https://github.com/robbyhecht)
