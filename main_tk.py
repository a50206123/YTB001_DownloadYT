import download_yt
import tkinter as tk

height_widget = 1

class DownloadYouTube(tk.Tk) :
    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self) :
        self.title('Download YouTube APP')
        self.geometry('600x100')
        
        self.frame_input = tk.Frame(self, width= 550, padx= 10, pady=10)
        self.frame_input.pack()

        self.label_input = tk.Label(self.frame_input, text= 'Input YouTube Url :', height= height_widget, padx= 3, pady=3)
        self.url_input = tk.Entry(self.frame_input)
        self.label_folder = tk.Label(self.frame_input, text= 'Download Folder :', height= height_widget, padx= 3, pady=3)
        self.folder_input = tk.Entry(self.frame_input)

        self.label_input.grid(column=0, row=0)
        self.url_input.grid(column=1, row=0)
        self.label_folder.grid(column=0, row=1)
        self.folder_input.grid(column=1, row=1)

        self.frame_button = tk.Frame(self, width=550, padx=10, pady=10)
        self.frame_button.pack()

        self.btn_download = tk.Button(self.frame_button, padx=3, pady=3, text='Click to Download!', 
                                      command= lambda (download_yt.download_yt(url=self.url_input.get(), 
                                                                       folder=self.folder_input.get())))
        
        self.btn_download.grid(column=5, row=0)

        self.mainloop()

if __name__ == '__main__' :
    dyt = DownloadYouTube()