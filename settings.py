# AivoClip
#
# アプリケーション設定クラス
#
# Copyright (c) 2024 led-mirage
# このソースコードは MITライセンス の下でライセンスされています。
# ライセンスの詳細については、このプロジェクトのLICENSEファイルを参照してください。

import json
import os
import threading

from aivoice import AIVoice

class Settings:
    FILE_VER = 1

    def __init__(self, setting_file_path):
        self._setting_file_path = setting_file_path
        self._lock = threading.Lock()
        self._init_member()

    def _init_member(self):
        self._speaker_id = "紲星 あかり"
        self._aivoice_install_path = AIVoice.DEFAULT_INSTALL_PATH

    # 話者名
    def get_speaker_id(self):
        with self._lock:
            return self._speaker_id

    def set_speaker_id(self, speaker_id):
        with self._lock:
            self._speaker_id = speaker_id

    # A.I.VOICE のインストールパス
    def get_aivoice_install_path(self):
        with self._lock:
            return self._aivoice_install_path
    
    def set_aivoice_install_path(self, install_path):
        with self._lock:
            self._aivoice_install_path = install_path

    # 設定ファイルを保存する
    def save(self):
        with self._lock:
            self._save_nolock()

    def _save_nolock(self):
        with open(self._setting_file_path, "w", encoding="utf-8") as file:
            setting = {}
            setting["file_ver"] = Settings.FILE_VER
            setting["speaker_id"] = self._speaker_id
            setting["aivoice_install_path"] = self._aivoice_install_path
            json.dump(setting, file, ensure_ascii=False, indent=4)

    # 設定ファイルを読み込む
    def load(self):
        if not os.path.exists(self._setting_file_path):
            self._init_member()
            self._save_nolock()
            return

        with self._lock:
            with open(self._setting_file_path, "r", encoding="utf-8") as file:
                setting = json.load(file)
                file_ver = setting.get("file_ver", 1)
                self._speaker_id = setting.get("speaker_id", self._speaker_id)
                self._aivoice_install_path = setting.get("aivoice_install_path", self._aivoice_install_path)
            return setting

        if file_ver < Settings.FILE_VER:
            self._save_nolock()
