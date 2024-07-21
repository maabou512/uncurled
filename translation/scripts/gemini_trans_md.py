### Gemini Translation script only for Mark Down file.
# Read whole md file and translate AT ONCE.
# Run by
# ```python gemini_trans_md.py [input_md_file] [output_translated_md_file]```
# Python 3.11.0(pyenv + venv)
# Note: you need to swtith venv and 
# set PYTHONPATH by ```source ../../scripts/settings.conf)```

import google.generativeai as genai
import sys
import time
import os



# API キーを設定(環境変数を持ってくる)
API_KEY=os.path.expandvars("$GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

## 入力ファイル名と出力ファイル名をチェック

## --------------------------------------------------
# Check if the first argument is provided
if len(sys.argv) < 2:
    print("Error: Please provide the first argument (filename1).")
    sys.exit(1)

# Check if the second argument is provided
if len(sys.argv) < 3:
    print("Error: Please provide the second argument (filename2).")
    sys.exit(1)

# Set the first argument to the variable f_name1
f_name1 = sys.argv[1]

# Set the second argument to the variable f_name2
f_name2 = sys.argv[2]
dir_name = os.path.dirname(f_name2)

if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created.")


# プロンプト準備

prompt = """
### 入力
* マークダウンファイルのテキスト
### 指示
あなたはITおよびOSS（オープンソースソフトウェア）の専門家です。入力されたテキストをを日本語に翻訳してください
### 条件
* マークダウン記法は維持すること
* 「である」調で翻訳すること
* 翻訳にあたってはそれ以前に翻訳した用語や表現を踏襲すること
## 出力（この先だけ表示）
"""

# モデルをインスタンス化
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# メイン処理
def main():
    # 入力ファイルと出力ファイルのパスを設定
    input_file_path  = f_name1
    output_file_path = f_name2
    
    # 入力ファイルを開く
    with open(input_file_path, 'r', encoding="utf-8") as input_file:
        text = input_file.read()
        # 出力ファイルを開く
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            result = generate_content(prompt,text)
            print(result)
            # 翻訳結果を書き込む
            output_file.write(result)

# 翻訳処理
def generate_content(prompt,text):
    request=prompt + text
    response = model.generate_content(request)
    return response.text

if __name__ == "__main__":
    main()


