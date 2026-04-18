[app]
title = Yazili Cevaplari
package.name = yazilicevaplari
package.domain = org.enes
source.dir = .
source.include_exts = py,png,jpg,mp3,spec
version = 1.0
requirements = python3,kivy

# İKON AYARI (Dosya adın farklıysa 'ikon.png' yazan yeri değiştir)
icon.filename = %(source.dir)s/ikon.png

# Ekran Ayarları
orientation = portrait
fullscreen = 1
android.wakelock = True

# NDK ve SDK Ayarları
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
