from django.db import models
import bcrypt,re

class UsersManager(models.Manager):
    def logVals(self, data):
        err={}
        u=Users.objects.filter(email=data['email'])
        if not u:
            err['e']='Email is not Registered'
        else:
            u=Users.objects.get(email=data['email'])
            if not bcrypt.checkpw(data['pw'].encode(), u.password.encode()):
                err['p']='Incorrect Password'
        return err
    def regVals(self, d):
        err={}
        regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(d['fname'])<2:
            err['f']='First Name needs to be at least 2 characters'
        if len(d['lname'])<2:
            err['l']='Last Name needs to be at least 2 characters'
        if not regex.match(d['email']):
            err['e']='Invalid Email address'
        if len(d['pw'])<8:
            err['p']='Password needs to be at least 8 characters'
        if d['cpw']!=d['pw']:
            err['cp']='Passwords do not match'
        return err


class Users(models.Model):
    first_name=models.CharField(max_length=65)
    last_name=models.CharField(max_length=65)
    email=models.EmailField(max_length=255) 
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UsersManager()