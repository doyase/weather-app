# weather-app

1️⃣ プロジェクトの概要
markdown
コピーする
編集する
# 天気情報アプリ
このプロジェクトは、Flask + JavaScript を使用した天気情報アプリです。
ユーザーが都市名を入力するか、GPSを使用して現在地の天気を取得できます。
2️⃣ 使用技術
markdown
コピーする
編集する
## 使用技術
- **Python (Flask)**: APIサーバー
- **JavaScript (Fetch API)**: フロントエンド
- **HTML / CSS (Bootstrap)**: UIデザイン
- **OpenWeather API**: 天気データの取得
3️⃣ セットアップ方法（ローカル環境で動かす手順）
markdown
コピーする
編集する
## セットアップ手順

### 1. Flaskのセットアップ（バックエンド）
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
pip install -r requirements.txt
.env ファイルを作成し、以下の内容を追加:

env
コピーする
編集する
OPENWEATHER_API_KEY=あなたのAPIキー
Flaskサーバーを起動:

bash
コピーする
編集する
python app.py
4️⃣ 使い方
markdown
コピーする
編集する
## 使い方
1. 都市名を入力して「取得」ボタンを押すと、天気情報を取得できます。
2. 「📍 現在地の天気」ボタンを押すと、GPSを利用して現在地の天気を取得できます。
3. 過去に検索した都市は履歴として表示され、クリックすると再検索できます。
