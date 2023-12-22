from django.db import models
from doctor.models import Doctor
from patient.models import Patient
import uuid
# Create your models here.
class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    
    class Meta:
        db_table = 'appointment'
        
    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} for {self.patient.name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"
