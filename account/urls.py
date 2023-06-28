from account.views import RegistrationView,CheckAuthenticatedView,ActivateView,ActivationConfirm,GetCSRFToken,LoginView,LogoutView,UserDetailView,ChangePasswordView,DeleteAccountView,ResetPasswordEmailView,ResetPasswordConfirmView,ResetPasswordView
from django.urls import path


urlpatterns = [
    path('account/csrf_cookie/',GetCSRFToken.as_view(),name='csrf_token'),
    path('account/authenticate/',CheckAuthenticatedView.as_view(),name='authenticate'),
    path('account/registration/',RegistrationView.as_view(),name='register'),
    path('account/activate/<str:uid>/<str:token>/',ActivateView.as_view(),name='activate'),
    path('account/activate/',ActivationConfirm.as_view(),name='activation_confirm'),
    path('account/login/',LoginView.as_view(),name='login'),
    path('account/user/',UserDetailView.as_view(),name='user_detail'),
    path('account/ch_password/',ChangePasswordView.as_view(),name='ch_password'),
    path('account/delete_account/',DeleteAccountView.as_view(),name='delete_account'),
    path('account/logout/',LogoutView.as_view(),name='logout'),
    path('account/reset_password_email/',ResetPasswordEmailView.as_view(),name='reset_password_email'),
    path('account/reset_password/<str:uid>/<str:token>/',ResetPasswordView.as_view(),name='reset_password'),
    path('account/reset_confirm/',ResetPasswordConfirmView.as_view(),name='reset_confirm'),
]
