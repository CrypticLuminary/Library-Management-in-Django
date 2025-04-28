from django.db import models
from django.conf import settings

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="books", null=True, blank=True)
    book_upload = models.FileField(upload_to="bookFiles")
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    

    def __str__(self):
        return self.title
    
