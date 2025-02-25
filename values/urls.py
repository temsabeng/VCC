from django.contrib import admin
from django.urls import path
from .views import project_evaluation_view  # Kendi uygulamanızın adını kullanın
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', project_evaluation_view, name='home'),  # Ana sayfaya yönlendirme
   path('project_evaluation/', project_evaluation_view, name='project_evaluation'),
]