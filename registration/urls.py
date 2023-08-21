from django.contrib import admin
from django.urls import path
from registration import views
from django.conf import settings
from django.conf.urls.static import static
from .views import add_record, success, mycollection 
from . import views
import pymongo
from django.conf.urls.static import static


# ,delete_record

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('home/', views.HomePage, name='home'),
    path('Record_Management', views.Record_Management, name='Record_Management'),
    path('Crud', views.Crud, name='Crud'),
    path('signup', views.SignupPage, name='signup'),
    path('login', views.LoginPage, name='login'),
    path('logout', views.LogoutPage, name='logout'),
    path('add_record', views.add_record, name='add_record'),
    path('delete_record', views.delete_record, name='delete_record'),
    path('success/', views.success, name='success'),
    path('show_records', views.show_records, name='show_records'),
    # path('open-web-camera/', views.open_web_camera, name='open_web_camera'),
    path('recognize_face', views.recognize_face, name='recognize_face'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



