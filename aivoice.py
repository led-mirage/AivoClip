# AivoClip
#
# A.I.VOICE制御用クラス
#
# Copyright (c) 2024 led-mirage
# このソースコードは MITライセンス の下でライセンスされています。
# ライセンスの詳細については、このプロジェクトのLICENSEファイルを参照してください。

import os
import threading
import time
from typing import List

import clr

class AIVoice:
    DEFAULT_INSTALL_PATH = "%ProgramW6432%/AI/AIVoice/AIVoiceEditor/AI.Talk.Editor.Api.dll"

    _install_path = DEFAULT_INSTALL_PATH
    _tts_control = None

    # 初期化する
    @classmethod
    def init(cls, install_path: str) -> None:
        program_dir = os.getenv("ProgramW6432")
        cls._install_path = install_path.replace("%ProgramW6432%", program_dir)
        cls.run_aivoice()

    # A.I.VOICEが起動していなかったら起動して接続する
    @classmethod
    def run_aivoice(cls) -> None:
        if os.path.isfile(cls._install_path):
            if cls._tts_control is None:
                clr.AddReference(cls._install_path)
                from AI.Talk.Editor.Api import TtsControl, HostStatus

                tts_control = TtsControl()
                host_name = tts_control.GetAvailableHostNames()[0]
                tts_control.Initialize(host_name)        
                if tts_control.Status == HostStatus.NotRunning:
                    tts_control.StartHost()
                tts_control.Connect()
                cls._tts_control = tts_control

    # 使用可能な話者の名前を取得する
    @classmethod
    def get_speakers(cls) -> List[str]:
        cls.run_aivoice()
        try:
            tts_control = cls._tts_control
            tts_control.Connect()
            speakers: List[str] = []
            for voice in tts_control.VoicePresetNames:
                speakers.append(voice)
            return speakers
        except Exception as err:
            cls._tts_control = None
            print(err)
            return None

    # 話す
    @classmethod
    def talk(cls, voice_name: str, text: str, stop_event: threading.Event = None) -> None:
        cls.run_aivoice()
        try:
            tts_control = cls._tts_control
            tts_control.Connect()
            tts_control.CurrentVoicePresetName = voice_name
            tts_control.Text = text
            play_time = tts_control.GetPlayTime()
            tts_control.Play()
            if stop_event is None:
                time.sleep((play_time + 500) / 1000)
            else:
                loop_num = int((play_time + 500) / 100)
                for i in range(loop_num):
                    if stop_event.is_set():
                        tts_control.Stop()
                    else:
                        time.sleep(0.1)
        except Exception as err:
            cls._tts_control = None
            print(err)
            raise
