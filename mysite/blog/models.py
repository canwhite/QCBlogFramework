from django.db import models

# Create your models here.


class CommonData(models.Model):
    
    
    title = models.CharField(max_length = 200)
    
    content = models.TextField()
    
    time = models.DateTimeField(auto_now = True)
    





