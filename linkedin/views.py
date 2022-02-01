from django.shortcuts import render, HttpResponse

# Create your views here.
def index(requests):
    return render(requests,'index.html')
    # return HttpResponse('This is index page')

def about(requests):
    return HttpResponse('This is About Page')