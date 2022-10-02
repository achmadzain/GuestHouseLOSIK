from django.db import models

# Create your models here.
class pelanggan(models.Model): 
    ID_pelanggan = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    jeniskelamin = models.CharField(max_length=10)
    tanggallahir = models.DateField()
    nohp = models.IntegerField()
    emailplg = models.EmailField()
    alamat = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nama)

class resepsionis(models.Model):
    ID_resepsionis = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    jeniskelamin = models.CharField(max_length=10)
    nohp = models.IntegerField()
    katasandi = models.CharField(max_length=8)

    def __str__(self):
        return str(self.nama)

class jeniskamar(models.Model):
    ID_jenisKamar = models.CharField(max_length=5, primary_key=True)
    HargaKamar = models.IntegerField()
    DeskripsiKamar = models.CharField(max_length=50)

    def __str__(self):
        return str(self.ID_jenisKamar)
    
class kamar(models.Model):
    ID_kamar = models.AutoField(primary_key=True)
    jeniskamar = models.ForeignKey(jeniskamar, on_delete= models.CASCADE)
    statuskamar = models.BooleanField(default=False)
    nokamar = models.IntegerField(null=True)

    def __str__(self):
        return str(self.jeniskamar)

class pemesanan(models.Model):
    KodeBooking = models.AutoField(primary_key=True)
    ID_pelanggan = models.ForeignKey(pelanggan, on_delete= models.CASCADE)
    ID_resepsionis = models.ForeignKey(resepsionis, on_delete= models.CASCADE)
    ID_kamar = models.ForeignKey(kamar, on_delete= models.CASCADE)
    CheckIn = models.DateField()
    CheckOut = models.DateField()
    LamaMenginap = models.IntegerField(null=True)

    def __str__(self):
        return str(self.KodeBooking)

class pembayaran(models.Model):
    ID_Pembayaran = models.AutoField(primary_key=True)
    KodeBooking = models.ForeignKey(pemesanan, on_delete= models.CASCADE)
    MetodePembayaran = models.CharField(max_length=10)
    TanggalPembayaran = models.DateField()

    def __str__(self):
        return str(self.ID_Pembayaran)