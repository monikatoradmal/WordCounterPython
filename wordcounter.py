from fastapi import FastAPI,HTTPException,status
import re
from typing import List

app= FastAPI()  #entrypoint of the api


valid_words={}        
        
@app.get("/count")
def get_all_count():
    return valid_words 

@app.get("/count/{word}")
def get_count_by_word(word:str):
    if valid_words.get(word) != None:
        return {word : valid_words.get(word)}    
    raise HTTPException(status_code=404,detail="Word not found")
        
def check_English_Dictionary(word):
    #This is a dummy method to check whether passed word is english or not  
    return word 

  
@app.post('/words/add')
def add_words(words :List[str]):
    for word in words:
        #skip word with numbers/special characters.
        if re.match('^[a-zA-Z]+$',word) == None:
            continue
        
        #check passed word in english dictionary else translate it to english
        word = check_English_Dictionary(word)
        
        count = valid_words.get(word)
        if count != None:
            valid_words.update({word:count+1})
        else:
            valid_words.update({word:1})    
    
    return "Words added successfully"
    
    
   

         

    



   

