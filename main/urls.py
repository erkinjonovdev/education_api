from django.urls import path
from .views import login, information_view, banner_view, about_view, popular_universities_view, \
    popular_faculties_view, how_works_view, testimonials_view, create_contact_view, university_filter_view, \
    uni_details_view, student_cabinet_view, student_applied_universities, student_applied_university_single, \
    student_personal_manager_view, uni_admin_view, university_students, university_invoices, university_student_info, \
    replying_to_student, university_cabinet, backoffice_view, backoffice_universities, dashboard_university_info, \
    dashboard_students, dashboard_student_info

urlpatterns = [
    path('login/', login),
    path('information/', information_view),
    path('banner/', banner_view),
    path('about/', about_view),
    path('popular-universities/', popular_universities_view),
    path('popular-faculties/', popular_faculties_view),
    path('how-works/', how_works_view),
    path('testimonials/', testimonials_view),
    path('create-contact/', create_contact_view),
    path('university-filter/', university_filter_view),
    path('uni-details/<int:pk>/', uni_details_view),
    path('student-cabinet/<int:pk>/', student_cabinet_view),
    path('student-applied-universities/<int:pk>/', student_applied_universities),
    path('student-applied-university_single/<int:pk>/', student_applied_university_single),
    path('student-personal-manager/<int:pk>/', student_personal_manager_view),
    path('uni-admin/', uni_admin_view),
    path('university-students/<int:pk>/', university_students),
    path('university-invoices/<int:pk>/', university_invoices),
    path('university-student_info/<int:pk>/', university_student_info),
    path('replying-to_student/<int:pk>/', replying_to_student),
    path('university-cabinet/<int:pk>/', university_cabinet),
    path('backoffice/', backoffice_view),
    path('backoffice-universities/', backoffice_universities),
    path('dashboard-students/', dashboard_students),
    path('dashboard-university-info/<int:pk>/', dashboard_university_info),
    path('dashboard-student-info<int:pk>/', dashboard_student_info),
]
