
import pyqrcode
import tkinter as tk
from tkinter import messagebox
import os
#dosya kontrolu icin



def create_qr():
    url = url_entry.get() #kullanicinin girdigi url yi al
    if not url:
        messagebox.showerror("Hata, Lutfen gecerli/aktif bir URL giriniz: ")
        return


    #QRcode olusturma
    try:

        qr_code = pyqrcode.create(url)
        qr_code.svg('qrcode.svg',scale=5) #svg formatinda kaydet

        if os.path.exists('qrcode.svg'):
            messagebox.showinfo("Basarili, QR Code basariyla olusturuldu, kaydedildi! ")
        else:
            messagebox.showerror("Hata, Qr Kodu olusturulamadi! ")
    except Exception as e:
        messagebox.showerror("Hata",f"bir hataolustu:{e}")

# Ana pencereyi olustur
root = tk.Tk()
root.title("QR Code Creator")

#URL giris icin etiket ve giris kutusu
url_label = tk.Label(root, text ="Olusturmak Istedigin Site linkini gir: ")
url_label.pack(pady=10)

url_entry = tk.Entry(root,width =40)
url_entry.pack(pady= 5)

#QR kodu olusturma butonu

generate_button = tk.Button(root, text="Simdi Olustur", command=create_qr)
generate_button.pack(pady=20)
#Ana donguyu otomatik baslat
root.mainloop()


