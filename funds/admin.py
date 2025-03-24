from django.contrib import admin

from .models import Fund


@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ("name", "strategy", "aum", "inception_date", "created_at", "updated_at")
    list_display_links = ("name",)
    list_filter = ("name", "strategy")
    list_per_page = 15
    search_fields = ("name",)
