from django.db import models

class Sales_info(models.Model):
    TransactionDate = models.DateTimeField(auto_now_add=True, null=True)
    CustomerName = models.CharField(max_length = 200, null=True)
    Product = models.CharField(max_length = 200, null=True)
    Quantity = models.FloatField(max_length = 50, null=True)
    TotalAmount = models.FloatField(max_length = 50, null=True)
    
    def __str__(self):
      return self.CustomerName
