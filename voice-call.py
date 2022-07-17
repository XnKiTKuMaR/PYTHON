import messagebird

client = messagebird.Client('ZM0cNkqOFR3QtppYgDD1BtKeF')

try:
    msg = client.voice_message_create('+319876543211', 'Hey,I am learning Python!', { 'voice' : 'male' })
    print(msg.__dict__)

except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)
 
