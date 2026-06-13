from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
    SALAT = (
        ("Fajr", "Fajr"),
        ("Dhuhr", "Dhuhr"),
        ("Asr", "Asr"),
        ("Maghrib", "Maghrib"),
        ("Isha", "Isha")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salat = models.CharField(max_length=100, choices=SALAT)
    on_time = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.salat} - {self.date}"