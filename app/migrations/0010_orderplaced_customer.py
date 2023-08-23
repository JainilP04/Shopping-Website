

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210118_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
            preserve_default=False,
        ),
    ]
