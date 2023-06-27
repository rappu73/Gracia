
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.index),
    path('complex', views.complex),
    path('contact', views.contact),
    path('apparat', views.apparat),
    path('massaje', views.massaje),
    path('sales', views.sales),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
