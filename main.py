import os
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class SakaApp(App):
    def build(self):
        self.layout = FloatLayout()
        self.sound = None
        
        # Giriş Ekranı Başlığı
        lbl = Label(text="HANGİSİNİN SINAV CEVAPLARINI İSTERSİN?", 
                    font_size='18sp', bold=True, color=(1,0,0,1),
                    pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.layout.add_widget(lbl)

        # Hilal Butonu (Resimli) - Dosya yolunu direkt yazdık
        btn_h = Button(background_normal='kadin.png', size_hint=(.4, .3),
                       pos_hint={'center_x': 0.3, 'center_y': 0.6})
        btn_h.bind(on_press=lambda x: self.kaosu_baslat('kadin.png'))
        self.layout.add_widget(btn_h)

        # Nuri Butonu (Resimli)
        btn_n = Button(background_normal='adam.png', size_hint=(.4, .3),
                       pos_hint={'center_x': 0.7, 'center_y': 0.6})
        btn_n.bind(on_press=lambda x: self.kaosu_baslat('adam.png'))
        self.layout.add_widget(btn_n)

        return self.layout

    def kaosu_baslat(self, resim_yolu):
        # Müziği başlat
        self.sound = SoundLoader.load('muzik.wav')
        if self.sound:
            self.sound.loop = True
            self.sound.play()
        
        self.layout.clear_widgets()
        
        # Ekrana 20 tane resim yağdır
        for _ in range(25):
            img = Image(source=resim_yolu, size_hint=(0.3, 0.3),
                        pos_hint={'x': random.random()*0.7, 'y': random.random()*0.7})
            self.layout.add_widget(img)

        # Şifre kutusunu açmak için görünmez ekran butonu
        tetikleyici = Button(background_color=(0,0,0,0), size_hint=(1, 1))
        tetikleyici.bind(on_press=self.sifre_ekrani)
        self.layout.add_widget(tetikleyici)

    def sifre_ekrani(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='SİSTEM KİLİTLENDİ!\nERİŞİM KODUNU GİRİN:', 
                                halign='center', font_size='15sp'))
        self.sifre_input = TextInput(multiline=False, password=True, size_hint_y=None, height='40dp')
        content.add_widget(self.sifre_input)
        btn = Button(text='SİSTEMİ GERİ YÜKLE', size_hint_y=None, height='50dp')
        content.add_widget(btn)
        self.popup = Popup(title='KRİTİK HATA!', content=content, size_hint=(0.8, 0.4), auto_dismiss=False)
        btn.bind(on_press=self.sifre_kontrol)
        self.popup.open()

    def sifre_kontrol(self, instance):
        if self.sifre_input.text == "etap+pardus!":
            if self.sound: self.sound.stop()
            os._exit(0)
        else:
            self.sifre_input.text = "" # Yanlış şifre girerse kutuyu temizle

if __name__ == '__main__':
    SakaApp().run()
