# Speech-recognition
- 基于百度的语音识别，python3.8(conda)+pyaudio+pyqt+baidu-aip


- 百度有面向python的语音识别框架，用pip 直接安装

  ```python
  pip install baidu-aip
  ```

- 我环境全部的包都在`requirements.txt`里，用下面命令即可安装所需要的依赖

  ```
  pip install -r requirements.txt
  ```

- 环境没有问题后，在百度智能云完成登录，在控制台创建一个应用，获得自己的APP_ID,API_KEY,SECRET_KEY。

​		在下面填入自己的 APP_ID,API_KEY,SECRET_KEY后，能运行即可

```python
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





