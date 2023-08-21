from django.db import models
import uuid

class MyCollection(models.Model):
    CriminalName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Criminality = models.CharField(max_length=100, default='')
    CriminalPic = models.FileField(upload_to='uploads/')
    record_id = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.CriminalName
    

