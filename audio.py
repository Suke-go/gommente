import ffmpeg

# 入力ファイルのパス
input_file = "yameteyo.mp4"

# 出力ファイルのパス
output_file = "yameteyo.wav"

# FFmpegを使用して変換と保存を実行
stream = ffmpeg.input(input_file)
stream = ffmpeg.output(stream, output_file)
ffmpeg.run(stream)

print(f"{input_file}を{output_file}に変換して保存しました。")