from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, \
    QFileDialog, QToolButton, QRadioButton, QTabWidget
import sys

from download_yt import download_yt, download_yts, download_yt_playlist

class main(QMainWindow) :
    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self) :
        self.ui = uic.loadUi('ui/MainWindow.ui', self)
        
        # Def. Tab
        self.tabWidget = self.ui.findChild(QTabWidget, 'tabWidget')
        
        # Def. LineEdit
        self.le_link1 = self.ui.findChild(QLineEdit, 'le_link1')
        self.le_link2 = self.ui.findChild(QLineEdit, 'le_link2')
        self.le_link3 = self.ui.findChild(QLineEdit, 'le_link3')
        self.le_link4 = self.ui.findChild(QLineEdit, 'le_link4')
        self.le_link5 = self.ui.findChild(QLineEdit, 'le_link5')
        self.le_links = [self.le_link1, self.le_link2, self.le_link3, 
                         self.le_link4, self.le_link5]
        
        self.le_link11 = self.ui.findChild(QLineEdit, 'le_link11')
        
        self.le_download_path = self.ui.findChild(QLineEdit, 'le_download_path')
        
        # Def. Buttons
        self.btn_select_path = self.ui.findChild(QToolButton, 'btn_select_path')
        self.pbtn_download = self.ui.findChild(QPushButton, 'pbtn_download')
        
        # Def. RadioButton
        self.rb_mp3 = self.ui.findChild(QRadioButton, 'rb_mp3')
        self.rb_mp4 = self.ui.findChild(QRadioButton, 'rb_mp4')
        
        self.rb_high = self.ui.findChild(QRadioButton, 'rb_high')
        self.rb_1080 = self.ui.findChild(QRadioButton, 'rb_1080')
        self.rb_720 = self.ui.findChild(QRadioButton, 'rb_720')
        
        # Connect
        self.pbtn_download.clicked.connect(self.download)
        self.btn_select_path.clicked.connect(self.select_path)
        
    def select_path(self) :
        path = QFileDialog.getExistingDirectory()
        self.le_download_path.setText(path)

    def download(self) :
        # File Type
        if self.rb_mp3.isChecked() :
            filetype = 'mp3'
        else :
            filetype = 'mp4'
        
        # Quality
        if self.rb_high.isChecked() :
            quality = 'high'
        elif self.rb_1080.isChecked() :
            quality = '1080p'
        else :
            quality = '720p'
        
        # Download Path
        path = self.le_download_path.text()
        
        if self.tabWidget.currentIndex() == 0 :
            urls = []
            for le in self.le_links :
                if le.text() :
                    urls.append(le.text())
            
            download_yts(urls, path, filetype, quality)
            
        elif self.tabWidget.currentIndex() == 1 :
            url = self.le_link11.text()
            download_yt_playlist(url, path)
        
        # print(f"It's {filetype} and {quality}")
        
if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec_()