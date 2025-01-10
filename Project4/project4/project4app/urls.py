from . import views 
from django.urls import path
urlpatterns = [
    path('',views.home,name='home'),    
    path('registration/',views.registration,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('user_list/',views.user_list,name='user_list'),
    path('delete/<int:id>/', views.user_delete, name='delete'),
    # path('update/<int:id>/',views.update_user,name='update'),
    path('update/<int:id>/', views.update_user, name='update'),

]