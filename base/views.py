from django.shortcuts import render
from django.http import HttpResponse

def taskList(requst):
    return HttpResponse("<h2> Hei you accesed the task list!! </h2>")