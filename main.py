import os
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class SakaApp(App):
    def build(self):
        # GERİ TUŞUNU KİLİTLE
        Window.bind(on_request_close=self.yasak_kardesim)
        
        self.layout = FloatLayout()
        self.sound = None
        
        # Üstteki Soru Yazısı
        lbl = Label(
            text="HANGİ SINAV CEVAPLARINI ALMAK İSTERSİN?", 
            font_size='18sp', bold=True, color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )
        self.layout.add_widget(lbl)

        # Kadın Hoca Resimli Buton
        self.btn_kadin = Button(
            background_normal='kadin.png',
            size_hint=(.4, .35), 
            pos_hint={'center_x': 0.3, 'center_y': 0.5}
        )
        self.btn_kadin.bind(on_press=lambda x: self.kaosu_baslat('kadin.png'))
        self.layout.add_widget(self.btn_kadin)

        # Erkek Hoca Resimli Buton
        self.btn_erkek = Button(
            background_normal='adam.png',
            size_hint=(.4, .35), 
            pos_hint={'center_x': 0.7, 'center_y': 0.5}
        )
        self.btn_erkek.bind(on_press=lambda x: self.kaosu_baslat('adam.png'))
        self.layout.add_widget(self.btn_erkek)

        return self.layout

    def yasak_kardesim(self, *args):
        return True

    def kaosu_baslat(self, resim_yolu):
        self.sound = SoundLoader.load('muzik.mp3')
        if self.sound:
            self.sound.loop = True
            self.sound.play()
        
        self.layout.clear_widgets()
        
        # Ekrana spam resimler atar (50 adet yaptık, tam çöksün)
        for _ in range(50):
            img = Image(source=resim_yolu, size_hint=(0.4, 0.4),
                        pos_hint={'x': random.random()*0.6, 'y': random.random()*0.6})
            self.layout.add_widget(img)

        # Görünmez şifre tetikleyici
        tetikleyici = Button(background_color=(0,0,0,0), size_hint=(1, 1))
        tetikleyici.bind(on_press=self.sifre_ekrani)
        self.layout.add_widget(tetikleyici)

    def sifre_ekrani(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='SİSTEM KİLİTLENDİ!\nŞİFREYİ GİRİN:', halign='center'))
        self.sifre_input = TextInput(multiline=False, password=True, size_hint_y=None, height='40dp')
        content.add_widget(self.sifre_input)
        btn = Button(text='TAMAM', size_hint_y=None, height='50dp')
        btn.bind(on_press=self.sifre_kontrol)
        content.add_widget(btn)
        
        self.popup = Popup(title='ERİŞİM ENGELİ', content=content, size_hint=(0.8, 0.4), auto_dismiss=False)
        self.popup.open()

    def sifre_kontrol(self, instance):
        if self.sifre_input.text == "etap+pardus!":
            if self.sound: self.sound.stop()
            os._exit(0)
        else:
            self.sifre_input.text = ""

if __name__ == '__main__':
    SakaApp().run()
