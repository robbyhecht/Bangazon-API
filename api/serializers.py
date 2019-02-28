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
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'address', 'phone_number', 'url')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """translates products to json"""

    class Meta:
        """like a form -- point at a model and tell it what fields you want to use"""

        model = Product
        fields = ('id', 'customer','name', 'description', 'price', 'quantity','product_type', 'url')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """translates orders to json"""

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get('_include')

        if include:
            if 'products' in include:
                self.fields['product'] = ProductSerializer(many=True, read_only=True)

            if 'customers' in include:
                self.fields['customer'] = CustomerSerializer(read_only=True, context=self.context)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_id', 'payment_type', 'payment_type_id', 'product', 'url')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """translates producttypes to json"""

    class Meta:
      model = ProductType
      fields = ('id', 'name', 'url')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """translates payment_type to json"""

    class Meta:
        model = PaymentType
        fields = ('id', 'payment_name', 'account_number', 'customer', 'url')

class TrainingProgramSerializer(serializers.HyperlinkedModelSerializer):
    """translates training_program to json"""

    class Meta:
        model = Training_Program
        fields = ('id', 'program_name', 'program_desc', 'start_date', 'end_date', 'max_attendees','employee', 'url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """translates departments to json"""

    def __init__(self, *args, **kwargs):
        super(DepartmentSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get('_include')

        if include:
            if 'employees' in include:
                self.fields['employees'] = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'department_name', 'budget', 'url')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    """translates computers to json"""

    class Meta:
        model = Computer
        fields = ('id', 'purchase_date', 'decommission_date', 'manufacturer', 'model', 'employee', 'is_available', 'url')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """translates employees to json"""

    computer = ComputerSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'start_date', 'end_date', 'department', 'computer', 'is_supervisor', 'url')