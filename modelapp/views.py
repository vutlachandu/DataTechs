from django.shortcuts import render
from modelapp.forms import CourseForm

# Create your views here.
def end_page(request):
    return render(request,"modelapp/end.html")
def add_course(request):
    form = CourseForm()
    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return end_page(request)
    return render(request,"modelapp/add.html",{'form':form})
