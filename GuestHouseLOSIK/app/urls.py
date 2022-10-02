from django.urls import path
from . import views

urlpatterns = [
    path('pelanggan', views.pelanggan, name='pelanggan'),
    path('createdata', views.createdata, name='createdata'),
    path('resepsionis', views.resepsionis, name='resepsionis'),
    path('jeniskamar', views.jeniskamar, name='jeniskamar'),
    path('kamar', views.kamar, name='kamar'),
    path('pemesanan', views.pemesanan, name='pemesanan'),
    path('createpemesanan', views.createpemesanan, name='createpemesanan'),
    path('checkout/<str:id>',views.checkout ,name='checkout'),
    path('updatedata/<str:id>', views.updatedata, name='updatedata'),
    path('deletedata/<str:id>', views.deletedata, name='deletedata'),
    path('createpembayaran/<str:id>', views.createpembayaran, name='createpembayaran'),
    path('pembayaran', views.pembayaran, name='pembayaran'),
    path('nota/<str:id>', views.nota, name='nota')
]