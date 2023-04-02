from django.urls import path
from shop import views

urlpatterns = [
    path('', views.homepage),
    #path('student/<int:id>', views.student_details)
]