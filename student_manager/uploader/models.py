from django.db import models
from django.utils import timezone

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    @property
    def image_url(self):
        return self.file.url

class Invoice(models.Model):
    user = models.ForeignKey("users.User", related_name="invoices", on_delete=models.PROTECT)
    invoice_number = models.CharField(max_length=20)
    invoice_amount = models.IntegerField()
    invoice_date = models.DateField()
    updated_at = models.DateTimeField(auto_now_add=timezone.now())
    created_at = models.DateTimeField(auto_now=timezone.now())
