from operator import index
from django import views
from django.urls import path
from . import views
urlpatterns = [
      
       path('',views.index,name='index'), 
       path('settings',views.settings, name='settings'),
       path('upload',views.upload, name='upload'),
            path('like-post',views.like_post, name='like-post'),
       path('like',views.pf, name='pf'),
       path('pro',views.pro, name='pro'),
       path('signin',views.signin, name='signin'),
       path('logout',views.logout, name='logout'),
       path('change_password',views.change_password, name='change_password'),
       path('code',views.code, name='code'),
       
       path('signup',views.signup,name='signup'),
       path('chatroom',views.chatroom, name='chatroom'),
       path('frequest',views.frequest, name='frequest'),
       path('accfrequest',views.accfrequest, name='accfrequest'),
       path('thoughts',views.thoughts, name='thoughts'),
       path('my_photos',views.my_photos, name='my_photos'),
       path('about_me',views.about_me, name='about_me'),
      

      
       
    
]