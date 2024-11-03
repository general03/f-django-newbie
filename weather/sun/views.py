import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from sun.models import Sun

# def suns(request):
#     data = []
#     for row in Sun.objects.all():
#         data.append(row.id)

#     return JsonResponse(data={"content": data})


def suns(request):
    data = Sun.objects.all()
    return render(request, "sun.html", {"data": data})

