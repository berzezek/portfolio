from django.shortcuts import render, get_object_or_404
from .models import Portfolio


def index(request):
    projects = Portfolio.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})


def detail(request, project_id):
    project_detail = get_object_or_404(Portfolio, pk=project_id)
    return render(request, 'portfolio/detail.html', {'detail': project_detail})