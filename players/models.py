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


class Comments(models.Model):
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    player = models.ForeignKey(Player, verbose_name="Игрок", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.player}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
