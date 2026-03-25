import os
import sys
import django

# Add backend to sys.path
sys.path.append(os.path.abspath('backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from products.models import Product
from categories.models import Category

print(f"Products: {Product.objects.count()}")
print(f"Categories: {Category.objects.count()}")
print(f"Approved Products: {Product.objects.filter(is_approved=True).count()}")
print(f"Available Products: {Product.objects.filter(is_available_for_sale=True).count()}")
print(f"Products with stock: {Product.objects.filter(stock_quantity__gt=0).count()}")
