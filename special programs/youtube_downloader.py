from yt_dlp import YoutubeDL

# url = input('Enter URL: ')
# name = input('Enter name to save your file: ')

url = 'https://www.youtube.com/watch?v=0SkXKAY5rRQ'
ydl_opts = {
    'format': 'best[ext=mp4]',  # Use best format available
    'outtmpl': f'resources/aaye aaye.mp4',
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
except Exception as e:
    print(f"An error occurred: {e}")