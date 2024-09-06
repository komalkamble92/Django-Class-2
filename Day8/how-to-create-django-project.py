'''
Steps to Create a Django Project and App
Install Python
Make sure Python (version 3.x) is installed on your computer.

Install Django
Open the terminal and type "pip install django" to install Django.

Create a Project Folder
Create a new folder for your project, then navigate into it using the terminal.

Start a New Django Project
In the terminal, type "django-admin startproject project_name" to create your Django project.

Navigate to the Project Folder
Go into the newly created project folder.

Run the Development Server
Type "python manage.py runserver" to start the Django development server.
Open a browser and go to "http://127.0.0.1:8000" to see your project.

Steps to Create a Django App
Create a New App
In the terminal, type "python manage.py startapp app_name" to create a new app inside your project.

Add the App to the Project
Open the settings.py file inside the project folder.
In the INSTALLED_APPS section, add your app's name (e.g., 'app_name').

Steps to Create a Model
Create a Model in the App
Open the models.py file inside your app folder.
Define a model (a class) to represent your data. For example, you could create a model called "Product" with fields like name, price, etc.

Apply the Changes to the Database
Run "python manage.py makemigrations" to create migration files for your model.
Then run "python manage.py migrate" to apply the changes to your database.

Use the Django Admin Panel
To manage your model using Django's admin panel, register the model in admin.py.
After that, create a superuser by typing "python manage.py createsuperuser" and follow the instructions.
Now you can log into "http://127.0.0.1:8000/admin" to manage your data.


'''