

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='locality',
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='krish', max_length=200),
            preserve_default=False,
        ),
    ]
