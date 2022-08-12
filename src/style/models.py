from dataclasses import field
from django.db import models

# Create your models here.
class Style(models.Model):

    UNITS = (
        ('0', 'PIXELS'),
        ('1', 'PERCENT'),
        ('2','MILLIMETERS'),
        ('3','IMCHES')
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    width_height_units = models.CharField(max_length=255, choices=UNITS, default="0")
    scale= models.FloatField(default=0)
    name = models.CharField(max_length=255, blank=True, default="")
    description = models.TextField(null=True, blank=True)
    opacity= models.IntegerField(default=0),
    color= models.CharField(default="#FFFFFF", max_length=20 ,blank=True, null=True)
    dpi= models.FloatField(default=72.0)
    name_template = models.CharField(max_length=255, blank=True, editable=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Style Boards"
    
    def __str__(self):
        return self.name

    def save(self, *agrs, **kwargs):
        self.name_template = f"{self.name} - {self.created}"
        self.save(*agrs, **kwargs)