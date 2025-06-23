# E-commerce Platform for Selling Cycles
This is the web page for my summer internship project — an e-commerce platform for selling cycles.

🐧 Environment

Operating System: Linux (Arch)

Framework: Django (Python)

🔧 Getting Started
# Step 1: Set up a Python virtual environment

python -m venv virt

# Step 2: Activate the virtual environment

source virt/bin/activate

# For Windows

virt\Scripts\activate.bat 

# Step 3: Install Django and Pillow

pip install Django

pip install Pillow

# Step 4: Start a new Django project

django-admin startproject ecom

# Step 5: Create a Django app inside your project

cd ecom
python manage.py startapp skyraptor


# 📁 Project Structure (after step 5)
```ecom/
├── ecom/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── skyraptor/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

# To run the local host server

python manage.py runserver

Also, make sure the virtual env is running

# And type localhost:8000 in your browser

# To use admin 

python manage.py migrate

localhost:8000/admin in your local web browser

# To create super user - admin
python manage.py createsuperuser