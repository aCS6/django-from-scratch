from django.contrib import admin
from django.urls import path

# import view of board app
from boards import views

urlpatterns = [
    path('' , view=views.home, name='home'), # map the view with url
    path('admin/', admin.site.urls),
]
