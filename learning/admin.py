from django.contrib import admin
from learning.models import Product


class ProductAdmin(admin.ModelAdmin):
    #fields = ('name', 'content',)
    #readonly_fields = ('content', )
    #fields = (('name', 'content'), ('price', 'stock_count', 'author', 'active'))

    fieldsets = (
        ('Zorunlu', {
            'fields': ('name', 'content')
        }),
        ('Opsiyonel', {
            'fields': ('price', 'stock_count'),
            'classes': ('collapse',)
        })
    )
    exclude = ('slug', )
    list_display = ('name', 'created', 'author')
    list_filter = ('created', 'author')

# Register your models here.
admin.site.site_header = 'STOK YÖNETİM PANELİ'
admin.site.site_title = 'bir stok yönetimi'
admin.site.index_title = 'Stok Yönetimi'
admin.site.register(Product, ProductAdmin)