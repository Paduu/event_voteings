from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'voteings', views.VoteingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
