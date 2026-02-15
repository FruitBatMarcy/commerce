from datetime import date
import django
from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    pass

class Listing(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    imgURL = models.CharField(max_length=256, default="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHNoZGl1azZ0dm9razJxbnBjNnd3bXc5Y2V2cmxvajl0bHkyYTV1cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/v6aOjy0Qo1fIA/giphy.gif")
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")    
    activeUntil = models.DateTimeField(max_length=20, blank=True, default=django.utils.timezone.now)
    CATEGORY_CHOICES=[
        ("tech", "Technology"),
        ("fay", "gay"),
        ("duck", "duck"),
        ("none", "none"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="none")

    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBets")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="betsOnListing")
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Bid {self.id}"