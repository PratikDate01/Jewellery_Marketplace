import os
import sys
import django

# Add backend to sys.path
sys.path.append(os.path.abspath('backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from accounts.models import User
from suppliers.models import Supplier

print(f"Users with role SUPPLIER: {User.objects.filter(role='SUPPLIER').count()}")
print(f"Supplier profiles: {Supplier.objects.count()}")
