import datetime

def process_cricketworldcup(message, context):
    
    print ("Received World Cup Cricket")
    print (message)
    
    response = {}
    
    response['game'] = message['game']
    response['event'] = message['event']
    response['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%D %H-%M-%S")
    response['welcome_message'] = 'Hi, Cricket worldcup will take place 3 years hence'
    
    return response