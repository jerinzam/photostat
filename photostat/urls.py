
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),    url(r'^printo-app/',include('printo_app.urls')),	
    url(r'^$','printo_app.views.index_main',name="index_mains"),


]


urlpatterns += [
                      
                        url(r'^printo-app/login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^printo-app/logout/$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^accounts/password/change/$',
                           auth_views.password_change,
			    {'template_name': 'registration/password_reset_form.html'},
                           name='auth_password_change'),
                       url(r'^accounts/password/change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^accounts/password/reset/$',
                           auth_views.password_reset,
			      {'template_name': 'registration/password_reset_form.html'},
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^accounts/password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^accounts/password/reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
              
		       ]

