import email
from email import message
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact

# a function to access the portfolio page
def index(request):
    return render(request, "index.html")

#  a function to send the form to backend
def contact(request):
    if request.method == "POST":
        contact = Contact(name = request.POST.get('name'), email = request.POST.get('email'), subject = request.POST.get('subject'), message = request.POST.get('message'))
        contact.save()

        messages.success(request, "message send successfuly !")
        return HttpResponseRedirect('/')
