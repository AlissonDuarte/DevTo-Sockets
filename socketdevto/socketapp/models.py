from django.db import models

class Random(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255,blank = True, null = True)

