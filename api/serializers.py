from rest_framework import serializers
from api.models import Customer
from api.models import Employee
from api.models import PaymentType

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """translates customers to json"""

    class Meta:
        model = Customer
        fields = ('url', 'first_name', 'last_name', 'username', 'email', 'address', 'phone_number')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    '''translates employees to json
    '''

    class Meta:
        model = Employee
        fields = ('url', 'first_name', 'last_name', 'start_date', 'end_date', 'department', 'is_supervisor')
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'phone_number')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """translates payment_type to json"""

    class Meta:
        model = PaymentType
        fields = ('payment_name', 'account_number', 'customer')
