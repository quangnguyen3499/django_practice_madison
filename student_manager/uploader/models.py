from django.db import models

# Create your models here.
class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    @property
    def image_url(self):
        return self.file.url
