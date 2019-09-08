# Lovederic Voice Maker
## What's this?
ラブデリック系含むゲームの表現でよくある「何を喋ってるのか、何語かも分からないごちゃっとした音声」をなんとなく再現したいなぁ...という、完全に趣味だけで書いたプログラム。
## Usage
基本的にはオリジナルのwave音源をランダム時間で切り貼りして出力するということをやっているだけ。
入力元のwaveファイルを**test.wav**にし、以下を実行すれば同ディレクトリに**output.wav**が生成される。 
`$ python voice_resample.py`
## Reference
以下のサイトを参考にさせていただきました。
- 「Pythonの音声入出力」(https://qiita.com/yu_tailsfox/items/86380a0d4d016e1634f1)
- 「[備忘録]pythonのwaveモジュール」(https://qiita.com/bayachin/items/68f7659d31fa6c836317)
