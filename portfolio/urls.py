from django.urls import path

from portfolio.models import Portfolio
from .views import index, detail


app_name = 'project'

urlpatterns = [
    path('', index, name='project'),
    path('<int:project_id>', detail, name='project_detail'),
]
