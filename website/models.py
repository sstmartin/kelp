# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Businesses(models.Model):
    business_id = models.CharField(primary_key=True, max_length=40)
    full_address = models.CharField(max_length=125, blank=True)
    hours = models.CharField(max_length=500, blank=True)
    is_open = models.CharField(max_length=10, blank=True)
    categories = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=50, blank=True)
    review_count = models.IntegerField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True)
    neighborhoods = models.CharField(max_length=250, blank=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True)
    stars = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    attributes = models.CharField(max_length=3000, blank=True)
    item_type = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'businesses'


class Reviews(models.Model):
    votes = models.CharField(max_length=100, blank=True)
    user_id = models.CharField(max_length=40)
    review_id = models.CharField(primary_key=True, max_length=40)
    stars = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    text = models.CharField(max_length=15000, blank=True)
    item_type = models.CharField(max_length=6, blank=True)
    business_id = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Users(models.Model):
    yelping_since = models.CharField(max_length=7, blank=True)
    votes = models.CharField(max_length=100, blank=True)
    review_count = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True)
    user_id = models.CharField(primary_key=True, max_length=40)
    fans = models.CharField(max_length=300, blank=True)
    average_stars = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    item_type = models.CharField(max_length=4, blank=True)
    compliments = models.CharField(max_length=200, blank=True)
    elite = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'users'
