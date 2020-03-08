
from . import views
import disorders.query_symptoms
import disorders.api_views
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/api/v1/disorder', disorders.api_views.Disorder.as_view()),
    path('server/api/v1/symptom', disorders.api_views.Symptom.as_view()),
    path('server/api/v1/search', disorders.query_symptoms.Search.as_view()),
    re_path(r'', views.catchall)
]
urlpatterns += staticfiles_urlpatterns()
