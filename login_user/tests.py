from django.test import TestCase

# Create your tests here.
#coding=utf-8
__author__ = 'shifeixiang'

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.hashers import make_password, check_password
password = '123'
sha_pwd = make_password(password,None,'pbkdf2_sha256')
print sha_pwd
result = check_password(password,sha_pwd)
print result