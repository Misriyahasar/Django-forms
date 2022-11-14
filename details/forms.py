from django import forms

from .models import *



class StudentForm(forms.ModelForm):
    full_name = forms.CharField(max_length=50, required=True,)
    email = forms.EmailField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    class_name = forms.ChoiceField(choices=CLASSES, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
 
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'age', 'class_name', 'description']