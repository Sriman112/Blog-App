
from django.db import models

class blogpost(models.Model):
      
      title=models.CharField(max_length=20)
      body=models.TextField(max_length=150)
      timestamp=models.DateTimeField()

      
