from time import strftime
from django.shortcuts import render,redirect
from numpy import True_
from . import models
from datetime import date, timedelta, datetime

# Create your views here.

def pelanggan(request):

    allpelangganobj = models.pelanggan.objects.all()
    return render(request, 'pelanggan.html',{
        'allpelangganobj' : allpelangganobj,
    })


def createdata(request):
    if request.method == "POST":
        nama = request.POST['nama']
        jeniskelamin = request.POST['jeniskelamin']
        tanggallahir = request.POST['tanggallahir']
        nohp = request.POST['nohp']
        emailplg = request.POST['emailplg']
        alamat = request.POST['alamat']

        newpelanggan = models.pelanggan(
            nama = nama,
            jeniskelamin = jeniskelamin,
            tanggallahir = tanggallahir,
            nohp = nohp,
            emailplg = emailplg,
            alamat = alamat,
        ).save()

        return redirect ('pelanggan')
    
    return render(request, 'createdata.html')

def updatedata(request, id):
    pelangganobj = models.pelanggan.objects.get(ID_pelanggan = id)
    if request.method == "GET":
        tanggallahir = datetime.strftime(pelangganobj.tanggallahir, '%y-%m-%d')
        return render(request,'updatedata.html',{
            'pelangganobj':pelangganobj,
            'tanggallahir' :tanggallahir
        })
    elif request.method == 'POST':
        nama = request.POST['nama']
        jeniskelamin = request.POST['jeniskelamin']
        tanggallahir = request.POST['tanggallahir']
        nohp = request.POST['nohp']
        emailplg = request.POST['emailplg']
        alamat = request.POST['alamat']
        pelangganobj.nama = nama
        pelangganobj.jeniskelamin = jeniskelamin
        pelangganobj.tanggallahir = tanggallahir
        pelangganobj.nohp = nohp
        pelangganobj.emailplg = emailplg
        pelangganobj.alamat = alamat
        pelangganobj.save()

        return redirect ('pelanggan')

def deletedata(request, id):
    pelangganobj = models.pelanggan.objects.get(ID_pelanggan = id)
    pelangganobj.delete()
    return redirect('pelanggan')


def resepsionis(request):
    allresepsionisobj = models.resepsionis.objects.all()

    return render(request, 'resepsionis.html',{
        'allresepsionisobj' : allresepsionisobj,
    })

def jeniskamar(request):
    alljeniskamarobj = models.jeniskamar.objects.all()

    return render(request, 'jeniskamar.html',{
        'alljeniskamarobj' : alljeniskamarobj,
    })

def kamar(request):
    allkamarobj = models.kamar.objects.all()

    return render(request, 'kamar.html',{
        'allkamarobj' : allkamarobj,
    })

def pemesanan(request):
    allpemesananobj = models.pemesanan.objects.all()
    return render(request, 'pemesanan.html',{
        'allpemesananobj' : allpemesananobj,
    })

def createpemesanan(request):
    if request.method == "GET":
        allpelangganobj = models.pelanggan.objects.all
        allresepsionisobj = models.resepsionis.objects.all
        allakamarobj = models.kamar.objects.filter(statuskamar=True)
        return render(request,'createpemesanan.html',{
            'dataresepsionis' : allresepsionisobj,'datapelanggan' : allpelangganobj,'datakamar' : allakamarobj})

    if request.method == "POST":
        ID_pelanggan = request.POST['ID_pelanggan']
        allpelangganobj = models.pelanggan.objects.get(ID_pelanggan = ID_pelanggan)

        ID_resepsionis = request.POST['ID_resepsionis']
        allresepsionisobj = models.resepsionis.objects.get(ID_resepsionis = ID_resepsionis)

        ID_kamar = request.POST['ID_kamar']
        allakamarobj = models.kamar.objects.get(ID_kamar = ID_kamar)
        allakamarobj.statuskamar = False
        allakamarobj.save()
        
        CheckIn = request.POST['CheckIn']
        CheckOut = request.POST['CheckOut']

        LamaMenginap = (datetime.strptime(CheckOut, '%Y-%m-%d') - datetime.strptime(CheckIn, '%Y-%m-%d')).days
        

        newpemesanan = models.pemesanan(
            ID_pelanggan =  allpelangganobj,
            ID_resepsionis = allresepsionisobj,
            ID_kamar = allakamarobj,
            CheckIn = CheckIn,
            CheckOut = CheckOut,
            LamaMenginap = LamaMenginap
        ).save()

        return redirect ('pemesanan')
    
    return render(request, 'createpemesanan.html')

def checkout(request,id):
    pemesananobj = models.pemesanan.objects.get(KodeBooking = id)
    kamarobj = models.kamar.objects.get(ID_kamar = pemesananobj.ID_kamar.ID_kamar)
    kamarobj.statuskamar = True
    kamarobj.save()
    pemesananobj.delete()
    return redirect('pemesanan')

def createpembayaran(request, id):
    allpemesananobj = models.pemesanan.objects.get(KodeBooking = id)
    if request.method == "GET":
        return render(request,'createpembayaran.html',{
            "datapemesanan" : allpemesananobj})

    elif request.method == "POST":
        KodeBooking = request.POST['KodeBooking']
        allpemesananobj = models.pemesanan.objects.get(KodeBooking = KodeBooking)

        MetodePembayaran = request.POST['MetodePembayaran']
        TanggalPembayaran = request.POST['TanggalPembayaran']

        newpembayaran = models.pembayaran(
            KodeBooking = allpemesananobj,
            MetodePembayaran = MetodePembayaran,
            TanggalPembayaran = TanggalPembayaran
        ).save()

        return redirect ('pembayaran')
    
    return render(request, 'createpembayaran.html')

def pembayaran(request):
    allpembayaranobj = models.pembayaran.objects.all()
    return render(request, 'pembayaran.html',{
        'allpembayaranobj' : allpembayaranobj,
    })

def nota(request,id):
    pembayaranobj = models.pembayaran.objects.get(ID_Pembayaran = id)
    pemesananobj = models.pemesanan.objects.get(LamaMenginap = id)
    pelangganobj = models.pelanggan.objects.all()
    jeniskamarobj = models.jeniskamar.objects.get(HargaKamar = id)
    hargatotal = int(pemesananobj.LamaMenginap)*int(jeniskamarobj.HargaKamar)
    return render(request, 'nota.html',{
        'pelangganobj' : pelangganobj,
        'pemesananobj' : pemesananobj,
        'pembayaranobj' : pembayaranobj,
        'jeniskamarobj' : jeniskamarobj,
        'hargatotal' : hargatotal
    })