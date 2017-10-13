from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('accounts.api.urls', namespace='users-api')),

]
handler400 = 'crane_game.views.error400'
handler403 = 'crane_game.views.error403'
handler404 = 'crane_game.views.error404'
handler500 = 'crane_game.views.error500'