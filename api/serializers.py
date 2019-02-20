from rest_framework import serializers
from api.models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    '''translates customers to json
    '''

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'phone_number')