from django.shortcuts import render
import random


def tavuk_olcum(gun_sayisi, top_tav_say, max_agrlk):
    toplam_agirlik = 0
    toplam_tavuk_sayisi = 0
    gunluk_agirliklar = []

    for gun in range(1, gun_sayisi + 1):
        gunluk_toplam_agrlk = 0
        olculen_tavuk_sayisi = random.randint(1, top_tav_say)
        agirliklar = []

        for i in range(olculen_tavuk_sayisi):
            agirlik = round(random.uniform(0, max_agrlk), 2)
            agirliklar.append(agirlik)
            gunluk_toplam_agrlk += agirlik

        gunluk_ortalama = gunluk_toplam_agrlk / olculen_tavuk_sayisi if olculen_tavuk_sayisi != 0 else 0
        toplam_agirlik += gunluk_toplam_agrlk
        toplam_tavuk_sayisi += olculen_tavuk_sayisi

        gunluk_agirliklar.append({'gun': gun, 'agirliklar': agirliklar, 'gunluk_ortalama': gunluk_ortalama})
    genel_ortalama = toplam_agirlik / toplam_tavuk_sayisi if toplam_tavuk_sayisi != 0 else 0

    return toplam_agirlik, toplam_tavuk_sayisi, genel_ortalama, gunluk_agirliklar

def tavuk_olcum_view(request):
    from .forms import tavuk_olcum_form
    if request.method == 'POST':
        form = tavuk_olcum_form(request.POST)
        if form.is_valid():
            gun_sayisi = form.cleaned_data['gun_sayisi']
            top_tav_say = form.cleaned_data['top_tav_say']
            max_agrlk = form.cleaned_data['max_agrlk']

            toplam_agirlik, toplam_tavuk_sayisi, genel_ortalama, gunluk_agirliklar = tavuk_olcum(gun_sayisi, top_tav_say, max_agrlk)


            return render(request, 'tavuk/result.html', {
                'toplam_agirlik': toplam_agirlik,
                'toplam_tavuk_sayisi': toplam_tavuk_sayisi,
                'genel_ortalama': genel_ortalama,
                'gunluk_agirliklar': gunluk_agirliklar,
            })

    else:
        form = tavuk_olcum_form()

    return render(request, 'tavuk/form.html', {'form': form})
