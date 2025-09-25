from django.urls import path
from IntentScoreAPI import views

urlpatterns = [
    path('product/offer/', views.create_offer, name='create-offer'),
    path('leads/upload/', views.upload_leads, name='upload-leads'),
    path('score/', views.score_leads, name='score-leads'),
]