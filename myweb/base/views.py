from django.shortcuts import render
from django.http import HttpResponse
from .models import Pict

# Create your views here.
def home(request):
    pictures=Pict.objects.all()
    # for picture in pictures:
    #     print(picture)

    context={"pictures": pictures}

    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')





