from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('computers', views.ComputerViewSet)
router.register('customers', views.CustomerViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('products', views.ProductViewSet)
router.register('product_type', views.ProductTypeViewSet)
router.register('payment_type', views.PaymentTypeViewSet)
router.register('orders', views.OrderViewSet)
router.register('training_programs', views.TrainingProgramViewSet)
router.register('departments', views.DepartmentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]