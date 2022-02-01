from django.shortcuts import render, HttpResponse
from linkedin.models import Contactus
# Create your views here.
def index(requests):
    return render(requests,'index.html')
    # return HttpResponse('This is index page')

def about(requests):
    return HttpResponse('This is About Page')


def contact(requests):
    if requests.method=="POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        phone = requests.POST.get('phone')
        text = requests.POST.get('desc')
        contact = Contactus(name=name,email=email,phone=phone,text=text)
        contact.save()
    return render(requests,'contact.html')
    # return HttpResponse('This is About Page')