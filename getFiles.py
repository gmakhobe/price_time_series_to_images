import os

folder_path = "media/bearish"  # Replace with your folder path 

image_names = [
    f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png"))
]

new_names = ""



for image_name in image_names:
    print('{"content": "###' + image_name + '", "mimeType": "image/jpeg"}')