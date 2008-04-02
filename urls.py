from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^todo/', include('todoer.do.urls')),

    # Uncomment this for admin:
     (r'^admin/', include('django.contrib.admin.urls')),
)
