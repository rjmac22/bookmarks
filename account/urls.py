from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    # previous login view
    #url(r'^login/$', views.user_login, name='login'),

    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', views.dashboard, name='dashboard'),

    # login /logout urls
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login',
            name='logout.logout_then_login'),

    # change password urls
    url(r'^password-change/$', 'django.contrib.auth.views.password_change',
         name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done',
           name="password_change_done"),

    # restore password urls
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset',
           name="password_reset"),
    url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done',
          name="password_reset_done"),
    url(r'^password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
         'django.contrib.auth.views.password_reset_confirm', name="password_reset_confirm"),
    url(r'^password_reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
       name="password_reset_complete"),

    # New user register
       url(r'^register/$', views.register, name='register'),

    # edit profile
    url(r'^edit/$', views.edit, name='edit'),

    # socal login URL
    url('social-auth', include('social.apps.django_app.urls', namespace='social')),
    # url('', include('django.contrib.auth.urls', namespace='auth')),
    # url('', include('social.apps.django_app.urls', namespace='social')),


    url(r'^users/follow/$', views.user_follow, name='user_follow'),

    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
