#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import cgi
import cgitb
from http import cookies
import os
import datetime
import time
import base64
import json

# Enable CGI error reporting
cgitb.enable()

# Database configuration
host = "localhost"
user = "root"
password = ""
database = "cropshield"

# Initialize session
def init_session():
    cookie = cookies.SimpleCookie()
    if 'HTTP_COOKIE' in os.environ:
        cookie.load(os.environ['HTTP_COOKIE'])
    
    session = {}
    if 'session' in cookie:
        session_data = cookie['session'].value
        try:
            session = json.loads(base64.b64decode(session_data).decode())
        except:
            pass
    
    return session

# Set up session
session = init_session()

# Print content type header
print("Content-type: text/html\n")
