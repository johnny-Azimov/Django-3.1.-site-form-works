from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    list_filter = ('car', 'title')
    search_fields = ('car__brand', 'car__model', 'title')


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
