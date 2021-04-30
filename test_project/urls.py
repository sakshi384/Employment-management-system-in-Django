"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from crud import views

# from django.views.generic.base import TemplateView
app_name = "crud"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('crud.urls')),
    # path('home/', include('home.urls')),
    path('register/',views.sign_up,name="regsiter"),
    path('',include('crud.urls')),
    path('',views.add_show,name='addandshow'),
    path('delete/<int:id>/',views.delete_record,name="deletedata"),
    path('update/<int:id>/',views.update_record,name="updatedata"),
    path('search/',views.search_record,name="searchdata"),


]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
