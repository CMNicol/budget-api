from django.db import models


# Create your models here.

# Category
# only primary key
class Category(models.Model):
    name = models.TextField(unique=True)


# Sub-category
# foreign key = category
class SubCategory(models.Model):
    name = models.TextField()
    parent_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


# Monthly budget
# foreign key = category
# foreign key = sub-category
class Budget(models.Model):
    description = models.TextField()
    amount = models.FloatField()
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)


# Consumability
# consumable good, non-consumable good, service
class Consumability(models.Model):
    consumability = models.TextField(unique=True)


# Expense
# foreign key = category
# foreign key = sub-category
# foreign key = consumability
class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING)
    date = models.DateField()
    description = models.CharField(max_length=250)
    amount = models.FloatField()
    consumability = models.ForeignKey(Consumability, on_delete=models.DO_NOTHING)


# Income
class Income(models.Model):
    source = models.TextField(unique=True)
    amount = models.FloatField()
