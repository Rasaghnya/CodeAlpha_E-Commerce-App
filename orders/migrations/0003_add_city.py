from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_order_is_paid_order_payment_method_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="city",
            field=models.CharField(default="", max_length=100),
        ),
    ]
