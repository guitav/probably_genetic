
from . import views
import disorders.query_symptoms
import disorders.api_views
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static, serve
from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf goes here ...


from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/api/v1/disorders', disorders.api_views.DisorderList.as_view()),
    path('server/api/v1/symptoms', disorders.api_views.SymptomsList.as_view()),
    path('server/api/v1/forms', disorders.query_symptoms.QueryList.as_view()),
    re_path(r'', views.catchall)
]
urlpatterns += staticfiles_urlpatterns()
