from rest_framework import serializers
from api.models import Computer
from api.models import Customer
from api.models import Employee
from api.models import Order
from api.models import Product
from api.models import ProductType
from api.models import PaymentType
from api.models import Training_Program
from api.models import Department



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """translates employees to json"""

    class Meta:
        model = Employee
        fields = ('url', 'first_name', 'last_name', 'start_date', 'end_date', 'department', 'is_supervisor')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """translates orders to json"""

    class Meta:
      model = Order
      fields = ('customer', 'payment_type', 'product')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """translates products to json"""

    class Meta:
        """like a form -- point at a model and tell it what fields you want to use"""

        model = Product
        fields = ('id','customer','name', 'description', 'price', 'quantity','product_type','url')


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """translates producttypes to json"""

    class Meta:
      model = ProductType
      fields = ('name',)

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """translates payment_type to json"""

    class Meta:
        model = PaymentType
        fields = ('url', 'payment_name', 'account_number', 'customer')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """translates customers to json"""

    def __init__(self, *args, **kwargs):
      super(CustomerSerializer, self).__init__(*args, **kwargs)
      request = kwargs['context']['request']
      include = request.query_params.get('_include')

      if include:
        if 'products' in include:
            self.fields['products'] = ProductSerializer(many=True, read_only=True)

        if 'payments' in include:
            self.fields['payment_types'] = PaymentTypeSerializer(read_only=True, many=True)


    class Meta:
        model = Customer
        fields = ('url', 'first_name', 'last_name', 'username', 'email', 'address', 'phone_number')

class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    """translates training_program to json"""

    class Meta:
        model = Training_Program
        fields = ('id','program_name', 'program_desc', 'start_date', 'end_date', 'max_attendees','employee','url')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """translates computers to json"""

    class Meta:
        model = Computer
        fields = ('purchase_date', 'decommission_date', 'manufacturer', 'model', 'is_available', 'employee', 'url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """translates departments to json"""

    class Meta:
        model = Department
        fields = ('url', 'department_name', 'budget')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """translates employees to json"""

    class Meta:
        model = Employee
        fields = ('url', 'first_name', 'last_name', 'start_date', 'end_date', 'department', 'is_supervisor')
