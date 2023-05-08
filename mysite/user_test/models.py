from django.db import models

# Create your models here.
class Member(models.Model):
    member_id = models.CharField(db_column='member_id', max_length=50)
    passwd = models.CharField(db_column='passwd', max_length=50)
    name = models.CharField(db_column='name', max_length=50)
    email = models.CharField(db_column='email', max_length=50, blank=True)
    height = models.IntegerField(db_column='height', default=0)
    weight = models.IntegerField(db_column='weight', default=0)
    gender = models.CharField(db_column='gender', max_length=50, default=0)
    purpose = models.CharField(db_column='purpose', max_length=50, default=0)
    age = models.IntegerField(db_column='age', default=0)


    class Meta:
        #        managed = False
        db_table = 'member'
