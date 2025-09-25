import yt_dlp

url = "https://www.youtube.com/watch?v=lCX8L2bFT5I"

ydl_opts = {'outtmpl': './Download MP4/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'format': 'best'}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
