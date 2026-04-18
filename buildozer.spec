[app]

# (str) Uygulama Başlığı
title = Sinav Sistemi

# (str) Paket Adı
package.name = saka.sistemi

# (str) Paket Alan Adı
package.domain = org.test

# (str) Kodun bulunduğu dizin
source.dir = .

# (list) Dahil edilecek dosyalar (Burası kritik!)
source.include_exts = py,png,jpg,wav

# (list) Gerekli kütüphaneler
requirements = python3,kivy,pillow

# (str) Versiyon
version = 1.0

# (str) Ekran yönü
orientation = portrait

# (bool) Tam ekran modu (Kaçışı zorlaştırır)
fullscreen = 1

# (list) Android İzinleri
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Android API seviyesi
android.api = 31

# (int) Minimum Android desteği
android.minapi = 21

# (list) İşlemci mimarileri
android.archs = arm64-v8a, armeabi-v7a

# (bool) Yedekleme izni
android.allow_backup = True

[buildozer]

# (int) Log seviyesi (Hata ayıklama için 2 iyidir)
log_level = 2

# (int) Root uyarısı
warn_on_root = 1