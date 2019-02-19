# Setting routes

from django.http import HttpResponse


def johnny(request):
    return HttpResponse("Johnny Cash")

def micheal(request):
    return HttpResponse("Micheal Jackson")

def prince(request):
    return HttpResponse("Prince")

