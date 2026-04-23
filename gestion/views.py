from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

def prod_list(request):
    produit = Person.objects.all()
    prodis = Person.objects.all()[1:2]
    return render(request, 'gestion/prod_list.html', {'produit': produit, 'prodis': prodis})

def prod_detail(request, pk):
    prodat = get_object_or_404(Person, pk=pk)
    return render(request, 'gestion/prod_detail.html', {'prodat':prodat})

def prod_tablePlus(request):
    prodas = Person.objects.all().order_by('name')
    prod = Person.objects.all()[1:2]
    return render(request, 'gestion/tableplus.html', {'prodas':prodas, 'prod':prod})

def prod_new(request):
    
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            
            return redirect('prod_list')
            
    else:
        form = PersonForm()
    return render(request, 'gestion/prod_edit.html', {'form':form})

def prod_edit(request, pk):
    prod = get_object_or_404(Person, pk=pk)
    if request.method== "POST":
        form = PersonForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('prod_detail', pk=prod.pk)
    else:
        form = PersonForm(instance=prod)
    return render(request, 'gestion/prod_edit.html', {'form':form})

def prod_supprim(request, pk):
    prod = get_object_or_404(Person, pk=pk)
    if request.method== "POST":
        prod.delete()
        return redirect('prod_list')
    return render(request, 'gestion/prod_edit.html', {'prod': prod})
    
    
        
    

