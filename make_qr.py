import qrcode
import os

url = "https://routine-khdj6xfuiumnnn7uibanre.streamlit.app/?code=mysecret2026"

img = qrcode.make(url)

save_path = os.path.join(os.getcwd(), "streamlit_qr.png")
img.save(save_path)

print("保存先:", save_path)
print("QRコード作成完了")