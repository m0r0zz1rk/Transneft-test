from django.db import models

STATE_CHOICES = (
        (1, "Новый"),
        (2, "В работе"),
        (3, "Приостановлен"),
        (4, "Завершен"),
    )


class Lead(models.Model):
    state = models.IntegerField(
        choices=STATE_CHOICES,
        default=1
    )
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Имя",
    )

    objects = models.Manager()

    def __str__(self):
        return self.name

    def lead_worked(self):
        """Смена статуса 'Новый' -> 'В работе'"""
        try:
            if self.state != 1:
                return 'Некорректный исходный статус объекта'
            self.state = 2
            self.name = f'{self.name} (В работе)'
            self.save()
            #Некоторая логика
            return 'Статус объета успешно изменен на "В работе"'
        except Exception as e:
            return SystemError(e)

    def lead_paused(self):
        """Смена статуса 'В работе' -> 'Приостановлен'"""
        try:
            if self.state != 2:
                return 'Некорректный исходный статус объекта'
            self.state = 3
            self.name = f'{self.name} (Приостановлен)'
            self.save()
            # Некоторая логика
            return 'Статус объекта успешно изменен на "Приостановлен"'
        except Exception as e:
            return SystemError(e)

    def lead_complete(self):
        """Смена статуса 'В работе' -> 'Завершен'"""
        try:
            if self.state != 2:
                return 'Некорректный исходный статус объекта'
            self.state = 4
            self.name = f'{self.name} (Завершен)'
            self.save()
            # Некоторая логика
            return 'Статус объекта успешно изменен на "Завершен"'
        except Exception as e:
            return SystemError(e)

    def lead_continue(self):
        """Смена статуса 'Приостановлен' -> 'В работе'"""
        try:
            if self.state != 3:
                return 'Некорректный исходный статус объекта'
            self.state = 2
            self.name = f'{self.name} (В работе)'
            self.save()
            # Некоторая логика
            return 'Статус объекта успешно изменен на "В работе"'
        except Exception as e:
            return SystemError(e)

    def lead_stop_complete(self):
        """Смена статуса 'Приостановлен' -> 'Завершен'"""
        try:
            if self.state != 3:
                return 'Некорректный исходный статус объекта'
            self.state = 4
            self.name = f'{self.name} (Завершен)'
            self.save()
            # Некоторая логика
            return 'Статус объекта успешно изменен на "Завершен"'
        except Exception as e:
            return SystemError(e)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
