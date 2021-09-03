from django.urls import path,include
from .views import account_signup,account_login,logout_student,student_profile,student_wallet


urlpatterns = [
    path('account/',account_login,name="student_account_login"),
    path('account/signup',account_signup,name="student_account_signup"),
    path('logout',logout_student, name="logout_student"),

    path('profile/',student_profile, name="student_profile"),
    path('wallet/',student_wallet, name="student_wallet"),
]