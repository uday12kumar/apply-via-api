apply-via-api
=============
django app to upload resume

Getting Started
----
To use the app, you'll first need credentials to access the agiliq API. 
Login with registered email as your username, password and save the `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URL`.

Once you have an `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URL`. you'll need to create a `upload_cre.env` configuration 
file in your directory.

### upload_cre.env Example
    [Credentials]
    export CLIENT_ID=yourclientid
    export CLIENT_SECRET=YOURCLIENTSECRET
    export REDIRECT_URI=YOURREDIRECTURL

### Install packages
    $ pip install -r requirements.txt

Usage
----

source the environment variables
    ``$ source upload_cre.env``

You can run the server and apply the resume:
    ``$ python manage.py runserver``
    
