from django.urls import path
from .views import (CoursesView,
                    my_fbv)

app_name = 'courses'
urlpatterns = [
    path('', CoursesView.as_view(template_name='about.html'), name='courses_list'),
    #path('', my_fbv.as_view(), name='courses-last'),
    path('<int:id>/', CoursesView.as_view(), name='courses-detail'),

]
