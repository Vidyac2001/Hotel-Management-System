from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfReservation', models.DateField(default=django.utils.timezone.now)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.SmallIntegerField()),
                ('numberOfBeds', models.SmallIntegerField()),
                ('roomType', models.CharField(choices=[('King', 'King'), ('Luxury', 'Luxury'), ('Normal', 'Normal'), ('Economic', 'Economic')], max_length=20)),
                ('price', models.FloatField()),
                ('statusStartDate', models.DateField(null=True)),
                ('statusEndDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(default=django.utils.timezone.now)),
                ('servicesType', models.CharField(choices=[('Food', 'Food'), ('Cleaning', 'Cleaning'), ('Technical', 'Technical')], max_length=20)),
                ('price', models.FloatField()),
                ('curBooking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.booking')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.guest')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Dependees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='room.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='roomNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room'),
        ),
    ]
