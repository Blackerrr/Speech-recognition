# Speech-recognition
基于百度的语音识别，python3.8(conda)+pyaudio+pyqt+baidu-aip

百度有面向python的语音识别框架，用pip 直接安装

> pip install baidu-aip

安装完成后，在百度智能云完成登录，在控制台创建一个应用。

在下面填入自己的 APP_ID,API_KEY,SECRET_KEY后，能运行即可

```
def main():
    APP_ID = 'your id'
    API_KEY = 'your key'
    SECRET_KEY = 'your secret keys'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    outfile = "./audio/16k.wav"

    app = QApplication(sys.argv)
    form = ExampleApp(outfile, client)
    form.show()

    app.exec_()


if __name__ == '__main__':
    main()

```





