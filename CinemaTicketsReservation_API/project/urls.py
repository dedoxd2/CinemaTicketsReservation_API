from django.contrib import admin
from django.urls import path, include
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1
    path('django/jrm', views.no_rest_no_model)

]
