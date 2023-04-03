# Generated by Django 4.1.7 on 2023-04-03 08:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0004_bookinstance_borrower"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookinstance",
            options={
                "ordering": ["due_back"],
                "permissions": (("can mark as returned", "set book as returned"),),
            },
        ),
    ]