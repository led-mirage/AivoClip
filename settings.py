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
    FILE_VER = 3

    def __init__(self, setting_file_path):
        self._setting_file_path = setting_file_path
        self._lock = threading.Lock()
        self._init_member()

    def _init_member(self):
        self._speaker_id = "紲星 あかり"
        self._aivoice_install_path = AIVoice.DEFAULT_INSTALL_PATH
        self._wavefile_outdir = ""
        self._replacements = []

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

    # WAVEファイルの出力ディレクトリ
    def get_wavefile_outdir(self):
        with self._lock:
            return self._wavefile_outdir
        
    def set_wavefile_outdir(self, outdir):
        with self._lock:
            self._wavefile_outdir = outdir

    # 置換設定
    def get_replacements(self):
        with self._lock:
            return self._replacements
        
    def set_replacements(self, replacements):
        with self._lock:
            self._replacements = replacements

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
            setting["wavefile_outdir"] = self._wavefile_outdir
            setting["replacements"] = self._replacements
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
                self._wavefile_outdir = setting.get("wavefile_outdir", self._wavefile_outdir)
                self._replacements = setting.get("replacements", self._replacements)

        if file_ver < Settings.FILE_VER:
            self._save_nolock()
