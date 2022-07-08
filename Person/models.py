from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30,default='')
    last_name = models.CharField(max_length=30,default='')
    SHIRT_sIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=30,default='')
    shirt_size = models.CharField(max_length=1, choices=SHIRT_sIZES,default='')



    class Meta:
        ordering = ['first_name']                    # Python manage.py migrate
        db_table = '"person"'                        # python manage.py makemigrations

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Musician(models.Model):
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    instrument = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Album(models.Model):      # Avoiding the use of the reserved word clean,save, or delete.
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    release_date = models.DateField(default='')
    num_start = models.IntegerField(default=0)