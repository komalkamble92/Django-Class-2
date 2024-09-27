# Generated by Django 5.1 on 2024-09-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('students', models.ManyToManyField(related_name='courses', to='appname.student')),
            ],
        ),
    ]
