from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters

from api.models import Computer
from api.models import Customer
from api.models import Employee
from api.models import Order
from api.models import PaymentType
from api.models import Product
from api.models import ProductType
from api.models import Department

from api.serializers import ComputerSerializer
from api.serializers import CustomerSerializer
from api.serializers import EmployeeSerializer
from api.serializers import OrderSerializer
from api.serializers import PaymentTypeSerializer
from api.serializers import ProductSerializer
from api.serializers import ProductTypeSerializer
from api.serializers import DepartmentSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'computers': reverse('computers', request=request, format=format),
        'customers': reverse('customers', request=request, format=format),
        'orders': reverse('orders', request=request, format=format),
        'employees': reverse('employees', request=request, format=format),
        'products': reverse('products', request=request, format=format),
        'departments': reverse('departments', request=request, format=format),
        'payment_types': reverse('payment_types', request=request, format=format),
        'product_types': reverse('product_types', request=request, format=format),
    })


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name')

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('name')

    # use method for includes, will adjust settings/filter above for q
    # issue 1, elif
    # def get_queryset(self):
    #     query_set = Customer.objects.all()
    #     keyword = self.request.query_params.get('_include', None)
    #     if keyword is not None:
    #         print("query params", keyword)
    #         if keyword is 'products':
    #             query_set = query_set.filter(products=keyword)
    #         elif keyword is 'payments':
    #             query_set = query_set.filter(payments=keyword)
    #     return query_set


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name', 'start_date', 'end_date', 'department', 'is_supervisor')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

<<<<<<< HEAD
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
=======
class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
>>>>>>> master

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('department_name', 'budget')
<<<<<<< HEAD
=======

    # use method for includes, will adjust settings/filter above for q
    # issue 1, elif
    # def get_queryset(self):
    #     query_set = Customer.objects.all()
    #     keyword = self.request.query_params.get('_include', None)
    #     if keyword is not None:
    #         print("query params", keyword)
    #         if keyword is 'products':
    #             query_set = query_set.filter(products=keyword)
    #         elif keyword is 'payments':
    #             query_set = query_set.filter(payments=keyword)
    #     return query_set
>>>>>>> master
