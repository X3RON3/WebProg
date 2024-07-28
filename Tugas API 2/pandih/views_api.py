from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def consumeApiGet(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    return render(request, "api-get.html", {'data': data})

@csrf_exempt
def addData(request):
    if request.method == 'POST':
        new_data = json.loads(request.body)
        response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_data)
        
        if response.status_code == 201:
            return JsonResponse({'message': 'Data berhasil ditambah'}, status=201)
        else:
            return JsonResponse({'message': 'Data gagal ditambah'}, status=response.status_code)

@csrf_exempt
def updateData(request, user_id):
    if request.method == 'PUT':
        updated_data = json.loads(request.body)
        response = requests.put(f"https://jsonplaceholder.typicode.com/users/{user_id}", json=updated_data)
        
        if response.status_code == 200:
            return JsonResponse({'message': 'Data berhasil ditambah'}, status=200)
        else:
            return JsonResponse({'message': 'Data gagal ditambah'}, status=response.status_code)

