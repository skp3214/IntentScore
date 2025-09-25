from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Lead
from .serializers import ProductOfferSerializer,LeadUploadSerializer
import pandas as pd
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