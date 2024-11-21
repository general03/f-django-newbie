from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from sun.models import Sun

# def suns(request):
#     data = []
#     for row in Sun.objects.all():
#         data.append(row.id)

#     return JsonResponse(data={"content": data})


# def suns(request):
#     data = Sun.objects.all()
#     return render(request, "sun.html", {"data": data})


# def suns(request):
#     """Route with GET parameter"""
#     if request.method == "GET":
#         country_name = request.GET.get("country", "Paris")
#         data = Sun.objects.filter(country=country_name)
#     return render(request, "sun.html", {"data": data})

def suns(request, country):
    """Route with GET parameter structured like API ReST"""
    if request.method == "GET":
        data = Sun.objects.filter(country=country)
    return render(request, "sun.html", {"data": data})

def suns_date(request, date):
    """Route with GET parameter structured like API ReST
    
    >> http://localhost:8000/suns/2024-11-03

    """
    if request.method == "GET":
        data = Sun.objects.filter(hours__date=datetime.strptime(date, '%Y-%m-%d'))
    return render(request, "sun_date.html", {"data": data})

def health_check(request):
    return JsonResponse({"status": "ok"})