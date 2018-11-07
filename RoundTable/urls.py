from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from .views import (
    registration_view,
    login_view,
    CallbackView,
    UserAccountView,
    CreateTeamView, TeamView, SearchView, AddInviteView)

urlpatterns = [
    path('', CreateTeamView.as_view(), name='index'),
    path('team_mod/<slug:slug>', TeamView.as_view(), name='team_mod'),

    # Если захочется сделать UserAccount для каждого пользователя с возможностью просмотра понадобится этот код
    # path('user_account/<str:user>', UserAccountView.as_view(), name='account_view'),

    path('user_account/', UserAccountView.as_view(), name='account_view'),
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),

    path('search/', SearchView.as_view(), name='search'),
    path('add_invite', AddInviteView.as_view(), name='add_invite'),
    path('vk_login/', RedirectView.as_view(url=settings.VK_REDIRECT), name='vk_login'),
    path('vk_callback/', CallbackView.vk_callback, name='vk_callback'),
    path('facebook_login/', RedirectView.as_view(url=settings.FACEBOOK_REDIRECT), name='facebook_login'),
    path('facebook_callback/', CallbackView.facebook_callback, name='facebook_callback'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
