from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

Editors, created = Group.objects.get_or_create(name="Editors")
Viewers, created = Group.objects.get_or_create(name="Viewers")
Admins, created = Group.objects.get_or_create(name="Admins")

# Code to add permission to group.
ct = ContentType.objects.get_for_model(Book)

# Now say I want to add 'Can add project' permission to new_group.
permission1 = Permission.objects.create(
    codename="can_edit", name="Can edit", content_type=ct
)
permission2 = Permission.objects.create(
    codename="can_create", name="Can create", content_type=ct
)
permission3 = Permission.objects.create(
    codename="can_view", name="Can view", content_type=ct
)
permission4 = Permission.objects.create(
    codename="can_delete", name="Can delete", content_type=ct
)

# Adding permissions to groups.
Editors.permissions.add(permission1, permission2)
Viewers.permissions.add(permission3)
Admins.permissions.add(permission4)