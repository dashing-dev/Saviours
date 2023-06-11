from django.db import models



# Create your models here.
class Input(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length=500)
    datetime_field = models.DateTimeField()
    name = models.CharField(max_length=300)
    contact = models.IntegerField( max_length=10)
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title

    