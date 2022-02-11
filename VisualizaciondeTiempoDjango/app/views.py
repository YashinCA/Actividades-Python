from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from time import strftime, localtime


def index(request):
    return redirect("/time_display")


def time_display(request):
    context = {
        "fecha": strftime("%b %d, %Y", localtime()),
        "hora": strftime("%H:%M %p", localtime()), }

    return render(request, 'app/index.html', context)
