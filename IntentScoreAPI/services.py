import pandas as pd
from .ai_integration import GeminiAIService, TransformersIntentService

class LeadScoringService:
    def __init__(self):
        self.ai_service = TransformersIntentService()
        self.decision_maker_roles = [
            'ceo', 'cfo', 'cto', 'cmo', 'coo', 'president', 'vp', 'vice president',
            'director', 'head of', 'manager', 'founder', 'owner'
        ]
        self.influencer_roles = [
            'specialist', 'analyst', 'coordinator', 'assistant', 'associate'
        ]
    
    def calculate_rule_score(self, lead_data):

        score = 0
        
        # Role relevance (max 20 points)
        role = lead_data.get('role', '').lower()
        if any(dm_role in role for dm_role in self.decision_maker_roles):
            score += 20
        elif any(inf_role in role for inf_role in self.influencer_roles):
            score += 10
        
        # Industry match (max 20 points) - This would be enhanced with actual ICP data
        # For now, using simple matching based on common patterns
        industry = lead_data.get('industry', '').lower()
        if 'saas' in industry or 'tech' in industry or 'software' in industry:
            score += 20
        elif 'business' in industry or 'services' in industry:
            score += 10
        
        # Data completeness (max 10 points)
        required_fields = ['name', 'role', 'company', 'industry', 'location']
        if all(lead_data.get(field) for field in required_fields):
            score += 10
        
        return min(score, 50)
    
    def score_lead(self, lead_data, offer_data):
        # Rule-based scoring
        rule_score = self.calculate_rule_score(lead_data)
        
        # AI-based scoring
        intent_label, reasoning, ai_score = self.ai_service.analyze_lead_intent(
            lead_data, offer_data
        )
        
        # Final score
        total_score = rule_score + ai_score
        
        return {
            'intent': intent_label,
            'score': total_score,
            'reasoning': reasoning,
            'rule_score': rule_score,
            'ai_score': ai_score
        }