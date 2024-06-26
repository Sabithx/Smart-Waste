# Generated by Django 4.2.7 on 2024-03-10 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('building_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=100)),
                ('Acname', models.CharField(max_length=100)),
                ('expiredate', models.CharField(max_length=100)),
                ('Cvv', models.CharField(max_length=100)),
                ('Balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_notification', models.CharField(max_length=30)),
                ('update_notification', models.CharField(max_length=30)),
                ('product_notification', models.CharField(max_length=30)),
                ('delivery_notification', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('gender', models.CharField(default='', max_length=10)),
                ('phone_no', models.IntegerField()),
                ('house_name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('Email', models.CharField(max_length=30)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Waste_type', models.CharField(max_length=30)),
                ('Quantity', models.IntegerField()),
                ('Rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('photo', models.CharField(default=0, max_length=250)),
                ('CATEGORY', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='myapp.workercategory')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Waste_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Narration', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=15)),
                ('Date', models.DateField()),
                ('qty', models.IntegerField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('WASTE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.waste')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=15)),
                ('Date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('WASTE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.waste')),
            ],
        ),
        migrations.CreateModel(
            name='Recycle_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('building_no', models.CharField(max_length=30)),
                ('license_no', models.CharField(max_length=30)),
                ('manager', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Recycle_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('WORKER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=30)),
                ('Rate', models.IntegerField()),
                ('RECYCLEUNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recycle_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=30)),
                ('vehicle_no', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('Email', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=15)),
                ('LOGIN', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Order_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('feedback', models.CharField(max_length=30)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_center', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('RECYCLE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recycle_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=15)),
                ('reply', models.CharField(max_length=200)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Area_Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AREA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.area')),
                ('WORKER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.worker')),
            ],
        ),
    ]
