from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # เปิดใช้งาน CORS สำหรับทุกแหล่งที่มา

@app.route('/get-line-profile-url', methods=['GET'])
def get_line_profile_url():
    line_id = "pkn_a"  # ใส่ Line ID ของคุณที่นี่
    line_url = f"https://line.me/ti/p/@{line_id}"
    return jsonify({'url': line_url})

if __name__ == '__main__':
    app.run(debug=True)
