from pytube import YouTube, Playlist

def download_yt(url = 'https://www.youtube.com/watch?v=OnThkOMc658', folder = './', filetype = 'mp4') :
    yt =YouTube(url, use_oauth=True, allow_oauth_cache=True)

    yt.streams.filter(file_extension = filetype).get_highest_resolution().download(folder)

    print('Finished !!')

def on_progress(stream, chunk, remains) :
    total = stream.filesize
    percent = (total - remains) / total * 100

    print(f'Downloading ... {percent : .2f}%', end = '\r')

def download_yts(urls, folder, filetype, quality):
    num_url = len(urls)
    
    for url in urls :
        yt = YouTube(url)
        
        if filetype == 'mp3' :
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(folder, filename = f'{yt.title}.{filetype}')
            print(f'{yt.title} Finished !!')
        else :
            if quality == 'high' :
                stream = yt.streams.filter().get_highest_resolution()
            elif quality == '1080p' :
                stream = yt.streams.filter().get_by_resolution('1080p')
            else :
                steam = yt.streams.filter().get_by_resolution('720p')
                
            stream.download(folder, filename = f'{yt.title}.{filetype}')
            
def download_yt_playlist(url, folder = './') :
    yt = Playlist(url)
    
    yt.download_all('./')

if __name__ == '__main__' :
    download_yt(folder = './', filetype = 'mp4')