from django.shortcuts import render
from project.models import Tree


def index(request):
    tree_data = Tree.objects.all()
    return render(request, 'index.html', {'tree_data': tree_data})
