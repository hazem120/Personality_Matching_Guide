"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from personality import views

app_name = 'personality'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    ## personality stuffffffff
    path('', views.personality_list , name = 'personality_list') , 
    path('personality/<int:id>', views.personality_details , name = 'personality_details') , 
    path('accounts/profile/' , views.profile , name= 'profile' ),
    path('accounts/addpersonality' , views.create_personality  , name = 'add_personality' ) ,
    path('search' , views.search , name= 'search' ),

]



urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)