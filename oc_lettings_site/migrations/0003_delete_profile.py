# Generated by Django 5.1.4 on 2024-12-11 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_remove_letting_address_delete_address_delete_letting'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Profile",
                ),
            ],
            # Update the table name to the new app name
            database_operations=[
                migrations.AlterModelTable(
                    name='Profile', table='profiles_profile'
                ),
            ],
        )
    ]
