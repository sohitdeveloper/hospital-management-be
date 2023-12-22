from django.db import models
import uuid
# Create your models here.
class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'patient'

    def __str__(self):
        return f"{self.name} ({self.id})"