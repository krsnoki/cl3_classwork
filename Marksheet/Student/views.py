from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Enter_DetailForm
from .models import Enter_Detail

# Create your views here.

def home(request):
	return render(request, 'Student/homepage.html')

def resultpage(request, pk):
    student = Enter_Detail.objects.get(reg=pk)
    context = {'student':student}
    print("Student: ", student.name, "mark: ", student.mark)
    return render(request, 'Student/resultpage.html', context)

def result(request):
    form = Enter_DetailForm()

    if request.method == "POST":
        print("print this --------------------------")
        print("\n\n\nprinting : ", request.POST)
        return redirect("resultpage/" + request.POST.get("reg"))

    context = { 'form':form }
    return render(request, 'Student/result_form.html', context)