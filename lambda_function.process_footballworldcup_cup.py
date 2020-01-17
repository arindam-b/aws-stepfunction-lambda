import datetime

def process_footballworldcup_cup(message, context):
    
    print ("Received World Cup Football")
    print (message)
    
    response = {}
    
    response['game'] = message['game']
    response['event'] = message['event']
    response['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%D %H-%M-%S")
    response['welcome_message'] = 'Hi, Football worldcup will take place 2 years hence'
    
    return response