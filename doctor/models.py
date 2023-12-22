from django.db import models
import uuid

# Create your models here.
class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    yoe = models.IntegerField()
    
    class Meta:
        db_table = 'doctor'
        
    def __str__(self):
        return f"{self.name} ({self.specialization})"