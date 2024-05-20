from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, View
from .forms import StudentRegisterForm, TeacherRegisterForm, CustomLoginForm
from .models import CustomUser

class StudentRegisterView(CreateView):
    model = CustomUser
    form_class = StudentRegisterForm
    template_name = 'registration/student_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        user.is_student = True
        user.save()
        return super().form_valid(form)

class TeacherRegisterView(CreateView):
    model = CustomUser
    form_class = TeacherRegisterForm
    template_name = 'registration/teacher_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        user.is_teacher = True
        user.save()
        return super().form_valid(form)

class RegisterLoginView(View):
    def get(self, request, *args, **kwargs):
        student_form = StudentRegisterForm()
        teacher_form = TeacherRegisterForm()
        login_form = CustomLoginForm()
        return render(request, 'registration/register_login.html', {
            'student_form': student_form,
            'teacher_form': teacher_form,
            'login_form': login_form
        })

    def post(self, request, *args, **kwargs):
        if 'student_register' in request.POST:
            student_form = StudentRegisterForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                return redirect('login')
        elif 'teacher_register' in request.POST:
            teacher_form = TeacherRegisterForm(request.POST)
            if teacher_form.is_valid():
                teacher_form.save()
                return redirect('login')
        elif 'login' in request.POST:
            login_form = CustomLoginForm(data=request.POST)
            if login_form.is_valid():
                user = authenticate(
                    request,
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    return redirect('all_courses')
        return self.get(request, *args, **kwargs)
