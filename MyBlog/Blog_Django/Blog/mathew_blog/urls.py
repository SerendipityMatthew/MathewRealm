from django.urls import path

from mathew_blog import views
app_name = 'mathew_blog'
urlpatterns = [
    path('', views.index, name='index')
]