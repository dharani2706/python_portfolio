from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve as serve_media

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path(
            "media/<path:path>",
            serve_media,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage your portfolio content"
