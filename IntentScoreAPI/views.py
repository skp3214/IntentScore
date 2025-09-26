from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lead,ProductOffer
from .serializers import ProductOfferSerializer,LeadUploadSerializer,LeadSerializer,ScoringResultSerializer
import pandas as pd
from .services import LeadScoringService
from django.http import HttpResponse
import json


@api_view(['GET'])
def index(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>IntentScore API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            h2 { color: #666; margin-top: 30px; }
            .endpoint { margin: 10px 0; padding: 10px; background: #f5f5f5; border-radius: 5px; }
            .method { font-weight: bold; color: #007bff; }
            .path { font-family: monospace; }
        </style>
    </head>
    <body>
        <h1>🎯 IntentScore API</h1>
        <p>A sophisticated Lead Intent Scoring System powered by AI</p>
        <p><strong>Version:</strong> 1.0.0</p>
        
        <h2>Available Endpoints:</h2>
        
        <div class="endpoint">
            <span class="method">POST</span> <span class="path">/product/offer/</span>
            <br>Create a new product offer
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <span class="path">/leads/upload/</span>
            <br>Upload leads via CSV file
        </div>
        
        <div class="endpoint">
            <span class="method">POST</span> <span class="path">/score/</span>
            <br>Score leads against product offers
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <span class="path">/results/</span>
            <br>Get all leads with their scores
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <span class="path">/csv/</span>
            <br>Export results to CSV
        </div>
        
        <hr>
        <p><em>Built with Django REST Framework</em></p>
    </body>
    </html>
    """
    return HttpResponse(html_content, content_type='text/html')

@api_view(['POST'])
def create_offer(request):
    serializer = ProductOfferSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def upload_leads(request):
    serializer = LeadUploadSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    csv_file = request.FILES['csv_file']
    
    try:
        # validate CSV structure
        df = pd.read_csv(csv_file)
        required_columns = ['name','role','company','industry','location','linkedin_bio']
        
        if not all(col in df.columns for col in required_columns):
            missing = [col for col in required_columns if col not in df.columns]
            
            return Response(
                {'error':f'Missing required colums: {missing}'},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        # clear existing leads
        Lead.objects.all().delete()
        
        leads = []
        
        # save leads to db
        for _,row in df.iterrows():
            
            lead = Lead(
                name = row['name'],
                role = row['role'],
                company = row['company'],
                industry = row['industry'],
                location = row['location'],
                linkedin_bio = row['linkedin_bio']
            )
            
            leads.append(lead)
            
            # saving bulk data into db
        Lead.objects.bulk_create(leads)
            
        return Response(
            {'message':f'Successfully uploaded {len(leads)} leads'},
            status=status.HTTP_201_CREATED
        )
            
    except Exception as e:
        return Response(
            {'error':f'Error processing CSV: {str(e)}'},
            status=status.HTTP_400_BAD_REQUEST
        )
        
@api_view(['POST'])
def score_leads(request):
    
    try:
        offer = ProductOffer.objects.last()
        if not offer:
            return Response(
                {'error':'No product offer found. Please create an offer first.'},
                status = status.HTTP_400_BAD_REQUEST
            )
            
        # Get all uploaded leads
        
        leads = Lead.objects.all()
        if not leads.exists():
            return Response(
                {'error':'No leads found. Please upload leads first.'},
                status = status.HTTP_400_BAD_REQUEST
            )
            
        scoring_service = LeadScoringService()
        offer_data = {
            'name': offer.name,
            'value_props': offer.value_props,
            'ideal_use_cases': offer.ideal_use_cases
        }
        
        results = []
        
        for lead in leads:
            lead_data = {
                'name':lead.name,
                'role':lead.role,
                'company':lead.company,
                'industry':lead.industry,
                'location':lead.location,
                'linkedin_bio':lead.linkedin_bio
            }
            
            scoring_result = scoring_service.score_lead(lead_data, offer_data)
            
            lead.intent = scoring_result['intent']
            lead.score = scoring_result['score']
            lead.reasoning = scoring_result['reasoning']
            lead.save()
            
            results.append({
                'name':lead.name,
                'role':lead.role,
                'company':lead.company,
                'industry':lead.industry,
                'location':lead.location,
                'intent':lead.intent,
                'score':lead.score,
                'reasoning':lead.reasoning
            })
            
        serializer = ScoringResultSerializer(results,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {'error':f'Error scoring leads: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
@api_view(['GET'])
def get_results(request):
    
    leads = Lead.objects.all()
    serializer = LeadSerializer(leads, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def export_results_csv(request):
    
    leads = Lead.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lead_scores.csv"'
    
    df_data = []
    
    for lead in leads:
        df_data.append({
            'Name':lead.name,
            'Role':lead.role,
            'Company':lead.company,
            'Industry':lead.industry,
            'Location':lead.location,
            'Intent':lead.intent,
            'Score':lead.score,
            'Reasoning':lead.reasoning
        })
        
    df = pd.DataFrame(df_data)
    df.to_csv(response,index=False)
    
    return response