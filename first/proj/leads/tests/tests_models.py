from django.test import TestCase

from leads.models import Lead


class LeadModelTest(TestCase):

    @classmethod
    def setUp(cls):
        #Создаем тестовый объект Lead
        Lead.objects.create(
            state=1,
            name='Тестовый объект'
        )

    def test_name_label(self):
        #Проверка verbose_name поля name
        lead = Lead.objects.get(id=1)
        field_label = lead._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_name_max_length(self):
        #Проверка максимальной длины поля name
        lead = Lead.objects.get(id=1)
        max_length = lead._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_lead_worked(self):
        #Проверка на изменение статуса 'Новый' -> 'В работе'
        lead = Lead.objects.get(id=1)
        lead.lead_worked()
        self.assertEquals(lead.state, 2)

    def test_lead_paused(self):
        #Проверка на изменение статуса 'В работе' -> 'Приостановлен'
        lead = Lead.objects.get(id=1)
        lead.state = 2
        lead.save()
        lead.lead_paused()
        self.assertEquals(lead.state, 3)

    def test_lead_complete(self):
        #Проверка на изменение статуса 'В работе' -> 'Завершен'
        lead = Lead.objects.get(id=1)
        lead.state = 2
        lead.save()
        lead.lead_complete()
        self.assertEquals(lead.state, 4)

    def test_lead_continue(self):
        #Проверка на изменение статуса 'Приостановлен' -> 'В работе'
        lead = Lead.objects.get(id=1)
        lead.state = 3
        lead.save()
        lead.lead_continue()
        self.assertEquals(lead.state, 2)

    def test_lead_stop_complete(self):
        #Проверка на изменение статуса 'Приостановлен' -> 'Завершен'
        lead = Lead.objects.get(id=1)
        lead.state = 3
        lead.lead_stop_complete()
        self.assertEquals(lead.state, 4)