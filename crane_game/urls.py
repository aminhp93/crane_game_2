from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/', include('accounts.api.urls', namespace='users-api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
handler400 = 'crane_game.views.error400'
handler403 = 'crane_game.views.error403'
handler404 = 'crane_game.views.error404'
handler500 = 'crane_game.views.error500'

from rest_framework.documentation import include_docs_urls

urlpatterns += [
    url(r'^docs/', include_docs_urls(title='My API title', public=True))
]
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Server Monitoring API")

urlpatterns += [
    url('^$', schema_view),
]