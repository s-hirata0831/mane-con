<h2 align="center">
    マネコン
</h2>

<div align="center">
    <img src="https://github.com/s-hirata0831/mane-con/blob/main/doc/%E3%83%9E.png?raw=true">
</div>

## OverView

高専生のモテたい！  
↓  
モテるためには服が必要  
↓  
おしゃれな服屋を商店街に呼びこもう！  
↓  
せや！空き店舗の多い書店街の一つを借りて複数店で使い回せばええやん！  
↓  
企業誘致と市場調査，実際に企業が店舗を使う際のウェブアプリ作ったろ！

[スライドはここから見れます。](https://docs.google.com/presentation/d/e/2PACX-1vR1e5fXo759bO0ojsRExOcqqWY-WSJFtWaDxA13EoD0lXOGpQ_u_eG8FoLB4mjlwNdYDCwdyPcLhma5/embed?start=false&loop=false&delayms=3000)

## Usage

実際の構成は上記リンクにあるのスライドを参照してください。  
ウェブアプリの動作の Gif を下に載せておきます。

<div align="center">
    <img src="https://github.com/s-hirata0831/mane-con/blob/main/doc/%E5%8B%95%E4%BD%9C%E3%81%AE%E6%A7%98%E5%AD%90.gif?raw=true">
</div>

ここに乗ってるコードは今までに作ったものから流用しているものもいくつかあったり，GPT 先生に頼った部分もいくつかあります。  
動けばよし！精神で作ったので，クレームは一切受け付けておりませので悪しからずご了承くださいませ。  
構成を少し話しておくと，

- form  
  GAS で自動的にフォームを作成，情報収集するプログラムが入ってます。
- httpServer  
  Arduino からシリアル通信を経由して取得したデータをスライスして格納し，Flask に POST するところのプログラム。  
  dataClient.py がシリアル通信取得からスライスして格納。  
  dataServer.py が格納された情報を Flask に POST。
- webApp  
  Flask で構築したウェブアプリ。  
  温湿度は html 内部に書いた JavaScript で毎秒 http.server に対して GET リクエストを送っている。  
  スタイルは tailwindCSS で当てたので自分で書いたところは一切ない。
- その他  
  node_modules→TailwindCSS 関連  
  ledOn.py→GPIO 制御しようとして作ったけど放置したやつ

## Author

MaizuruRedBrick ハッカソン(#舞鶴ハッカソン)で製作されました。  
最優秀賞もらって嬉しー！
