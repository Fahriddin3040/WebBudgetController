from django.db import models


class User(models.Model):
    f_name = models.CharField(max_length=25, verbose_name='Имя')
    l_name = models.CharField(max_length=25, verbose_name='Фамилия')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        full_name = self.f_name + ' ' + self.l_name
        return full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользоваетли'
        ordering = ['f_name', 'l_name']


class Note(models.Model):
    SORT_CHOICES = [
        (1, 'Expence'),
        (2, 'Income'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    sort = models.IntegerField(choices=SORT_CHOICES, null=False, verbose_name='Вид транзакции')
    reason = models.CharField(max_length=50, null=False, verbose_name='Причина')
    price = models.IntegerField(null=False, verbose_name='Финансовая стоимость')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')

    def __str__(self):
        return 'S'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['id', 'user_id', 'sort', 'reason', 'price', 'date_time']


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, db_index=True)

    def __str__(self):
        return self.name
