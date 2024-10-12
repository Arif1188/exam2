from django.db import models

class HeaderModel(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    time = models.DateTimeField(auto_created=True)
    
    def __str__(self) -> str:
        return self.number

class MiddleModel(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    
    
class FooterModel(models.Model):
    text = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.text
    
    
