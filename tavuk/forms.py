from django import forms  

class tavuk_olcum_form(forms.Form):
    gun_sayisi = forms.IntegerField(label='Gün Sayısı', min_value=1)
    top_tav_say = forms.IntegerField(label='Toplam Tavuk Sayısı', min_value=1)
    max_agrlk = forms.FloatField(label='Maksimum Ağırlık', min_value=0)
