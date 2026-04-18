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

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
# İşte hatayı çözen satır:
android.ndk = 25b
android.ndk_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
