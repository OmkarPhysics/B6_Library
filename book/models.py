from django.db import models

# Create your models here.

class ActiveBooksManager(models.Manager):
    def get_queryset(self):
        return super(ActiveBooksManager, self).get_queryset().filter(is_active="y")


class InactiveBooksManager(models.Manager):
    def get_queryset(self):
        return super(InactiveBooksManager, self).get_queryset().filter(is_active="n")




class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.CharField(max_length=1, default="y")

    active_obj = ActiveBooksManager()
    inactive_obj = InactiveBooksManager()
    objects = models.Manager()     

    class Meta:
        db_table = "books"

    def __str__(self):
        return f"{self.name}" 


   
class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  


    class Meta:
        db_table = "emp"

    def __str__(self):
        return f"{self.first_name}" 