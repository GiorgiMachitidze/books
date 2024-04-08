from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    page_count = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    author_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return self.name
