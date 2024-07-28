from django.urls import path
from file import views

app_name = 'file'


urlpatterns = [
    path('uploadphoto/', views.UploadFile, name='uploadphoto'),
    # path('list/', views.FileListView.as_view(), name='list'),
    path('<int:pk>/download/', views.FileDownloadView.as_view(), name='download'),
]