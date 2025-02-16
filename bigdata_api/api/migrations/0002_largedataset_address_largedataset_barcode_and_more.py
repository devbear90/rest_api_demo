# Generated by Django 5.1.6 on 2025-02-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='largedataset',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='barcode',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='last_purchased_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='material',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='model_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='serial_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='shipping_time',
            field=models.IntegerField(blank=True, help_text='Szállítási idő napokban', null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='sku',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='specifications',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='sub_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='supplier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='supplier_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='warranty',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largedataset',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='largedataset',
            name='data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='largedataset',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
