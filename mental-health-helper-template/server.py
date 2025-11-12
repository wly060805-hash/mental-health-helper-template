# server.py
from flask import Flask, request, jsonify
import uuid
from datetime import datetime
import os

app = Flask(__name__)

# 模拟会话存储
SESSIONS = {}

@app.route('/api/start', methods=['POST'])
def start_conversation():
    data = request.json
    user_name = data.get("name", "朋友")
    session_id = str(uuid.uuid4())

    SESSIONS[session_id] = {
        "history": [],
        "phase": "chat",
        "created": datetime.now()
    }

    return jsonify({
        "session_id": session_id,
        "message": f"你好呀 {user_name}～我是你的心灵小助手 ❤️\n\n最近过得怎么样？可以和我说说吗？😊",
        "disclaimer": "💡 提示：本工具仅提供情绪支持，不能替代专业诊疗。"
    })

@app.route('/api/reply', methods=['POST'])
def get_reply():
    data = request.json
    session_id = data.get("session_id")
    user_input = data.get("message", "").strip()

    if not session_id or session_id not in SESSIONS:
        return jsonify({"error": "会话无效或已过期"}), 400

    # 简化回复（真实版本会调用 Qwen API）
    reply_text = "谢谢你告诉我这些。我在这里倾听你，你并不孤单。🌼"

    # 检查是否提到测试
    if "测试" in user_input:
        reply_text = "你想做个心理状态小测评吗？我们可以一起完成一个简单的自评量表哦～"

    SESSIONS[session_id]["history"].append({"role": "user", "content": user_input})
    SESSIONS[session_id]["history"].append({"role": "assistant", "content": reply_text})

    return jsonify({"reply": reply_text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
