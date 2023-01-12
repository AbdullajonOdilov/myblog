
from django.contrib import admin
from django.urls import path
from app2.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    # path('blog/', blog),
    path('about/', about),
    # path('channel/', channel),
    path('intervyu/', meeting),
    path('maqola/<int:son>/', maqola),
    path('date/<int:num>/', intervyu)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
