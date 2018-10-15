from django.db import models

# Create your models here.
class Areas(models.Model):
   atitle = models.CharField(max_length=20)
   p = models.ForeignKey('self', null=True, blank=True)
   class Meta():
       db_table = 'areas'
