from django.shortcuts import render, redirect
from .models import Contact
from .mongodb import collection


def home(request):
    return render(request, 'main/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('home')

    return redirect('home')


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']

        collection.insert_one({
            'name': name,
            'message': message
        })

        return redirect('home')

    return redirect('home')