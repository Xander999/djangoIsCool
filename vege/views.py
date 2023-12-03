from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def receipes(request):
    if(request.method == 'POST'):
        data = request.POST
        receipeName = data.get('receipeName')
        receipeDescription = data.get('receipeDescription')
        receipeImage = request.FILES.get('receipeImage')
        print(data)
        print('Receipe Name :', receipeName)
        print('Receipe Description :', receipeDescription)
        print('Receipe Image :', receipeImage)
        Receipe.objects.create(
            receipeImage = receipeImage,
            receipeName = receipeName,
            receipeDescription = receipeDescription
        )
        return redirect('receipe')
    querySet = Receipe.objects.all()
    context = {'receipes':querySet}

    return render(request, 'receipes.html', context)

def deleteReceipe(request, id):
    querrySet = Receipe.objects.get(id=id)
    querrySet.delete() 
    return redirect('receipe')
