import datetime

def process_european_cup(message, context):
    
    print ("Received European Cup")
    print (message)
    
    response = {}
    
    response['game'] = message['game']
    response['event'] = message['event']
    response['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%D %H-%M-%S")
    response['welcome_message'] = 'Hi, this year European cup will take place'
    
    return response