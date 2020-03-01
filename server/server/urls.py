
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static, serve
from django.conf import settings
import disorders.api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/disorders', disorders.api_views.DisorderList.as_view()),
    path('api/v1/symptoms', disorders.api_views.SymptomsList.as_view()),
    re_path(r'^(?P<path>.*)', serve, {'document_root': settings.FRONTEND_ROOT})

]
