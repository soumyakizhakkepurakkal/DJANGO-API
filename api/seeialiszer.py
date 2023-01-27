from rest_framework import serializers
from . models import Products

class ProductSerilzer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','item','price']