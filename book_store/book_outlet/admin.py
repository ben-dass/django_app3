from django.contrib import admin

from .models import Address, Author, Book, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
    }

    list_filter = (
        "author",
        "rating",
    )

    list_display = (
        "title",
        "author",
        "is_best_seller",
    )


admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Country)
