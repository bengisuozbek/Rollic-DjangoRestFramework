from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, editable=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(default='', max_length=50, unique=True)
    phone = models.CharField(max_length=15, blank=False)   
    password = models.CharField(max_length=15, blank=False)
    confirm_password = models.CharField(max_length=15, blank=False)

    def __str__(self):                  
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)