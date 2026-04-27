from llm import summarize,tone_detect,generate_reply,get_tone
from schemas import RequestBody
from fastapi import FastAPI
import json 

app = FastAPI()

@app.post("/summarize")
def summarize_email(request : RequestBody):
    result = summarize(request.text)
    
    try :
        parsed = json.loads(result)
        return parsed
    except :
        return {"error" : "Invalid JSON from model","raw output" : result }
    
@app.post("/tone_detect")
def tone_detection(request : RequestBody):
    result = tone_detect(request.text)
    try :
        parsed = json.loads(result)
        return parsed
    except : 
        return {"error" : "Invalid JSON from model", "raw output" : result}
    
   
@app.post("/reply_generation")
def reply_generation(request : RequestBody):
    tone = get_tone(request.text)          
    result = generate_reply(request.text, tone)   
    
    try :
        parsed = json.loads(result)
        return parsed 
    except : 
        return {"error" : "Inavlid Json from model" , "raw output" : result}
    
