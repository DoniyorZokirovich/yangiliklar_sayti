
import os

os.system('cmd /k "python -m venv venv && venv\Scripts\\activate && pip install django && django-admin startproject src . && python manage.py startapp sayt && mkdir static && mkdir media && mkdir templates"')

