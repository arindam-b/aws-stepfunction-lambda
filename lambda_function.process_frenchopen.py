import datetime

def process_frenchopen(message, context):
    
    print ("Received French Open")
    print (message)
    
    response = {}
    
    response['game'] = message['game']
    response['event'] = message['event']
    response['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%D %H-%M-%S")
    response['welcome_message'] = 'Hi, this year French open will take place'
    
    return response