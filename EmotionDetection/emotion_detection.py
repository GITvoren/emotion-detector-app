import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    my_obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=my_obj, headers=header)
    
    # --- DEBUG PRINTS ---
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    # --------------------
    
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
        
    return None