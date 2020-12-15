from dictionary import mydict, taskdict
import time
import re
import random
import execution as ex
import pyttsx3 as sound

#template
bot_template = "ECHO : {0}\n"
#user_template = "USER : {0}"

### untuk efek suara (sound efffect)###
#creating object
speak = sound.init()

#changing rate
rate = speak.getProperty("rate")
speak.setProperty("rate",121)

#change voice
voices = speak.getProperty("voices")
speak.setProperty("voice", voices[0].id)


#untuk memembuat sebuah patterns
#patterns
patterns = {}

for intent, keys in mydict.keywords.items():
    patterns [intent] = re.compile('|'.join(keys))


###### program ######

def match_intent(message):
    #print(message)
    matched_intent = None
    
    for intent,pattern in patterns.items():
        if re.search(pattern,message):
            matched_intent=intent
    return matched_intent

def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
            #print(name)
    return name

def replace_pronouns(message):
    message = message.lower()
    if ' I ' in message:
        return re.sub('I', 'you', message)
    if ' my ' in message:
        return re.sub('my', 'your', message)
    if ' your ' in message:
        return re.sub('your', 'my', message)
    if ' me ' in message:
        return re.sub('me', 'you', message)
    if ' you ' in message:
        return re.sub('you', 'me', message)

    return message

    

#respon pesan
#message respond
def respond(message):
    response = None
    key='default'
    #call match_intent
    intent=match_intent(message.lower())
    name = find_name(message)
        
    #processing message
    if intent in mydict.responses:
        key = intent
        response = random.choice(mydict.responses[key])
    #print(intent, response,)
    if intent not in mydict.responses:
        #searching intent in ex module
        intent = ex.match_intent(message)
        #getting response
        response = ex.execution(message)
        if intent is None :
            response = random.choice(mydict.responses[key])
        #print(intent, response)
    
### processing message ###
    #searching if there is {0}
    phrase = message
    if "{0}" in response:
        #response, phrase = match_rule(response, message)
        #membuat match objek
        #creating match object
        match = re.search(patterns[intent], phrase) 
        
        #menggabungkan dengan pesan
        #joining message
        phrase = re.sub(str(match.group()), "", phrase)

        # # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase) 

        # Include the phrase in the response 
        response = response.format(phrase) 
        #print(response)

    if name is not None:
        response = random.choice(mydict.responses['usrname']).format(name)
    
    return response

##do not erase##
##jangan dihapus, dipakai jarang dibuang sayang##
'''
def match_rule(response, message):
    #response, phrase = None, None
    # Iterate over the rules dictionary
    for pattern, response in patterns.items():
        # Create a match object
        #match = re.search(responses[response], message)
        #if match is not None:
            # Choose a random response
            #response = random.choice(responses[key])
        if '{0}' in response:
            match = re.search(responses[key], message)
            phrase = match.group(1)
            phrase = replace_pronouns(phrase)
    # Return the response and phrase
    return response, phrase#format(phrase)
''' 
#to play sound
def sound_message(response):
    #run
    speak.say(response)
    speak.runAndWait()

def speech_setting(filename):
  file = open(filename  , "r")
  content = file.read()
  file.close
  return(str(content))
  
#pengirim pesan
#send message
Voice_effect = True
if speech_setting("voice_setting.txt") == "off":
    Voice_effect = False
elif "on" : 
    Voice_effect = True

def send_message(message):
    #print user_template & message
    #print(user_template.format(message))

    responses = respond(message)
    
    time.sleep(random.uniform(0.1,1))
    #print BOT_template & responses
    print(bot_template.format(responses))
    if Voice_effect is True:
        sound_message(responses)
        
    
"""def temp_msg(msg):
  print(msg)
  return msg"""
  
#testing
'''
send_message("halo")
send_message("hi")
send_message("hey there ")
send_message("hello there")
send_message("bye")    
send_message("you have any name ? ")
send_message("hello there")    
send_message("what's your name ?")
send_message("how are you?")
send_message("your book")
send_message("do you remember your last birthday?")
send_message("can you do something for me?")
send_message("who are you?")
'''
#send_message('what')
