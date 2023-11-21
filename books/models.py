from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", default=None)

    class Meta:
        permissions = [("special_status", "Can read all books")]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.TextField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.review
