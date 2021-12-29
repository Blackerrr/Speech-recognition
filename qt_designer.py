from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from aip import AipSpeech
import sys, window, wave, pyaudio
import threading, time

'''
dev_pid:
    1537 普通话
    1737 英语
    1637 粤语
    1837 四川话 
'''
dev = {'普通话': 1537, '英语': 1737, '粤语': 1637, '四川话': 1837}


class ExampleApp(QtWidgets.QMainWindow, window.Ui_SpeechRecognition):
    def __init__(self, filename, client, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        self.filename = filename
        self.client = client

        self.pushButton.clicked.connect(self.button1_clicked)
        self.pushButton_2.clicked.connect(self.button2_clicked)
        self.pushButton_3.clicked.connect(self.button3_clicked)

        self.radioButton.toggled.connect(self.onClicked)
        self.radioButton_2.toggled.connect(self.onClicked)
        self.radioButton_3.toggled.connect(self.onClicked)
        self.radioButton_4.toggled.connect(self.onClicked)
        self.radioNumber = self.sender()
        self.dev_pid = 0
        self.start = 0
        self.sampleRate = 16000
        self.audioType = 'wav'

    def onClicked(self):
        self.radioNumber = self.sender()
        if self.radioNumber.isChecked():
            self.dev_pid = dev[self.radioNumber.text()]
            # print(self.dev_pid)
            print("You live in " + self.radioNumber.text())

    def button1_clicked(self):
        if self.dev_pid == 0:
            self.textBrowser.setText("您还没有选择语言")
        else:
            print("开始录制")
            self.textBrowser.setText("正在录制！！！")
            self.start = 1  # 开始录制
            if 1:  # 多线程
                t = threading.Thread(target=self.record, )
                t.start()
            else:
                self.record()

    def button2_clicked(self):
        if self.start == 0:
            self.textBrowser.setText("现在还没有开始录制")
        else:
            self.start = 0
            self.textBrowser.setText("录制结束！！！")
            print("录制结束")

    # 录制音频
    def record(self):
        pa = pyaudio.PyAudio()
        # 打开声卡，设置 采样深度为16位、声道数为1、采样率为16、输入、采样点缓存数量为2048
        stream = pa.open(format=pyaudio.paInt16, channels=1, rate=self.sampleRate, input=True, frames_per_buffer=2048)
        record_buf = []

        for i in range(0, 8 * 30):  # 支持识别的音频最大30s
            if self.start == 0:
                break
            audio_data = stream.read(2048)  # 读出声卡缓冲区的音频数据
            record_buf.append(audio_data)  # 将读出的音频数据追加到record_buf列表

        stream.stop_stream()
        stream.close()
        pa.terminate()

        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.sampleRate)
        wf.writeframes("".encode().join(record_buf))
        wf.close()

    def button3_clicked(self):
        if self.start == 1:
            self.textBrowser.setText("正在录制，无法识别！！！")
            print("正在录制，无法识别！！！")
        else:

            # self.textBrowser.setText("开始识别！！！")   # 加上这句怎么都看不出来效果，不知道原因

            result = self.recogntion()
            if result['err_no'] == 0:
                self.textBrowser.setText("识别结果： " + result['result'][0])
                print("you said: " + result["result"][0])
            else:
                self.textBrowser.setText('Recognition Eror, Error number is ' + str(result['err_no']))
                print("failed!!!")

    # 识别音频
    def recogntion(self):
        with open(self.filename, 'rb') as f:
            audio_data = f.read()

        result = self.client.asr(audio_data, self.audioType, self.sampleRate, {
            'dev_pid': self.dev_pid,
        })
        print(result)

        return result


def main():
    APP_ID = '25426975'
    API_KEY = 'besIFO02GHosUHIUdeeYAOLL'
    SECRET_KEY = '4WL6EbLp821uC1oUNKQZLKWWOMot2zGt '

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    outfile = "./audio/16k.wav"

    app = QApplication(sys.argv)
    form = ExampleApp(outfile, client)
    form.show()

    app.exec_()


if __name__ == '__main__':
    main()
