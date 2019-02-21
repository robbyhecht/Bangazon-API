from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
from api.models import Customer
from api.serializers import CustomerSerializer

from api.models import Employee
from api.serializers import EmployeeSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('customers', request=request, format=format)
    })


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name')

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