[app]
title = Saka Uygulamasi
package.name = sakaapp
package.domain = org.enes
source.dir = .
source.include_exts = py,png,jpg,mp3,spec
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android Ayarları (Hata almamak için sabitlendi)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.skip_update = False
android.api = 31
android.minapi = 21
android.ndk = 23b
android.log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
