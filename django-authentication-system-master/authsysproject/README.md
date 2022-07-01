# CVMe Install instructions
## Installation for virtual environment

Python 3.8 must be downloaded to be compatible with Fauna.

https://www.python.org/downloads/release/python-380/ - This is where to download it.

First, create the file you want the virt environment to go to.

```
mkdir "name of file"
cd "name of file"
```

Next, install Python 3.8 into the virtual environment.

```
py -m venv venv
venv\Scripts\activate.bat
```

The virtual environment will be working now. This will be displayed by having (venv) before the folder path.

Next is installing Django and Fauna, then starting it.

```
pip install django
pip install pytz
$ pip install faunadb
django-admin startproject "name of file"
python manage.py startapp users
```
