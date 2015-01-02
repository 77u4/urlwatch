from pushover import Client

def send(user_key, api_token, message, title)
	client = Client(user_key, api_token)
	client.send_message(message, title)
