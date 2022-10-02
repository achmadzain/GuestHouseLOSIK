from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.pelanggan)
admin.site.register(models.resepsionis)
admin.site.register(models.kamar)
admin.site.register(models.jeniskamar)
admin.site.register(models.pemesanan)
admin.site.register(models.pembayaran)