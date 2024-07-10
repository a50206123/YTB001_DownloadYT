from pytube import YouTube 

def download_yt(url = 'https://www.youtube.com/watch?v=OnThkOMc658', folder = 'Download MP4', filetype = 'mp4') :
    yt =YouTube(url, on_progress_callback= on_progress)

    yt.streams.filter().get_highest_resolution().download(folder)

    print('Finished !!')

def on_progress(stream, chunk, remains) :
    total = stream.filesize
    percent = (total - remains) / total * 100

    print(f'Downloading ... {percent : .2f}%', end = '\r')

if __name__ == '__main__' :
    download_yt()