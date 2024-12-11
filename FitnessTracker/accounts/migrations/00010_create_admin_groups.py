from django.db import migrations


def create_admin_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    # Create or get the groups
    superusers_group, _ = Group.objects.get_or_create(name="Superusers")
    staff_group, _ = Group.objects.get_or_create(name="Staff")

    all_permissions = Permission.objects.all()
    superusers_group.permissions.set(all_permissions)

    # Assign permissions to the Staff group
    staff_permissions = Permission.objects.filter(
        codename__in=[
            "view_appuser",
            "change_workoutcategory", "view_workoutcategory",
            "change_workout", "view_workout",
            "change_profile", "view_profile",
            "change_favouriteworkouts", "view_favouriteworkouts",
            "change_meal", "view_meal",
            "change_progressexercise", "view_progressexercise",
            "change_progresslog", "view_progresslog"
        ]
    )
    staff_group.permissions.set(staff_permissions)


def remove_admin_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name__in=["Superusers", "Staff"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0009_alter_appuser_first_name_alter_appuser_last_name_and_more'),
    ]

    operations = [
        migrations.RunPython(create_admin_groups, reverse_code=remove_admin_groups),
    ]
