import requests

class API:

    def __init__(self):
        self.api_key = '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'
        self.sentiment_url = 'https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english'
        self.ner_url = 'https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english'
        self.emotion_url = 'https://api-inference.huggingface.co/models/nateraw/bert-base-uncased-emotion'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type' : 'application/json'
    
        }

    def sentiment_analysis_result(self,text):
        payload = {'inputs':text}
        Response = requests.post(self.sentiment_url, json = payload, headers = self.headers )
        
        print("Sentiment Status Code:-", Response.status_code)
        print("Sentiment ", Response.content)
        return Response.json()
    
    def NER_result(self,text):
        payload = {'inputs' : text}
        Response = requests.post(self.ner_url, json = payload, headers = self.headers)

        print("NER Status Code :-",Response.status_code)
        print('NER result :-',Response.content)
        return Response.json()
    
    def Emotion_result(self,text):
        payload = {'inputs' : text}
        Response = requests.post(self.emotion_url, json = payload, headers = self.headers)

        print('Emotion status Code :-',Response.status_code)
        print('Emotion prediction result :- ',Response.content)
        return Response.json()
