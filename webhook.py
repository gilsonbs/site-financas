from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    os.system('/home2/monted69/asael.tech/financas/webhook.sh')
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)