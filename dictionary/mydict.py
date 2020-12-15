###kumpulan respon (dictionary)###
###collection of responses (dictionary)###

#kata kunci intent
#intent keywords
keywords = {
    'greet' : ['hello', 'hey', 'hi ', 'halo','helo','wassup', 'whats up', 'bruh', 'hi'], #1
    'introduce' : ['who are you', 'introduce yourself', 'am i know you?', 'what are you'], #2
    'goodbye' : ['bye', 'farewell', 'nice to meet you','see ya'], #3
    'thankyou' : ['thank', 'thx'], #4
    'sgreet':['hello there'], #5
    'ask name':['your name', 'name?', 'name'], #6
    'remember':['do you remember','remember'], #7
    'want':['i want', 'wanna', 'want', 'can i', 'may i'], #8
    'question' : ['do you mind','what do you', 'what can you do','can you'], #9
    'AYcircum' : ['how are you', 'how do you do', 'how\'s life','how\'s going', 'what\'s wrong with you'], #10
    'beat' : ['by the way', 'btw', 'you know what','\.....','um','hm'], #11
    'callyou' : ['echo bot','oi', 'hei echo', 'echo', 'bot', "you there"], #12
    'old' : ['how old','how old are you?', 'old', 'your birthday'], #13
    'think' : ['what do you think','what do you think about', 'have you ever think', 'think', 'thinking about',],#14
    '+Uanswer' : ['nice','yes', 'sure', 'why not', 'yes iam','great','interesting', 'really', 'ok','okay','yeah'],#15
    '-Uanswer' :['dunno', 'well, no', 'no','dont','don\'t'],#16
    'gender' : ['gender', 'what is your gender', 'you have any gender?', 'are you male or female', 'male', 'female'],#17
    'comand' : ['\@','\$','\>','\/',],#18
    'askcall' : ['can i call you', 'can i call you echo', 'what should i call you',],#19
    'offense' : ['shit', 'fuck', 'bitch',], #20
    'readme':['info', 'info about you', ],#21
    'user_need' : ["i need ", "would you get me", "need"],#22

}

#respon dari kata kunci
#response from keyword
responses = {
    "introduce":[
        'hello, my name is EchoBOT. What is your name?', 
        'Iam Echo BOt, a simple chat bot',
        'let me introduce myself, my name is echo Bot. And you?',
        'hey, iam ECHO BOT, a simple chat bot made in python, by Asthi21, do you know him?',
        'hello, my name is Echo Bot nice to meet you',
        'iam just a few hundreds lines of code'
    ],

    'old' : ['dunno man', 'I have no idea about it','Bruh... you know i am a bot...'],

    "greet" : ["hello", 'hello, how are you', 'hello there', 'Bruh...', 'Yo, wassup'],

    'AYcircum' : [
        'iam fine, thanks','iam great', 'great, what about you?', 'iam fine',
        'nothing happens','not good, what about you?', 'Daijoubou desu....'
    ],

    'default':[
        'Please rephrase...', 
        "Very interesting",
        "I am not sure I understand you fully",
        "What does that suggest to you?",
        "Please continue",
        "Go on",
        "Do you feel strongly about discussing such things?",
        "i dont get it",
        "i still dont understand",
        "i still dont get it",
        "could you explain",
        "explain yourself please",
        "do you have the slightest idea how little that narrows it down?",
        "I can’t get my head around it. Wait, i didnt had any head :D",
        "I have no clue"
        ],

    'ask name' : [
        "yes", 
        "sure","My name is EchoBot", 
        "they call me echo bot", 
        "Echo BOT",
        "my name is ECHO BOT",
        'you can call me ECHO BOT'
        ],

    'goodbye': [
        'farewell then',
        'nice to meet you',
        'see ya',
        'see you next time',
        'bye bye'
        ],

    'thankyou':[
        "your\'e welcome",
        'no problem',
        'okay',
        'dont mind it'
        ],

    'sgreet':['general kenobi'],

    'remember': [
        'Did you think I would forget{0}',
        "Why haven't you been able to forget{0}",
        'What about{0}',
        'Yes .. and?',
        "yes... why?"
        ],

    'want' : [
        'What would it mean if you got{0}',
        'Why do you want to {0}',
        "What's stopping you from getting{0}",
        'no, you can\'t{0}',
        'yes, you can'
        ],

    'question' : [
        'yes... yes iam',
        'yes i can{0}',
        'if {0}? Absolutely.',
        'No chance',
        'just {0}? Sure',
        'yes',
        'yes..... just kidding, i cant do anything :D',
    ],

    'beat' : ['yes?', 'what?', 'go on...', 'take your time', '...?','yes?'],

    'callyou' : ['yes?', 'can i help you?', 'what?','....?','iam here', 'whats wrong?','yes? can i help you?', 'did you just called me?'],

    'think' : ['i am thingking about you <(U-w-U)>', 'yeah i think {0} is a great idea','its great','nothing','NOPE, dont worrry, i cant think', 'What do you think about {0}'],

    '+Uanswer' : ['yes','good', 'great', 'wow, really?', 'thats great', 'NICE', 'cool'],
    '-Uanswer' : ['okay then', 'well, its okay'],

    'gender' : ['Dunno', 'Dunno man...', 'i have no idea','i dont think i have it','well yes, but actually no','I dont know','idk'],
    'comand' : [
        '-_-', 'do you think i have some comand? haha, unfortunately i dont',
        'i dont have any comand',':D','my creator didnt smart enough to give me a command key bruh'
        ],
      'usrname' : ['Hello, {0}!', 'hey {0}, iam echo bot', 'nice to meet you {0}', '{0}? thats a great name!'],
      'askcall' : ['echo','echo BOT','yes','why not','yes, you can call me{0}','you can call me echo','why you wanna call me {0} ?'],
      'offense' : ['woah woah woah','easy buddy','keep calm bruh','no offensive word please',],
      'readme' : ['okay', 'wait','hold up', 'wait a sec'],
      'user_need' : ["why would you need{0} ?", "why would you need that ?", "you need {0} ?", "sorry bruh, i cant get it for you", "you need{0}? okay then"],
    }
