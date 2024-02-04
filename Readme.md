# <img src="image/application.ico" width="48"> AivoClip

Copyright (c) 2024 led-mirage

## 概要

クリップボードに貼り付けられたテキストを A.I.VOICE で読み上げるアプリです。

[VoivoClip](https://github.com/led-mirage/VoivoClip) の A.I.VOICE 版です。

## スクリーンショット

<img width="188" alt="screenshot" src="https://github.com/led-mirage/AivoClip/assets/139528700/1f42be6b-7feb-4cfa-aa6a-23b0d5a5adf1">

https://github.com/led-mirage/AivoClip/assets/139528700/afeaf908-8bdd-4d31-b873-6473affa555d

## 機能

- クリップボード監視の開始と停止
- キャラクター選択
- リピート
- 設定値の自動保存

## 動作確認環境

- Windows 11 Pro 23H2
- Python 3.12.0
- A.I.VOICE Editor 1.4.9.0

## 実行方法

### 🛩️ 実行ファイル（EXE）を使う場合

#### 1. プロジェクト用のフォルダの作成

任意の場所にプロジェクト用のフォルダを作成してください。

#### 2. アプリのダウンロード

以下のリンクから AivoClip.ZIP をダウンロードして、作成したフォルダに展開してください。

https://github.com/led-mirage/AivoClip/releases/tag/v0.2.0

#### 3. 実行

A.I.VOICEを起動してから AivoClip.exe または AivoClipNC.exe をダブルクリックすればアプリが起動します。  
AivoClip.exe はコンソールも一緒に起動するバージョンで、AivoClipNC.exe はコンソールが起動しないバージョンです。  
※A.I.VOICEが起動していない状態でアプリを開始すると、自動的にA.I.VOICEを起動しようと試みます。

### 🛩️ Pythonで実行する場合

#### 1. プロジェクト用のフォルダの作成

任意の場所にプロジェクト用のフォルダを作成してください。

#### 2. ターミナルの起動

ターミナルかコマンドプロンプトを起動して、作成したプロジェクトフォルダに移動します。

#### 3. ソースファイルのダウンロード

ZIPファイルをダウンロードして作成したフォルダに展開してください。  
または、Gitが使える方は以下のコマンドを実行してクローンしてもOKです。

```bash
git clone https://github.com/led-mirage/AivoClip.git
```

#### 4. ライブラリのインストール

以下のコマンドを実行して必要なライブラリをインストールします。

```bash
pip install -r requirements.txt
```

#### 5. 実行

A.I.VOICE を起動したのち、以下のコマンドを実行するとアプリが起動します。  
※A.I.VOICEが起動していない状態でアプリを開始すると、自動的にA.I.VOICEを起動しようと試みます。

```bash
python application.py
```

## 設定

### ⚙️ アプリケーション設定ファイル（オプション）

`settings.json`ファイルにはこのアプリの設定情報が記載されています。

#### ✨ speaker_id（既定値 紲星 あかり）

A.I.VOICEのキャラクター名（プリセット名）を記載します。アプリのGUIで設定できます。

#### ✨ aivoice_install_path（既定値 %ProgramW6432%/AI/AIVoice/AIVoiceEditor/AI.Talk.Editor.Api.dll）

A.I.VOICEを自動起動するために使用します。A.I.VOICEのDLLファイルのパスを記載してください。A.I.VOICEを既定の場所にインストールした場合は変更する必要はありません。別の場所にインストールした場合はこの値を変更してください。

#### ✨ wavefile_outdir（既定値 空文字列）

読み上げた音声を自動保存するディレクトリを指定します。空文字列の場合はファイルは保存されません。

## 使用しているライブラリ

### 🔖 pyperclip 1.8.2 

ホームページ： https://github.com/asweigart/pyperclip/tree/master  
ライセンス：[BSD 3-Clause "New" or "Revised" License](https://github.com/asweigart/pyperclip/blob/master/LICENSE.txt)

### 🔖 Pillow 10.2.0

ホームページ： https://python-pillow.org/  
ライセンス：[HPND License](https://raw.githubusercontent.com/python-pillow/Pillow/main/LICENSE)

### 🔖 pythonnet 3.0.3

ホームページ： https://github.com/pythonnet/pythonnet/  
ライセンス：[MIT License](https://github.com/pythonnet/pythonnet/blob/master/LICENSE)

## ライセンス

© 2024 led-mirage

本アプリケーションは [MITライセンス](https://opensource.org/licenses/MIT) の下で公開されています。詳細については、プロジェクトに含まれる LICENSE ファイルを参照してください。

## バージョン履歴

### 0.1.0 (2024/01/07)

- ファーストリリース

### 0.2.0 (2024/02/04)

- 音声ファイル（WAVEファイル）を自動保存する機能を追加
- ローカルPCでビルドしたをpyinstaller使用するよう変更（誤検知対策）
- VOICEVOX 0.16.1で動作確認
