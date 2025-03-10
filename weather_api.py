import requests
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Flaskアプリの作成
app = Flask(__name__)
CORS(app)  # CORSを有効化（他のドメインからのアクセスを許可）

# .envファイルからAPIキーを読み込む
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
print(f"🌍 読み込んだ API_KEY: {API_KEY}")  # APIキーが正しく読み込まれているか確認

def get_coordinates(city):
    """
    都市名をもとに緯度・経度を取得する関数。
    OpenWeatherのジオコーディングAPIを使用する。

    Args:
        city (str): 検索する都市名
    
    Returns:
        tuple: (緯度, 経度) のタプル。取得に失敗した場合は (None, None) を返す。
    """
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(geo_url)
    geo_data = response.json()

    if response.status_code == 200 and geo_data:
        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]
        return lat, lon
    else:
        return None, None
    
@app.route('/weather', methods=['GET'])
def get_weather_by_coordinates():
    """
    緯度・経度を指定して天気情報を取得するAPIエンドポイント。
    
    クエリパラメータ:
        lat (str): 緯度
        lon (str): 経度

    Returns:
        JSONレスポンス: 天気情報またはエラーメッセージ
    """
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    # 必要なパラメータがない場合はエラーを返す
    if not lat or not lon:
        return jsonify({"error": "緯度・経度が指定されていません"}), 400

    # OpenWeather APIを使用して天気情報を取得
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"
    response = requests.get(weather_url)
    weather_data = response.json()

    if response.status_code == 200:
        return jsonify({
            "都市": weather_data["name"],
            "天気": weather_data["weather"][0]["description"],
            "気温 (°C)": weather_data["main"]["temp"],
            "湿度 (%)": weather_data["main"]["humidity"],
            "風速 (m/s)": weather_data["wind"]["speed"]
        })
    else:
        return jsonify({"error": "天気情報を取得できませんでした"}), 400


@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    """
    都市名を指定して天気情報を取得するAPIエンドポイント。
    
    Args:
        city (str): 取得したい都市名

    Returns:
        JSONレスポンス: 天気情報またはエラーメッセージ
    """
    lat, lon = get_coordinates(city)

    # 座標を取得できなかった場合
    if lat is None or lon is None:
        return jsonify({"error": "都市の座標を取得できませんでした"}), 400
    
    # OpenWeather APIを使用して天気情報を取得
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"
    response = requests.get(weather_url)
    weather_data = response.json()

    if response.status_code == 200:
        return jsonify({
            "都市": weather_data["name"],
            "天気": weather_data["weather"][0]["description"],
            "気温 (°C)": weather_data["main"]["temp"],
            "湿度 (%)": weather_data["main"]["humidity"],
            "風速 (m/s)": weather_data["wind"]["speed"]
        })
    else:
        return jsonify({"error": "天気情報を取得できませんでした"}), 400

if __name__ == '__main__':
    # Flaskアプリを起動（デバッグモード有効）
    # ホストを 0.0.0.0 に設定して、外部からもアクセス可能にする
    app.run(host="0.0.0.0", port=5000, debug=True)
