from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
 
    else:
        form = StudentForm()
 
    return render(request, 'student_form.html', {'form': form})
