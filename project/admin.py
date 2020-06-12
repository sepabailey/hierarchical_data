from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from project.models import Tree

admin.site.register(Tree, DraggableMPTTAdmin)
