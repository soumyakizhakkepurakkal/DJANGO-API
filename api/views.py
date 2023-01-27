from django.shortcuts import render
from . models import Products
from . seeialiszer import ProductSerilzer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def index(request):
  if request.method=='GET':
    prouct=Products.objects.all()
    ser=ProductSerilzer(prouct,many=True)
    return JsonResponse(ser.data,safe=False)
  if request.method=='POST':
    ser=ProductSerilzer(data=request.data)
    if ser.is_valid():
        ser.save()
        return JsonResponse(ser.data,status=201)
@api_view(['GET','POST',"DETETE"])
def details(request, id):
    try:
        Product=Products.objects.get(id=id)
    except Products.DoesNoExist:
        return JsonResponse({'error':'product not found'},status=404)
    if request.method=='GET':
        ser=ProductSerilzer(Product)
        return JsonResponse(ser.data)
    if request.method=='DELETE':
        Product.delete()            
        return JsonResponse({'DELETED':'prouct deleted'},status=204)