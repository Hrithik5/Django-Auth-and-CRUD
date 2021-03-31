from django.shortcuts import redirect, render
from django.http import HttpResponse,Http404
from django.contrib import messages
from .models import Information
from .forms import InfoCreate

# Create your views here.
def home(request):
    Dataset = Information.objects.all()
    # print(Dataset)
    return render(request, 'home.html', {'context' : Dataset})

def add(request):
    if request.method == 'POST':
        #  <----  When we create form in HTML we use this method ---->
        fname = request.POST.get('fname')
        lname = request.POST.get('surname')
        number = request.POST.get('contact')
        Data = Information(fname = fname, lname = lname, number = number)
        Data.save()
        
        return redirect('home')

def edit(request, data_id):
    Temp = Information.objects.get(pk=data_id)

    if request.method == 'POST':
        form = InfoCreate(request.POST)
        if form.is_valid():
            Temp.fname = form.cleaned_data.get('fname')
            Temp.lname = form.cleaned_data.get('lname')
            Temp.number = form.cleaned_data.get('number')
            Temp.save()
            return redirect('home')
    
    form = InfoCreate(initial = {'fname' : Temp.fname, 'lname': Temp.lname, 'number':Temp.number})
    return render(request, 'edit.html', {'form': form, 'Data':Temp})

def delete(request, data_id):
    if request.method == 'POST':
        Temp = Information.objects.get(pk=data_id)
        Temp.delete()
    return redirect('home')