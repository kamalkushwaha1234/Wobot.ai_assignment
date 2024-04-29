from django.urls import path, include
from api.views import user_views as views 
from django.utils.decorators import method_decorator



urlpatterns = [
    path('login/', views.login_page, name='login_page'),    
    path('register/', views.register_page, name='register'), 
    path('profile/', views.profile_page, name='profile_page'), 
    path('logout/', views.logout_user, name='logout_user'), 


    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/register/',views.registerUser, name="register_user"),

    path('api/profile/', views.getUserProfile, name="users-profile"),
    
    #path('profile/update/', views.updateUserProfile, name="users-profile-update"),
]

