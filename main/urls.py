from django.urls import path, include
from .views import HomePageView, gallery_view, ContactPageViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("gallery/", gallery_view, name="Gallery"),
    path("contact/", ContactPageViews.as_view(), name="Contact")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)