from django.db import models

# Create your models here.
class  Contacts(models.Model):
    last_name = models.CharField(max_length=100, null = True, blank = False)
    first_name = models.CharField(max_length=100, null = True, blank = False)
    phone_number = models.CharField(max_length=100,  null = True, blank = True)
    email = models.EmailField(max_length=100, null = True, blank = True)
    image = models.URLField(null = True, blank = True)

    class Meta:
        db_table = 'contacts'
        unique_together = (('last_name', 'first_name'),)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'