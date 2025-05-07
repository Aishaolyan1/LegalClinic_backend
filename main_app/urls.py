from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/signup/',views.CreateUserView.as_view(), name='signup'),
    path('users/token/refresh/', views.VerifyUserView.as_view(), name='token_refresh'),
    path('lawyers/', views.LawyerCreateListView.as_view(), name='create-list-lawyers'),
    path('lawyers/<int:lawyer_id>/', views.LawyerDetail.as_view(), name='view-update-delete-lawyer'),
]
