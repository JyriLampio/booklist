from django.contrib import admin
from django.urls import path
from books import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookcollection/', views.BookcollectionListView.as_view()),
	path('bookcollection/<int:pk>', views.BookcollectionDetailView.as_view()),
	path('bookcollection/<int:pk>/update', views.BookcollectionUpdateView.as_view()),
	path('bookcollection/create/', views.BookcollectionCreateView.as_view()),
	path('bookcollection/<int:pk>/delete', views.BookcollectionDeleteView.as_view()),
]
