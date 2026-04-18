[app]
title = Yazili Cevaplari
package.name = yazilisaka
package.domain = org.enes
source.dir = .
source.include_exts = py,png,jpg,mp3,spec
version = 3.0
requirements = python3,kivy

# İKON: Klasörde 'ikon.png' olmalı
icon.filename = %(source.dir)s/ikon.png

orientation = portrait
fullscreen = 1
android.wakelock = True

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
