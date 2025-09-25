import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
load_dotenv()

class GeminiAIService:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
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
