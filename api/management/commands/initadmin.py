
from django.conf import settings
from django.core.management.base import BaseCommand
from api.models import CustomUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        if CustomUser.objects.count() == 0:
            email = "admin@admin.com"
            password = 'admin'
            print(f'Creating account for {email}')
            admin = CustomUser.objects.create_superuser(email=email, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')