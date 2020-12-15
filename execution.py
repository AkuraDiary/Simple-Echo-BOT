#untuk mengeksekusi dari taskdict
import re 
import random
from dictionary import taskdict
import task

#membuat patterns
patterns = {}

for intent, keys in taskdict.keywords.items():
    patterns [intent] = re.compile('|'.join(keys))

def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        if re.search(pattern,message):
            matched_intent = intent
    return matched_intent

def execution(message):
    response = None
    #key = None
    intent = match_intent(message.lower())
    #searching for key intent
    if intent in taskdict.responses:
        key = intent
        response = random.choice(taskdict.responses[key])
        #running task
        task.run(key)
    #else:
        #response = None

    return response
    
#testing
#print(execution('what'))
#print(execution(" "))
#print(execution("give me notes about wifi"))
#input("")
#print(match_intent('notes'))