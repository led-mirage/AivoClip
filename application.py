# AivoClip
#
# アプリケーションクラス
#
# Copyright (c) 2024-2026 led-mirage
# このソースコードは MITライセンス の下でライセンスされています。
# ライセンスの詳細については、このプロジェクトのLICENSEファイルを参照してください。

import argparse
import sys, os
from tkinter import messagebox

from app_logging import get_logger, setup_logging
from settings import Settings
from aivoice import AIVoice

APP_NAME = "AivoClip"
APP_VERSION = "0.4.0"
COPYRIGHT = "Copyright 2024-2026 led-mirage"

SETTING_FILE = "settings.json"

logger = get_logger("application")

class Application:
    # コンストラクタ
    def __init__(self):
        self.speakers = None
        self.settings = None
        pass

    # 開始
    def start(self):
        self.set_dpi_awareness()

        parser = argparse.ArgumentParser(description=f"{APP_NAME} {APP_VERSION}")
        parser.add_argument("--setting", type=str, default=SETTING_FILE, help="設定ファイル名")
        args = parser.parse_args()

        self.print_apptitle()

        self.settings = Settings(args.setting)
        self.settings.load()

        try:
            AIVoice.init(self.settings.get_aivoice_install_path())
            self.speakers = AIVoice.get_speakers()
        except Exception:
            logger.exception("Failed to get speakers from A.I.VOICE")
            logger.info(f"{APP_NAME} {APP_VERSION} stopped because A.I.VOICE is unavailable")
            message = "A.I.Voice が利用できません"
            messagebox.showerror(f"{APP_NAME}", message)
            raise SystemExit(1)

        from main_window import MainWindow
        main_window = MainWindow(self)
        main_window.show()
        main_window.terminate()

    # 高DPIディスプレイ対応（文字がぼやけないようにする）
    def set_dpi_awareness(self):
        if os.name == "nt":
            try:
                from ctypes import windll
                # Windows 8.1以降のDPI意識設定
                windll.shcore.SetProcessDpiAwareness(1)
            except Exception:
                # 古いOSや環境で失敗してもアプリ自体は起動するように
                pass

    # タイトルを表示する
    def print_apptitle(self):
        print(f"----------------------------------------------------------------------")
        print(f" {APP_NAME} {APP_VERSION}")
        print(f"")
        print(f" {COPYRIGHT}")
        print(f"----------------------------------------------------------------------")
        print(f"")

if __name__ == "__main__":
    log_file_path = setup_logging()

    if log_file_path is not None:
        logger.info(f"{APP_NAME} {APP_VERSION} started")

    try:
        from application import Application
        app = Application()
        app.start()
    except Exception as err:
        logger.exception("Application failed")

        message = (
            "An unexpected error occurred while the application was running.\n\n"
            f"{type(err).__name__}: {err}"
        )
        try:
            from ctypes import windll
            windll.user32.MessageBoxW(None, message, APP_NAME, 0x10)
        except Exception:
            pass

        raise SystemExit(1)
    else:
        logger.info(f"{APP_NAME} {APP_VERSION} stopped normally")
