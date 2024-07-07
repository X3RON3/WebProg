from django.shortcuts import render
from django.http import JsonResponse
from pandih.models import course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def apiCourse(request):
    if (request.method == "GET"):
        data = serializers.serialize("json", course.objects.all())

        return JsonResponse(json.loads(data), safe=False)
    
    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        if not body:
            data = '{"message": "data is not json type!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        else:
            created= course.objects.create(
                course_name=body['course_name']
            )
            data='{"message"= "data succesfully created!"}'
            dumps= json.dumps(data)
            return JsonResponse(dumps, safe=False)

    if request.method == "PUT":
        body = json.loads(request.body.decode("utf-8"))
        if not body or 'id' not in body:
            data = '{"message": "invalid data or missing ID!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        try:
            course_obj = course.objects.get(id=body['id'])
            course_obj.course_name = body.get('course_name', course_obj.course_name)
            course_obj.save()
            data = '{"message": "data successfully updated!"}'
            dumps = json.dumps(data)
            return JsonResponse(dumps, safe=False)
        except course.DoesNotExist:
            data = '{"message": "course not found!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)

    if request.method == "DELETE":
        body = json.loads(request.body.decode("utf-8"))
        if not body or 'id' not in body:
            data = '{"message": "invalid data or missing ID!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        try:
            course_obj = course.objects.get(id=body['id'])
            course_obj.delete()
            data = '{"message": "data successfully deleted!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        except course.DoesNotExist:
            data = '{"message": "course not found!"}'
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
