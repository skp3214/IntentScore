import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
load_dotenv()

class GeminiAIService:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def analyze_lead_intent(self, lead_data, offer_data):
        
        prompt = self._build_prompt(lead_data, offer_data)
        
        try:
            response = self.model.generate_content(prompt)
            intent_label, reasoning = self._parse_ai_response(response.text)
            
            # Map intent to AI score
            ai_score_mapping = {'High': 50, 'Medium': 30, 'Low': 10}
            ai_score = ai_score_mapping.get(intent_label, 10)
            
            return intent_label, reasoning, ai_score
            
        except Exception as e:
            # Fallback in case of AI service failure
            return 'Low', f'AI analysis failed: {str(e)}', 10
    
    def _build_prompt(self, lead_data, offer_data):
        return f"""
        Analyze the buying intent of this prospect for the given product offer.
        
        PRODUCT OFFER:
        - Name: {offer_data.get('name', 'N/A')}
        - Value Propositions: {', '.join(offer_data.get('value_props', []))}
        - Ideal Use Cases: {', '.join(offer_data.get('ideal_use_cases', []))}
        
        PROSPECT DATA:
        - Name: {lead_data.get('name', 'N/A')}
        - Role: {lead_data.get('role', 'N/A')}
        - Company: {lead_data.get('company', 'N/A')}
        - Industry: {lead_data.get('industry', 'N/A')}
        - Location: {lead_data.get('location', 'N/A')}
        - LinkedIn Bio: {lead_data.get('linkedin_bio', 'N/A')}
        
        Classify the buying intent as High, Medium, or Low and provide a brief reasoning (1-2 sentences).
        
        Respond in exactly this format:
        Intent: [High/Medium/Low]
        Reasoning: [1-2 sentence explanation]
        """
    
    def _parse_ai_response(self, response_text):
        intent_match = re.search(r'Intent:\s*(High|Medium|Low)', response_text, re.IGNORECASE)
        reasoning_match = re.search(r'Reasoning:\s*(.+)', response_text, re.DOTALL)
        
        intent = intent_match.group(1) if intent_match else 'Low'
        reasoning = reasoning_match.group(1).strip() if reasoning_match else 'No reasoning provided'
        
        return intent, reasoning


class TransformersIntentService:
    def __init__(self):
        # Use a small, free model for text classification
        self.classifier = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            tokenizer="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze_lead_intent(self, lead_data, offer_data):
        """
        Use transformer model for intent classification and generate contextual reasoning.
        """
        prompt = self._build_prompt(lead_data, offer_data)

        try:
            result = self.classifier(prompt[:512])  # Limit length for small models
            confidence = result[0]['score']
            label = result[0]['label']

            # Map to our intent system based on confidence and role analysis
            intent = self._determine_intent(lead_data, offer_data, confidence, label)
            
            # Generate personalized reasoning for each lead
            reasoning = self._generate_personalized_reasoning(lead_data, offer_data, intent, confidence)

            intent_scores = {'High': 50, 'Medium': 30, 'Low': 10}
            ai_score = intent_scores.get(intent, 10)

            return intent, reasoning, ai_score

        except Exception as e:
            return 'Low', f'Local model analysis failed: {str(e)}', 10

    def _build_prompt(self, lead_data, offer_data):
        return (
            f"Analyze buying intent for this prospect:\n"
            f"Role: {lead_data.get('role')}\n"
            f"Industry: {lead_data.get('industry')}\n"
            f"Company: {lead_data.get('company')}\n"
            f"Offer: {offer_data.get('name')}\n"
        )
    
    def _determine_intent(self, lead_data, offer_data, confidence, label):
        """Determine intent based on role, industry, and model confidence"""
        role = lead_data.get('role', '').lower()
        industry = lead_data.get('industry', '').lower()
        
        # High-value roles and industries get bonus
        high_value_roles = ['ceo', 'cto', 'vp', 'director', 'head', 'founder', 'manager']
        tech_industries = ['technology', 'saas', 'software', 'ai', 'artificial intelligence', 'cloud']
        
        role_match = any(hvr in role for hvr in high_value_roles)
        industry_match = any(ti in industry for ti in tech_industries)
        
        if confidence > 0.85 and (role_match or industry_match):
            return 'High'
        elif confidence > 0.75 and role_match:
            return 'High'
        elif confidence > 0.6:
            return 'Medium'
        else:
            return 'Low'
    
    def _generate_personalized_reasoning(self, lead_data, offer_data, intent, confidence):
        """Generate unique, human-like reasoning for each lead"""
        name = lead_data.get('name', 'This prospect')
        role = lead_data.get('role', 'professional')
        company = lead_data.get('company', 'their organization')
        industry = lead_data.get('industry', 'their industry')
        location = lead_data.get('location', 'their location')
        
        # Generate different reasoning patterns based on intent level
        if intent == 'High':
            patterns = [
                f"{name}'s position as {role} at {company} positions them as a key decision-maker in the {industry} sector. Their authority and industry alignment with our solution suggests strong potential for engagement and conversion.",
                f"Given {name}'s senior role as {role}, they likely have budget authority and strategic influence at {company}. The {industry} industry's current market dynamics make this an opportune time for solution adoption.",
                f"As {role} at {company}, {name} represents an ideal target profile. Their leadership position in the {industry} space indicates both need and capability to implement our solution effectively.",
                f"The combination of {name}'s role as {role} and {company}'s position in the {industry} market creates a compelling opportunity. Senior stakeholders like {name} are typically early adopters of innovative solutions."
            ]
        elif intent == 'Medium':
            patterns = [
                f"While {name}'s role as {role} at {company} shows some alignment with our target profile, additional qualification is needed to determine their specific pain points and budget authority in the {industry} sector.",
                f"{name} presents a moderate opportunity given their position as {role}. However, {company}'s current priorities and {name}'s influence on technology decisions require further investigation.",
                f"The prospect {name} shows promise as {role} at {company}, though their exact decision-making authority and current solution gaps in the {industry} context need clarification.",
                f"As {role}, {name} may have influence at {company}, but determining their specific challenges and timeline for {industry} solutions will be crucial for qualification."
            ]
        else:
            patterns = [
                f"While {name} works as {role} at {company}, their current position may have limited decision-making authority for solutions like ours. The {industry} sector typically requires engagement with more senior stakeholders.",
                f"{name}'s role as {role} suggests they may not be the primary decision-maker at {company}. In the {industry} industry, purchasing decisions usually involve C-level or VP-level professionals.",
                f"Although {name} is positioned as {role} at {company}, their level of influence on strategic technology decisions in the {industry} sector appears limited based on available information.",
                f"The prospect {name} may serve more as an influencer rather than decision-maker in their role as {role}. {company} likely requires engagement with higher-level stakeholders for solution adoption."
            ]
        
        # Add location-based insights occasionally
        import random
        reasoning = random.choice(patterns)
        
        # Sometimes add location context
        if random.random() > 0.7 and location and location != 'Remote':
            location_context = f" Their {location} location also positions them well within a key market for our solution."
            reasoning += location_context
            
        return reasoning