from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'portfolio'

urlpatterns = [
    path('', views.home),
    path('git', views.git, name="git_projects"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)