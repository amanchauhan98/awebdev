from django.db import models

# Create your models here.
class theory_topic(models.Model):
    subtitle = models.CharField(max_length=40)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'theoryTopic')
    desc = models.TextField()
    link = models.URLField(null=True)

    def __str__(self):
        return self.title



class course_blog(models.Model):
    course = models.CharField(max_length = 30)
    department = models.CharField(max_length=30)
    course_title = models.CharField(max_length=100)
    desc = models.TextField()


    def __str__(self):
        return self.course
    
    


