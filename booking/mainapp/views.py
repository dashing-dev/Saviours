from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , HttpResponse
from .decorators import admin_only
from .models import Input
from .forms import InputForm


# Create your views here.
def index(request):
    return render (request , 'index.html')


def create_view(request):
    context ={}
 
    # add the dictionary during initialization
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request , 'list_view.html')
         
    context['form']= form
    return render(request, "create_view.html", context)
    

def social(request):
    context ={}
 
    # add the dictionary during initialization
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request , 'list_view.html')
         
    context['form']= form
    return render(request, "social.html", context)


def helpline(request):
    return render(request, 'helpline.html')
    
@admin_only
def update_view(request):
    return render(request, 'update_view.html')



def delete_view(request):
    return render(request, 'delete_view.html')



def adminpage(request):
    data = Input.objects.all()
    return render(request, 'adminpage.html', {'data': data})