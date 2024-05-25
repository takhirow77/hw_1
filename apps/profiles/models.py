from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Биография")
    location = models.CharField(max_length=30, blank=True, verbose_name="Местоположение")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True, verbose_name="Фотография профиля")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
