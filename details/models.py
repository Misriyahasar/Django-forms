from django.db import models
from django import forms

# Create your models here.
CLASSES = (
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth'),
    ('5', 'Fifth'),
    ('6', 'Sixth'),
    ('7', 'Seventh'),
    ('8', 'Eighth'),
    ('9', 'Ninth'),
    ('10', 'Tenth'),
    ('11', 'Eleventh'),
    ('12', 'Twelfth'),
)
class Student(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    class_name = models.CharField(max_length=5, choices=CLASSES)
    description = models.TextField()

    def __str__(self):
        return self.full_name
