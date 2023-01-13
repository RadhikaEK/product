from django.db import models

# Create your models here.
class Details(models.Model):
    d_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=100)
    size = models.IntegerField()
    category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'details'