from django.contrib import admin
from django.http import HttpRequest, HttpResponse

from .models import Article, Review, WorksTags, WorksTasks, Works


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']
    fieldsets = [
        (None, {
            'fields': [
                'user',
                'title',
                'text',
            ]
        }),
        ("Метаданные", {
            'fields': [
                'created_at'
            ]
        })
    ]
    readonly_fields = ['user', 'title', 'text', 'status', 'created_at']

    def response_change(self, request: HttpRequest,
                        review: Review) -> HttpResponse:
        if '_deceline' in request.POST:
            review.status_deceline()
        elif '_accept' in request.POST:
            review.status_accept()
        return super().response_change(request, review)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs.filter(status=0)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {
                "fields": [
                    "image",
                    "title",
                    "author",
                    "description"
                ]
            }
        ),
        (
            "Метаданные", {
                "fields": [
                    "slug",
                    "created_at",
                ]
            }
        )
    )
    readonly_fields = ["slug", "created_at"]


class WorksTagsAdmin(admin.ModelAdmin):
    pass


class WorksTasksInline(admin.TabularInline):
    model = WorksTasks


class WorksAdmin(admin.ModelAdmin):
    inlines = [WorksTasksInline]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Works, WorksAdmin)
admin.site.register(WorksTags, WorksTagsAdmin)
