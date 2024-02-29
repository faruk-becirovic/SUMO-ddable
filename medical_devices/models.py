from django.db import models

class Device(models.Model):
    """Model that represents medical devices"""

    DEVICE_TYPES = [
        ('EKG', 'Electrokardiogram'),
        ('TUZV', 'Terapeutski ultrazvuk'),
        ("DEFI", 'Defibrilator'),
    ]

    md_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    md_model = models.CharField(max_length=20)
    serial_no = models.CharField(max_length=20, unique=True)
    inv_no = models.IntegerField(primary_key=True)
    
