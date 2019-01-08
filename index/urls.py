from django.urls import path, include
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('reservation/', views.book_table, name='book_table'),
    path('change-or-cancel-reservation', views.change_or_cancel, name='change_or_cancel'),
    path('vote/', views.vote, name='survey_vote'),
]