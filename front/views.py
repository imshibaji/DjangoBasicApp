from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.

def index(request):
    # return HttpResponse('<h1>Hello From Django</h1>')
    return render(request, 'index.html', {'message': 'Hello From Django'})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if(request.method == 'POST'):
        postData = request.POST
        contact = Contact(
            name=postData.get('name'),
            email= postData.get('email'),
            message=postData.get('message')
        )
        contact.save()

        messages.success(request, 'Thank you for contact with us.')
        return redirect('/contact')

    else:
        return render(request, 'contact.html')