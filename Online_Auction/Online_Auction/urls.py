from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('SellerApp.urls')),
    path('v1/', include('AuctionApp.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
