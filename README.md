<<<<<<< HEAD
# Instazone
 A  a clone of the image sharing network, Instagram. Users can sign up login, view and post photos and follow other users.
## Built By [Bryan Juma](https://github.com/Alampulo/)

## Description
This is an application that allows users to view images. Image details are stored in categories and tagged by Location. The admin is responsible for uploading, editing or deleting images.

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* Register and Sign in to the application.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like or Save a picture and leave a comment on it.

# Setup and installation

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the Instazone
* Create new images for showcasing
* Delete images
* Update image post details.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display  images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  signup** | All details should be viewed|
| To add an image  | **Through Admin dashboard** |  add  Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To comment an image  | **Through Admin dashboard ** | click on image object and confirm by comenting button|
| To search  | **Enter text in search bar** | Users can search by category|
| To filter by Location  | **Click drop-down on navbar** | Users can view images on homepage|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* git clone https://github.com/Alampulo/Instazone 
cd Not-Instagram
Activate virtual environment

create and acvite a virtual environment python3.6 -m venv virtual && source virtual/bin/activate

Install dependancies

Install dependancies that will create an environment for the app to run pip install -r requirements.txt

Create the Database

- psql
- CREATE DATABASE instazone;
.env file

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'instazone'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
Run initial Migration

python3.6 manage.py makemigrations instazone
python3.6 manage.py migrate
Run the app

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test images

## Technologies Used
* Python3. /Django
* postgresql
* Bootstrap4

## License

Copyright (c) 2018 Bryan Juma

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
=======

>>>>>>> a19d48ca5e7d915e861d019ec001acfdcff3485c
