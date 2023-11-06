"""ee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path(r'^secret/', include(admin.site.urls)),
    path("iiti-ee-admin-login/", admin.site.urls),
    path("api/announcement/", include('announcements.urls'), name="announcement"),
    path("api/events/", include('events.urls'), name='event'),
    path("api/news/", include('news.urls'), name='news'),
    path("api/people/", include('people.urls'), name='people'),
    path("api/research/", include('research.urls'), name='research'),
    path("api/course/", include('course.urls'), name='course'),
    path("api/achievements/", include('achievements.urls'), name='achievements')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
