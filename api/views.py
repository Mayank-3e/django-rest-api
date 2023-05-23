from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def studentDetail(req,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    return JsonResponse(serializer.data)

def studentList(req):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def studentCreate(req):
    jsondata=req.body
    stream=io.BytesIO(jsondata)
    pydata=JSONParser().parse(stream)
    if req.method=='POST':
        serializer=StudentSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            res={'msg': 'Data created'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    if req.method=='PUT':
        id=pydata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg': 'Data updated'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)