from django.db import models
from datetime import datetime, date
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

# -------------
# BANGAZON STORE SECTION
# -------------

# Customer Model
class Customer(SafeDeleteModel):
    """Users - represents both buyers and sellers at Bangazon"""
    _safedelete_policy = SOFT_DELETE_CASCADE

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=20, blank=False)
    address = models.CharField(max_length=100, blank=False)
    phone_number = models.IntegerField(blank=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('last_name',)

# ProductType Model
class ProductType(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        """string method returns producttype name"""
        return self.name

    class Meta:
        ordering = ('name',)

# Product Model
class Product(models.Model):
    """An item that a User can Sell or Buy"""
    # customer in this instance is the product seller
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    quantity = models.IntegerField(blank=False)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, related_name='products')

    def __str__(self):
        """string method that returns the product name"""

        return self.name

    class Meta:
        ordering = ('name',)

# PaymentType Model
class PaymentType(models.Model):
    """A payment type saved by the buyer for use with orders"""
    # customer in this instance is the product buyer
    payment_name = models.CharField(max_length=50, blank=False)
    account_number = models.IntegerField(blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payment_types')

    def __str__(self):
        """string method that returns the payment type name"""

        return self.customer.first_name + self.payment_name
        
    class Meta:
        ordering = ('payment_name',)

# Order Model
class Order(models.Model):
    """An order placed by the buying/logged in user"""
    # customer in this instance is the product buyer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    payment_type = models.ForeignKey(PaymentType, default=None, blank=True, null=True, on_delete=models.PROTECT, related_name='orders')
    product = models.ManyToManyField(Product, through='ProductOrder', related_name='orders')

    def __str__(self):
        """string method that returns the Order id"""

        return str(self.id)

# ProductOrder Model
class ProductOrder(models.Model):
    """A join table linking the product being sold to the order being placed"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_order')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_rder')

    def __str__(self):
        """string method that returns the ProductOrder id"""

        return str(self.id)

# -------------
# BANGAZON ADMIN/HR SECTION
# -------------

# Department Model
class Department(SafeDeleteModel):
    """a grouping of employees"""
    _safedelete_policy = SOFT_DELETE_CASCADE
    department_name = models.CharField(max_length=100)
    budget = models.IntegerField()

    def __str__(self):
        """string method that returns the department name"""

        return self.department_name

    class Meta:
        ordering = ('department_name',)


# Employee Model
class Employee(SafeDeleteModel):
    """a person that works for the company"""
    _safedelete_policy = SOFT_DELETE_CASCADE

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField('Starting Date')
    end_date = models.DateField('Ending Date', default=None, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='employees')
    is_supervisor = models.BooleanField(default=False)

    def __str__(self):
        return_value = (f"{self.first_name} {self.last_name} works in the {self.department} department")
        return return_value
    
    class Meta:
        ordering = ('last_name',)

#Computer Model
class Computer(SafeDeleteModel):
    """A device that is assigned to a company employee"""
    _safedelete_policy = SOFT_DELETE_CASCADE

    purchase_date = models.DateField('Purchase Date')
    decommission_date = models.DateField('Decommission Date', default=None, blank=True, null=True)
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    employee = models.ManyToManyField(Employee, through='Join_Computer_Employee', related_name='computers')

    def __str__(self):
        computer_name = (f"{self.manufacturer} {self.model} - ID#{self.id}")
        return computer_name
    
    class Meta:
        ordering = ('manufacturer', 'model',)

# Join table for Computer & Employee
class Join_Computer_Employee(models.Model):
    """a relationship between computers and employees"""
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, related_name='employee_computers')
    computer = models.ForeignKey('Computer', on_delete=models.PROTECT, related_name='employee_computers')
    assign_date = models.DateField('Assign Date')
    unassign_date = models.DateField('Unassign Date', default=None, blank=True, null=True)

# Training Program Model
class Training_Program(SafeDeleteModel):
    """A program the company offers employees"""
    _safedelete_policy = SOFT_DELETE_CASCADE

    program_name = models.CharField(max_length=100)
    program_desc = models.CharField(max_length=200)
    start_date = models.DateField('Starting Date')
    end_date = models.DateField('Ending Date')
    max_attendees =  models.IntegerField()
    employee = models.ManyToManyField(Employee, through='Join_Training_Employee', related_name='training_programs')

    def __str__(self):
        """returns a training program name"""
        return self.program_name

# Join table for Training Program & Employee
class Join_Training_Employee(models.Model):
    """The join table for employees and training"""
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='employee_trainings')
    training_program = models.ForeignKey(Training_Program, on_delete=models.PROTECT, related_name='employee_trainings')
