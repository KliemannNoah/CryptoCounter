from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # allows for header and footer to be used in other templates
    re_path(r'header.html$', views.header, name='header'),
    re_path(r'footer.html$', views.footer, name='footer'),
    # url paths for site
    path('', views.market, name='market'),
    path('market', views.market, name='market'),
    path('ico', views.ico, name='ico'),
    path('socialtrends', views.socialTrends, name='socialtrends'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('watchlist/addcoin/<int:cid>/', views.addWatchlistCoin, name='addwatchlistcoin'),
    path('watchlist/deletecoin/<int:cid>/', views.deleteWatchlistCoin, name='deletewatchlistcoin'),
    path('watchlist/addico/<int:iid>/', views.addWatchlistIco, name='addwatchlistico'),
    path('watchlist/deleteico/<int:iid>/', views.deleteWatchlistIco, name='deletewatchlistico'),
    path('login', views.login, name='login'),
    path('logout', auth_views.logout, {'next_page': 'market'}, name='logout'),
    path('register', views.register, name='register'),
    path('account', views.account, name='account'),
    path('deleteaccount', views.deleteAccount, name='deleteaccount'),
    path('coindetails/<str:cname>/', views.coinDetails, name='coindetails'),
    path('icodetails/<str:iname>/', views.icoDetails, name='icodetails'),
    path('search', views.search, name='search'),
]
