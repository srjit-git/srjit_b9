from django.urls import path
from teacher import views
urlpatterns = [
    path('tec/',views.teacher),
    path('book_add/',views.Bookcreateview.as_view()),
    path('view_book/',views.BookListView.as_view(),name='view_book'),
    path('del_book/<int:pk>',views.BookDelete.as_view(),name='del_book'),
    path('upd_book/<int:pk>',views.Bookupdate.as_view(),name='upd_book'),
    path('Humanview/',views.Humanview.as_view(),name='Humanview'),

]