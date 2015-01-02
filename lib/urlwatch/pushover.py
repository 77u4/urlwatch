from pushover import Client

# SETUP
	user_key  = ''
	api_token = ''

def send(title, message)
	client = Client(user_key, api_token)
	client.send_message(message, title)
