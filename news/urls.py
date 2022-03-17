from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostAdd


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view(), name='NewsSearch'),
    path('add/', PostAdd.as_view(), name='NewsAdd'),

]
