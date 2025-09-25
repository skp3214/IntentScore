from django.urls import path
from IntentScoreAPI import views

urlpatterns = [
    path('product/offer/', views.create_offer, name='create-offer'),
    path('leads/upload/', views.upload_leads, name='upload-leads'),
    path('score/', views.score_leads, name='score-leads'),
    path('results/', views.get_results, name='get-results'),
    path('csv/', views.export_results_csv, name='export-csv'),
]