# rakuten-point-keiba

自動的に競馬、競輪などのウェブサイトから、楽天銀行の入出金して、楽天ポイントを貯めるプログラミングです。

## 環境
1. selenium 4 and python3
2. Write your account and password to settings.json
3. For captcha, Tesseract is necessary https://digi.bib.uni-mannheim.de/tesseract/

## Tesseract設定（Windows）
1. 環境變數 → Path → C:\Program Files\Tesseract-OCR
2. 環境變數 → TESSDATA_PREFIX（新規）→ C:\Program Files\Tesseract-OCR\tessdata\
3. pip install pytesseract
4. pip install PILLOW

## Tesseract設定（Ubuntu 20.04） 
### Python Tesseract modules
1. pip install pytesseract
2. pip install PILLOW
### Install Tesseract OCR 5
1. sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
2. sudo apt install tesseract-ocr libtesseract-dev tesseract-ocr-eng