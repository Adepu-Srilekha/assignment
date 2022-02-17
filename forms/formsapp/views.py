from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactFarm,SnippetForm

# Create your views here.
def contact(request):
    if request.method=='POST':
        form=ContactFarm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']

            print(name)


    form=ContactFarm()
    return render(request,'form.html',{'form':form})

def Snippet_detail(request):
    if request.method=='POST':
        form=SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    form=SnippetForm()
    return render(request,'form.html',{'form':form})
