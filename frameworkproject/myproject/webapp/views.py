from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import employee
from .serializers import employeeSerializer

class employeeCreateApi(generics.CreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class employeeApi(generics.ListAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class employeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class employeeDeleteApi(generics.DestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer


"""
@api_view(['GET'])

def get(request):
    employee_obj = employee.objects.all()
    serializer = employeeSerializer(employee_obj, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_employee(request):
    serializer = employeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def getdetail(request, id):
    emp_obj = employee.objects.get(id=id)
    serializer = employeeSerializer(emp_obj, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, id):
    emp_obj = employee.objects.get(id=id)
    serializer = employeeSerializer(instance=emp_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    emp_obj = employee.objects.get(id=id)
    emp_obj.delete()
    return redirect(get)
"""



