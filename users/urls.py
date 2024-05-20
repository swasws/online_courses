from django.urls import path
from django.contrib.auth import views as auth_views
from .views import StudentRegisterView, TeacherRegisterView, RegisterLoginView
from .forms import CustomLoginForm

urlpatterns = [
    path('student/', StudentRegisterView.as_view(), name='student_registration'),
    path('teacher/', TeacherRegisterView.as_view(), name='teacher_registration'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/register_login.html', authentication_form=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register_login'), name='logout'),  # Перенаправление на страницу входа
    path('', RegisterLoginView.as_view(), name='register_login'),
]
