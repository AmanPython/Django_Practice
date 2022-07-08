from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    class Meta:
        ordering = ['first_name']
        db_table = '"person"'

    def __str__(self):
        return self.first_name + ' ' + self.last_name