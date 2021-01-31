# rakuten-point-keiba

自動的に競馬、競輪などのウェブサイトから、楽天銀行の入出金して、楽天ポイントを貯めるプログラミングです。

◆環境
1. selenium and python3
2. Write your account and password to settings.json
3. For captcha, Tesseract is necessary https://digi.bib.uni-mannheim.de/tesseract/

◆Tesseract設定
1. 環境變數 → Path → C:\Program Files\Tesseract-OCR
2. 環境變數 → TESSDATA_PREFIX（新規）→ C:\Program Files\Tesseract-OCR\tessdata\
3. pip install pytesseract
4. pip install PILLOW
