from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status

# Create your views here.

class UserView(APIView):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many = True)
        return Response({"msg":serializer.data})
    
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":serializer.data})
        return Response({"msg":"eror"})
    
class UserViewP(APIView):
    def get(self,request,pk):
        student = Student.objects.filter(pk=pk).first()
        serializer = StudentSerializer(student)
        return Response({"msg":serializer.data})
    
    def put(self,request,pk):
        student = Student.objects.filter(id=pk).first()
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_200_OK)
        return Response({'msg':'some problrm occured'})
    
    def delete(self,request,pk):
        student = Student.objects.filter(id=pk).first()
        if student:
            student.delete()
            return Response({'msg':'deleted successfully'},status=status.HTTP_200_OK)
        return Response({'msg':'some error occured'})
    