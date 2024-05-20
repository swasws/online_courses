from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import CourseForm

@login_required
def all_courses_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', {'courses': courses})

@login_required
def my_courses_view(request):
    if request.user.is_teacher:
        courses = request.user.taught_courses.all()
    else:
        courses = Course.objects.filter(enrollments__student=request.user)
    return render(request, 'courses/my_courses.html', {'courses': courses})

@login_required
def create_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('all_courses')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def course_detail_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrolled = Enrollment.objects.filter(course=course, student=request.user).exists()
    return render(request, 'courses/course_detail.html', {'course': course, 'enrolled': enrolled})

@login_required
def enroll_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.user.is_student and request.user.studentprofile.year >= course.year_requirement:
        enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
        return redirect('my_courses')
    return redirect('all_courses')
