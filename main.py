import os
import re

def delete_duplicate_files():
    # 実行ファイルがあるディレクトリを取得
    target_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(target_dir)
    
    # 実行中のスクリプト自身は削除対象から除外
    script_name = os.path.basename(__file__)

    # 重複ファイルを示すパターン (例: "ファイル名 (1).txt" や "ファイル名（1）.txt")
    # \s? はスペース（半角/全角）があるかないか
    # [\(\（] は半角または全角の開始カッコ
    # \d+ は1文字以上の数字
    # [\)\）] は半角または全角の閉じカッコ
    duplicate_pattern = re.compile(r".+\s?[$$\（]\d+[$$\）]\.[^.]+$")

    deleted_count = 0

    print(f"スキャン開始: {target_dir}\n")

    for filename in files:
        # スクリプト自身はスキップ
        if filename == script_name:
            continue

        # ファイル名が重複パターンにマッチするかチェック
        if duplicate_pattern.match(filename):
            file_path = os.path.join(target_dir, filename)
            
            try:
                # ファイルであることを確認して削除
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"削除しました: {filename}")
                    deleted_count += 1
            except Exception as e:
                print(f"エラー発生 ({filename}): {e}")

    print(f"\n完了: 合計 {deleted_count} 個のファイルを削除しました。")

if __name__ == "__main__":
    # 実行前に確認を入れる
    print("【注意】このフォルダ内の (1) などが付いた重複ファイルを削除します。")
    ans = input("実行しますか？ (y/n): ")
    
    if ans.lower() == 'y':
        delete_duplicate_files()
    else:
        print("キャンセルしました。")
