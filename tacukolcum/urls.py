from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from tavuk.views import tavuk_olcum_view
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tavuk_olcum_view, name='anasayfa'),
    path('tavuk/', include('tavuk.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
