# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from datetime import date

# class Myrecordentry(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=25)
#     username = models.CharField(db_column='Username', max_length=25)  # Field name made lowercase.
#     password = models.CharField(max_length=35)
#     dob = models.DateField(db_column='DOB')  # Field name made lowercase.

#     class Meta:
#         managed = True
#         db_table = 'myrecordentry'


class test1(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)  # Field name made lowercase.
    password = models.CharField(max_length=100)
    dob = models.DateField(default=date.today)  # Field name made lowercase.

    class Meta:
        db_table = 'test1'