from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL, insecure=True)