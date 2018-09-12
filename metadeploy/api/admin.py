from django.contrib import admin

from .models import (
    Product,
    ProductSlug,
    Version,
    Plan,
)


admin.site.register(Product)
admin.site.register(ProductSlug)
admin.site.register(Version)
admin.site.register(Plan)
