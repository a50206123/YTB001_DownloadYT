import yt_dlp

# Input : url
url = "https://www.youtube.com/watch?v=lCX8L2bFT5I"

ydl_opts = {'outtmpl': './Download MP4/%(title)s.%(ext)s', # Download Path
            'merge_output_format': 'mp4', # File Type
            'format': 'bestvideo+bestaudio', # Quality
            
            'postprocessors': [{ # Convert MP4 to MOV using FFMPEG
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mov',
            }]}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
