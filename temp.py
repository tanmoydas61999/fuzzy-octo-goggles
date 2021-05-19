import telebot
import requests
import json
import os

bot = telebot.TeleBot("1114840719:AAE53BQlnmss5p49Z7xsAz5fkGesVVF35ME")

@bot.message_handler(content_types=['video'])
def send_welcome(message):
	file_name = message.json['video']['file_name']
	print(file_name)
	file = bot.get_file(message.video.file_id)
	r = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format('1114840719:AAE53BQlnmss5p49Z7xsAz5fkGesVVF35ME', file.file_path))
	# with open(file_name,'wb') as f:
	# 	f.write(r.content)
	headers = {"Authorization": "Bearer " + os.environ['Token']}
	para = {
	    "name": file_name,
	}
	files = {
	    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
	    'file': r.content
	}
	r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
	)
	print(r.text)

bot.polling() 





