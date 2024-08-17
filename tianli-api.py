import flask, g4f
from flask import request, jsonify, Flask

app = Flask(__name__)

@app.route('/tianli-api', methods=['GET', 'POST'])
def tianli_api():
    data=request.json
    headers=request.headers
    try:
        content=data['content']
        key=data['key']
        title=data['title']
        author=data['author']
        if key=='sk-114514':
            result=g4f.ChatCompletion.create(
                model=g4f.models.gpt_4o,
                messages=[
                    {"role": "system", "content": "你是一个名为Sunday的文章助手，请根据文章内容生成摘要"},
                    {"role": "user", "content": f"文章内容：{content}，请尽量简短得生成摘要，并使用与文章内容相同的语言"}
                ],
                stream=False
            )
            return jsonify({'summary': result})
    except:
        return jsonify({'error': 'Invalid request'}), 400
