from django.db import models
from django.forms.fields import ImageField
from django.utils.safestring import mark_safe

class Enter_Detail(models.Model):
    name = models.CharField(max_length=30)
    reg = models.CharField(max_length=30)
    subject = models.CharField(max_length=30, null=True)
    mark = models.PositiveBigIntegerField()
    def __str__(self):
        return self.name

# class Name(models.Model):
#     name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.name   

# class Mark(models.Model):
#     mark = models.PositiveBigIntegerField()
#     def __str__(self):
#         return self.mark