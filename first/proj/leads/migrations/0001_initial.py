# Generated by Django 4.1.5 on 2023-01-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(1, 'Новый'), (2, 'В работе'), (3, 'Приостановлен'), (4, 'Завершен')], default='JANUARY')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
            ],
        ),
    ]