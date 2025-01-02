from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    subject = models.CharField(max_length=300,null=True)
    message = models.CharField(max_length=700,null=True)

    def __str__(self):
        return self.name
