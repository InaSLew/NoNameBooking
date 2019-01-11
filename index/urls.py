from django.urls import path, include
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('reservation/', views.book_table, name='book_table'),
    path('reschedule-or-cancel-reservation', views.reschedule_or_cancel, name='reschedule_or_cancel'),
    path('cancel-reservation', views.cancel_reservation, name='cancel_reservation'),
    path('reschedule-reservation', views.reschedule_reservation, name="reschedule_reservation"),
    path('vote/', views.vote, name='survey_vote'),
]