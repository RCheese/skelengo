from django.contrib import admin

from .models import Ship


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created", "updated", "tag_list")
    ordering = ("-created",)
    search_fields = ("title",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
