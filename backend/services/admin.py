from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from .models import Order, Service, ServiceCategory


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status']

    fieldsets = [
        (None, {
            'fields': [
                'customer',
                'status',
                'deadline',
                'description'
            ]
        })
    ]

    readonly_fields = ['customer', 'status', 'deadline', 'description', 'serviceCategory']

    actions = []

    def response_change(self, request: HttpRequest,
                        order: Order) -> HttpResponse:
        if '_onprogress' in request.POST:
            order.status_progress()
        elif '_remove' in request.POST:
            order.status_canceled()
        elif '_finished' in request.POST:
            order.status_finished()
        return super().response_change(request, order)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class ServiceCategoryInline(admin.TabularInline):
    model = ServiceCategory
    extra = 0


class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [
            "image",
            "image_card",
            "title",
            "description"
        ]}),
        ("Метаданные", {"fields": [
            "slug",
            "created_at"
        ]})
    ]
    readonly_fields = ["slug", "created_at"]
    inlines = [ServiceCategoryInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
