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
from api.models import Training_Program
from api.models import Department

from api.serializers import ComputerSerializer
from api.serializers import CustomerSerializer
from api.serializers import EmployeeSerializer
from api.serializers import OrderSerializer
from api.serializers import PaymentTypeSerializer
from api.serializers import ProductSerializer
from api.serializers import ProductTypeSerializer
from api.serializers import TrainingProgramSerializer
from api.serializers import DepartmentSerializer

from django.utils import timezone
from datetime import datetime, date

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
        'training_programs': reverse('training_programs', request=request, format=format),
    })


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name', 'username', 'email', 'address', 'phone_number')

    def get_queryset(self):
        query_set = Customer.objects.all()
        keyword = self.request.query_params.get('active', None)

        if keyword is not None:
          keyword = keyword.lower()
          if keyword == 'true':
            query_set = query_set.filter(orders__customer_id__isnull = False)
            return query_set

          if keyword == 'false':
            query_set = query_set.filter(orders__customer_id__isnull = True)
            return query_set

          return query_set

        else:
          print("query params", keyword)

        return query_set

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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # if order includes customers or payment types, ?_include= should be able to nest detail views of those properties within the order table
    filter_backends = (filters.SearchFilter, )
    search_fields = ('customer', 'payment_type', 'product')

    # logic: if order has a payment type, completed then equals true
    def get_queryset(self):
        query_set = Order.objects.all()
        keyword = self.request.query_params.get('completed', None)
        if keyword is not None:
          keyword = keyword.lower()
          if keyword == 'false':
              query_set = query_set.filter(payment_type__isnull = True)
          elif keyword == 'true':
              query_set = query_set.filter(payment_type__isnull = False)
          else:
              pass
        return query_set

class TrainingProgramViewSet(viewsets.ModelViewSet):
    queryset = Training_Program.objects.all()
    serializer_class = TrainingProgramSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('program_name', 'start_date')
    now = timezone.now()

    def get_queryset(self):
        queryset = Training_Program.objects.all()
        # set the query param on the left to 'completed'
        keyword = self.request.query_params.get('completed', None)

        # this is saying you can either query or not
        if keyword is not None:
            keyword = keyword.lower()
            # if 'false' or 'False' is on right side of query param do the following
            if keyword == "false":
                # filter the queryset so that start_date is >= today
                queryset = Training_Program.objects.filter(start_date__gte=self.now)
            # now looking for true on the right side of query
            elif keyword == "true":
                # filter to trainings with a start date in the past
                queryset = Training_Program.objects.filter(end_date__lte=self.now)
        return queryset

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('department_name', 'budget')

    def get_queryset(self):
        query_set = Department.objects.all()

        keyword = self.request.query_params.get('_filter')
        if keyword == 'budget':
            keyword = keyword.lower()

            keyword = self.request.query_params.get('_gt')
            if keyword is not None:
                keyword = keyword.lower()
                query_set = query_set.filter(budget__gte=keyword)

        return query_set

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
