from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    COMPLAINT_TYPES = [
        ("Operation Issue", "Operation Issue"),
        ("Customer Care Issue", "Customer Care Issue"),
        ("Marketing Issue", "Marketing Issue"),
        ("Technical Issue", "Technical Issue"),
        ("Bribe Case", "Bribe Case"),
        ("Illegal Activities", "Illegal Activities"),
        ("Other", "Other"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Ongoing", "Ongoing"),
        ("Solved", "Solved"),
        ("Rejected", "Rejected"),
    ]

    date = models.DateField(auto_now_add=True)
    center = models.CharField(max_length=100)
    area_manager = models.CharField(max_length=100)
    area_manager_email = models.EmailField()
    vin = models.CharField("Vehicle Identification Number", max_length=100)
    tele_no = models.CharField("Customer Mobile Number", max_length=20)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_no = models.AutoField(primary_key=True)
    complaint = models.TextField()
    immediate_action = models.TextField()
    correct_action = models.TextField()
    complaint_type = models.CharField(max_length=50, choices=COMPLAINT_TYPES)
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.complaint_no} - {self.vin}"

class ClassChange(models.Model):
    CLASS_CHOICES = [
        ("Motor Cycle", "Motor Cycle"),
        ("Motor Car", "Motor Car"),
        ("Tricycle", "Tricycle"),
        ("Dual Purpose", "Dual Purpose"),
        ("Motor Lorry", "Motor Lorry"),
        ("Motor Coach", "Motor Coach"),
        ("Prime Mover", "Prime Mover"),
        ("Land Vehicle", "Land Vehicle"),
        ("Omni Bus", "Omni Bus"),
    ]

    APPROVED_CHOICES = [
        ("Nuwan", "Nuwan Jayaneththi"),
        ("Rasika", "Rasika Perera"),
        ("Other", "Other"),
    ]

    date = models.DateField()
    time = models.TimeField()
    center = models.CharField("Center", max_length=100)
    vin = models.CharField("Vehicle Identification Number", max_length=100)
    previous_class = models.CharField(max_length=100, choices=CLASS_CHOICES)
    change_class = models.CharField(max_length=50, choices=CLASS_CHOICES)
    reason = models.TextField()
    approved_by = models.CharField(max_length=50, choices=APPROVED_CHOICES)
    refund = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])
    remark = models.TextField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vin} - {self.change_class}"
