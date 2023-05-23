from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.studentList),
    path('stuinfo/<int:pk>',views.studentDetail),
    path('stucreate/',views.studentCreate)
]
