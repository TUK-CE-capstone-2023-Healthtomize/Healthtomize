from django.db import models
# Create your models here.

class food(models.Model):
    food_name = models.CharField(db_column='food_name', max_length=50, default=0)
    serving_size = models.IntegerField(db_column='serving_size', default=0)
    calories = models.IntegerField(db_column='calories', default=0)
    carbon = models.IntegerField(db_column='carbon', default=0)
    protein = models.IntegerField(db_column='protein', default=0)
    fat = models.IntegerField(db_column='fat', default=0)
    cholesterol = models.IntegerField(db_column='cholesterol', default=0)


    class Meta:
        #        managed = False
        db_table = 'food'

