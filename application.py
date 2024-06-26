# AivoClip
#
# アプリケーションクラス
#
# Copyright (c) 2024 led-mirage
# このソースコードは MITライセンス の下でライセンスされています。
# ライセンスの詳細については、このプロジェクトのLICENSEファイルを参照してください。

import argparse
import sys
from tkinter import messagebox

from settings import Settings
from aivoice import AIVoice

APP_NAME = "AivoClip"
APP_VERSION = "0.3.2"
COPYRIGHT = "Copyright 2024 led-mirage"

SETTING_FILE = "settings.json"

class Application:
    # コンストラクタ
    def __init__(self):
        self.speakers = None
        self.settings = None
        pass

    # 開始
    def start(self):
        parser = argparse.ArgumentParser(description=f"{APP_NAME} {APP_VERSION}")
        parser.add_argument("--setting", type=str, default=SETTING_FILE, help="設定ファイル名")
        args = parser.parse_args()

        self.print_apptitle()

        self.settings = Settings(args.setting)
        self.settings.load()

        AIVoice.init(self.settings.get_aivoice_install_path())

        self.speakers = AIVoice.get_speakers()
        if self.speakers is None:
            message = "A.I.Voice が利用できません"
            print(message)
            messagebox.showerror(f"{APP_NAME}", message)
            sys.exit()

        from main_window import MainWindow
        main_window = MainWindow(self)
        main_window.show()
        main_window.terminate()
    
    # タイトルを表示する
    def print_apptitle(self):
        print(f"----------------------------------------------------------------------")
        print(f" {APP_NAME} {APP_VERSION}")
        print(f"")
        print(f" {COPYRIGHT}")
        print(f"----------------------------------------------------------------------")
        print(f"")

if __name__ == "__main__":
    from application import Application
    app = Application()
    app.start()
