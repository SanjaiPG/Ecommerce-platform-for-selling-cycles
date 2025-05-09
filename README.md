#E-commerce Platform for Selling Cycles
This is the web page for my summer internship project — an e-commerce platform for selling cycles.

🐧 Environment
Operating System: Linux (Arch)

Framework: Django (Python)

🔧 Getting Started
#Step 1: Set up a Python virtual environment

python -m venv virt

#Step 2: Activate the virtual environment

source virt/bin/activate

#Step 3: Install Django

pip install Django

#Step 4: Start a new Django project

django-admin startproject ecom

#Step 5: Create a Django app inside your project

cd ecom
python manage.py startapp skyraptor


#📁 Project Structure (after step 5)
ecom/
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
