from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")
    title = models.TextField(verbose_name="Комментарии")
    photo = models.ImageField(upload_to="player_avatars/%Y/%m/%d")

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"
        ordering = ['last_name']
