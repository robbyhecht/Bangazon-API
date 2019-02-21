from rest_framework import serializers
from api.models import Customer
from api.models import Product
from api.models import ProductType


from api.models import PaymentType

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """translates customers to json"""

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'phone_number')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    '''translates products to json
    '''

    
    class Meta:
        '''like a form -- point at a model and tell it what fields you want to use
        '''

        model = Product
        fields = ('customer','name', 'description', 'price', 'quantity','product_type')
class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """translates payment_type to json"""

    class Meta:
        model = PaymentType
        fields = ('payment_name', 'account_number', 'customer')
