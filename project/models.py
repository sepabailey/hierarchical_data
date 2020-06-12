from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Tree(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name="children")

    class MPTTMeta:
        level_attribute = 'mptt_level'
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
