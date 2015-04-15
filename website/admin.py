from django.contrib import admin
from website import models as website_models
from django.db.models.base import ModelBase
# Register your models here.

for name, var in website_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)