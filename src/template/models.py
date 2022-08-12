from venv import create
from django.db import models
from src.style.models import Style
# Create your models here.
class Templates(models.Model):

    TYPE = (
        ('0', 'HOLIZONTAL'),
        ('1', 'VERTICAL'),
        ('2','SQUARE')
    )
     
    created = models.DateTimeField(auto_now_add=True)
    name_template = models.CharField(max_length=255, blank=True, null=False)
    updated =  models.DateTimeField(auto_now=True)
    type_template = models.CharField(max_length=255, choices=TYPE, default='0')
    style = models.ForeignKey(Style, related_name="templates", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Templates Boards"

    def __str__(self):
        return self.name_template