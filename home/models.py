from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class userdata(models.Model):
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    Rpassword = models.CharField(max_length=20)
    website = models.URLField(max_length=100)
    state = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=30, default='')
    postalcode = models.IntegerField()
    file_upload = models.FileField(upload_to='upload')

    def __str__(self):
        return self.fname
    
# basic python programmes database
class basicPython(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to = "pythonimg")
    new_slug = AutoSlugField(populate_from = 'title', unique = True, null = True, default = None)

    def __str__(self):
        return self.title

# basic program of C
class Cprog(models.Model):
    title =  models.CharField(max_length=40)
    desc = models.TextField()
    image = models.ImageField(upload_to = "progC")
    new_slug = AutoSlugField(populate_from = 'title', unique = True, null = True, default = None)


    def __str__(self):
        return self.title

class websites(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to = "websiteimg")
    site = models.URLField(max_length=200)
    price = models.IntegerField()
    facebook = models.URLField(max_length=400)
    twitter = models.URLField(max_length=400)
    mail = models.EmailField(max_length=400)


    def __str__(self):
        return self.title

class code_desc(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to = "code")
    code = HTMLField()
    new_slug = AutoSlugField(populate_from = 'title', unique = True, null = True, default = None)



    def __str__(self):
        return self.title

# for c code desc
class c_code(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = "code")
    code = HTMLField()
    new_slug = AutoSlugField(populate_from = 'title', unique = True, null = True, default = None)


    def __str__(self):
        return self.title
    
            

    
    

    
    
    

    

      

