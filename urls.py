from downloader import path
from .import views

urlpatterns = [
    path('', views.download_files),
]