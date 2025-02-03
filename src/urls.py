from dj_rest_auth import views
from dj_rest_auth.jwt_auth import get_refresh_view
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication
    path("api/auth/login/", views.LoginView.as_view(), name="login"),
    path("api/auth/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("api/auth/logout/", views.LogoutView.as_view(), name="logout"),
    path("api/", include("src.apps.users.api.urls")),
]

# Docs urls
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]


if settings.DEBUG:
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
