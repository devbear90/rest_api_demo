from django.db import models

class LargeDataset(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    sub_category = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    data = models.JSONField(null=True, blank=True, default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    published_date = models.DateTimeField(null=True, blank=True)
    last_purchased_date = models.DateTimeField(null=True, blank=True)

    brand = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    model_number = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    warranty = models.CharField(max_length=50, null=True, blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    supplier_email = models.EmailField(null=True, blank=True)
    
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    color = models.CharField(max_length=30, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    shipping_time = models.IntegerField(null=True, blank=True, help_text="Szállítási idő napokban")
    barcode = models.CharField(max_length=50, unique=True, null=True, blank=True)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    metadata = models.JSONField(null=True, blank=True, default=dict)
    specifications = models.JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return f"{self.name} - {self.category} ({self.status})" if self.name and self.category else "Névtelen bejegyzés"
