from rest_framework import serializers
from api.models import Customer
from api.models import ProductType

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    '''translates customers to json
    '''

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'phone_number')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
      model = ProductType
      fields = ('name',)