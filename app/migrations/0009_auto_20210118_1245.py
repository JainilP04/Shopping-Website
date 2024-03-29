

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210117_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='cart',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
