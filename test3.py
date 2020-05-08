import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("youtubedn2.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton1.clicked.connect(self.button1Function)
        self.pushButton1.clicked.connect(self.button2Function)
        # self.LineEdit1.textChanged.connect(lineeditURLFunction)

    def lineeditURLFunction(self):
        ss = self.LineEdit1.text()

    def button2Function(self):
        print("btn_2 Clicked")

    def button1Function(self):
        VIDEO_DOWNLOAD_PATH = './musics'  # 다운로드 경로

        def download_video_and_subtitle(output_dir, youtube_video_list):

            download_path = os.path.join(
                output_dir, '%(id)s-%(title)s.%(ext)s')

            for video_url in youtube_video_list:

                # youtube_dl options
                ydl_opts = {
                    'format': 'best/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
                    'outtmpl': download_path,  # 다운로드 경로 설정
                    'writesubtitles': 'best',  # 자막 다운로드(자막이 없는 경우 다운로드 X)
                    'writethumbnail': 'best',  # 영상 thumbnail 다운로드
                    'writeautomaticsub': True,  # 자동 생성된 자막 다운로드
                    'subtitleslangs': 'en'  # 자막 언어가 영어인 경우(다른 언어로 변경 가능)
                }

                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_url])
                except Exception as e:
                    print('error', e)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    #ss = input("url 주소 적으세요.")
#    youtube_url_list = [  # 유투브에서 다운로드 하려는 영상의 주소 리스트(아래는 Sample Video 리스트)
#        ss
#    ]
#    download_video_and_subtitle(VIDEO_DOWNLOAD_PATH, youtube_url_list)
#    print('Complete download!')

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())
