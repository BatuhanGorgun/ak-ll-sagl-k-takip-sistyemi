import random
import sqlite3
import tkinter as tk
import tkinter.messagebox as messagebox




# Veritabanı bağlantısı
connection = sqlite3.connect('health_tracker.db')
cursor = connection.cursor()

# Tablo oluşturma
cursor.execute('''CREATE TABLE IF NOT EXISTS health_data
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  calories INTEGER,
                  steps INTEGER,
                  sleep_duration INTEGER,
                  heart_rate INTEGER)''')
connection.commit()


def save_calories():
    calories = calories_entry.get()

    if int(calories) > 2000:
        message_label.config(text="Günlük kalori ihtiyacınızı aştınız!", fg="black",bg="red")
    else:
        message_label.config(text="Kaloriler kaydedildi!", fg="white",bg="green")

    # Veriyi veritabanına kaydetme
    cursor.execute("INSERT INTO health_data (calories) VALUES (?)", (calories,))
    connection.commit()
    update_stats()


def save_steps():
    steps = steps_entry.get()

    if int(steps) < 10000:
        message_label.config(text="Günlük hedefin altındasınız!", fg="black",bg="red")
    elif int(steps) >10000: message_label.config(text="Bravo !!! Günlük hedefini aştın.", fg="black",bg="green")
    else: message_label.config(text="Adımlar kaydedildi!", fg="black",bg="green")



    cursor.execute("INSERT INTO health_data (steps) VALUES (?)", (steps,))
    connection.commit()
    update_stats()


def save_sleep_duration():
    sleep_duration = sleep_duration_entry.get()

    if int(sleep_duration) < 7:
        message_label.config(text="Yetersiz uyku sağlık sorunlarına sebep olabilir. Uyku düzeninizi düzeltmeniz önerilir.", fg="black",bg="orange")
    elif int(sleep_duration) > 10:
        message_label.config(text="Kalk uykucu! Günü kaçırıyorsun", fg="black",bg="orange")
    else:
        message_label.config(text="Uyku süresi kaydedildi!", fg="green")


    cursor.execute("INSERT INTO health_data (sleep_duration) VALUES (?)", (sleep_duration,))
    connection.commit()
    update_stats()


def save_heart_rate():
    heart_rate = heart_rate_entry.get()

    if int(heart_rate) < 60:
        message_label.config(text="Nabzınız çok düşük! Nabız ölçerin doğru takıldığını kontrol edin.", fg="black",bg="red")
    elif int(heart_rate) > 130:
        message_label.config(text="Nabzınız normalin üzerinde! Meditasyon yapmanız önerilir.", fg="black",bg="red")

    else:
        message_label.config(text="Nabzınız normal!", fg="black",bg="orange")


    cursor.execute("INSERT INTO health_data (heart_rate) VALUES (?)", (heart_rate,))
    connection.commit()
    update_stats()


def reset_data():
    # Tabloyu sıfırlama
    cursor.execute("DELETE FROM health_data")
    connection.commit()
    update_stats()
    message_label.config(text="Veriler sıfırlandı!", fg="black",bg="green")


def show_developers():
    messagebox.showinfo("Yapımcılar", "Yapımcılar:\n\n- Batuhan Görgün\n- Seymen Kayıkçı")


def enlighten_me():
    enlightening_texts = [
        "Yetişkin bir kadının günlük 2.7 litre, erkeğin ise 3.7 litre su içmelidir. Su içmeyi unutma! 😊",
        "Yetişkin bir insanın ortalama 7-8 saat uyuması gerekir.",
        "Kadınların günde yaklaşık 2 bin kaloriye, erkeklerin ise 2 bin 500 kalori alması önerilir.",
        "Biliyor muydun? İnsan beyninin hafıza kapasitesi, dört terabaytlık bir hard diskin kapasitesine eşittir.",
        "Vücudun kan kaynağı olmayan tek bölümü, gözdeki korneadır. Oksijeni doğrudan havadan alır.",
        "Beyinden gönderilen sinir sinyalleri, saatte 274 km hızla hareket eder.",
        "İnsan beyni, bir gün içerisinde dünyadaki tüm telefonların toplamından daha fazla elektrik sinyali üretir.",
        "İnsan kalbi, hayatı boyunca 182 milyon litre kan pompalar.",
        "Siz bu cümleyi okurken, vücudunuzda 50.000 hücre öldü ve yenileri ile değişti.",
        "İnsan bedenindeki kan damarlarının toplam uzunluğu, yaklaşık 100.000 km'dir.",
        "Vücut ısımızın yaklaşık yüzde 80'ini başımızdan kaybederiz. Soğuk havalarde bere takmayı unutmayın<3",
        "İnsan bedeninde kendi kendini iyileştiremeyen tek organ, diştir.O yüzden dişlerinizi fırçalayın",
        "İnsan bedenindeki kalsiyumun yüzde 99'u, dişlerde bulunur.",
    ]

    selected_text = random.choice(enlightening_texts)
    messagebox.showinfo("Beni Aydınlat", selected_text)



def update_stats():
    # Verileri veritabanından çekme
    cursor.execute("SELECT SUM(calories) FROM health_data")
    total_calories = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(steps) FROM health_data")
    total_steps = cursor.fetchone()[0] or 0

    stats_label.config(text="Adımlar: {}   Kaloriler: {}".format(total_steps, total_calories))


# GUI penceresi
window = tk.Tk()
window.title("Akıllı Sağlık Takip Sistemi")
window.geometry("500x500")
window.configure(bg="#1b2731")
# Kalori takibi
calories_label = tk.Label(window, text="Günlük Kalori:",bg="#ff9933")
calories_label.pack()
calories_entry = tk.Entry(window)
calories_entry.pack()
calories_button = tk.Button(window, text="Kaydet", command=save_calories,bg="#00cc00")
calories_button.pack()

# Adım takibi
steps_label = tk.Label(window, text="Günlük Adım:",bg="#ff9933")
steps_label.pack()
steps_entry = tk.Entry(window)
steps_entry.pack()
steps_button = tk.Button(window, text="Kaydet", command=save_steps,bg="#00cc00")
steps_button.pack()

# Uyku takibi
sleep_duration_label = tk.Label(window, text="Uyku Süresi:",bg="#ff9933")
sleep_duration_label.pack()
sleep_duration_entry = tk.Entry(window)
sleep_duration_entry.pack()
sleep_duration_button = tk.Button(window, text="Kaydet", command=save_sleep_duration,bg="#00cc00")
sleep_duration_button.pack()

# Nabız ölçümü i
heart_rate_label = tk.Label(window, text="Nabız:",bg="#ff9933")
heart_rate_label.pack()
heart_rate_entry = tk.Entry(window)
heart_rate_entry.pack()
heart_rate_button = tk.Button(window, text="Kaydet", command=save_heart_rate,bg="#00cc00")
heart_rate_button.pack()

# Verileri sıfırlama düğmesi
reset_button = tk.Button(window, text="Verileri Sıfırla", command=reset_data,bg="#ff1a1a")
reset_button.pack()

# Mesaj gösterme etiketi
message_label = tk.Label(window, text="")
message_label.pack()

# Yapımcı bilgileri düğmesi
developers_button = tk.Button(window, text="Yapımcılar", command=show_developers,bg="#ffcc00")
developers_button.place(x=430, y=5)

# Beni Aydınlat düğmesi
enlighten_button = tk.Button(window, text="Beni Aydınlat", command=enlighten_me,bg="#ff9933")
enlighten_button.place(x=10, y=470)

# İstatistik gösterge etiketi
stats_label = tk.Label(window, text="Adımlar: 0   Kaloriler: 0", bg="#ff9933", fg="black")
stats_label.pack()
def show_message_box():
    messagebox.showinfo("Teşekkürler", "Uygulamamızı kullandığınız için teşekkür ederiz,Uygulamamız geliştirilirler Düzenleyici olarak Pycharm, Dil olarak python ,Veritabanı olarak ise SQL lite 3 kullanılmıştır . Sağlıklı günler dileriz.")

def show_kaloriler_box():
    messagebox.showinfo("Kaloripedi","Tam Buğday Ekmeği 25g 63kcl                                                        Çavdar Ekmeği 25g  65kcl                                                           Beyaz Ekmek 25g kcl                                                                       İnek Sütü(Tam Yağlı) 200ml 110kcal                                                İnek Sütü (Yağsız) 200ml 93kcal                                               Süzme Peynir 30g 69kcal                                                             Beyaz Peynir(Yarım Yağlı İnek) 30g 60kcal                                        Yoğurt (Yağlı) 100ml 95kcal                                                         Elma 182g 1 orta boy  95kcal                                                          Armut 178g 1 orta boy 101kcal                                                           Portakal 130g 1 orta boy 62kcal                                                 Mandalina 76g 1 küçük boy 40kcl                                                     Muz 118g 1 orta boy 105 kcal                                                 Domates 123g 1 orta boy 22kcal                                                      Salatalık 100g 1 orta boy   15kcal                                                        Havuç 61g 1 orta boy  25kcal                                                 Fındık 15g 10-12 adet 100kcal                                                  Badem 17g 12-14 adet  97kcal                                                ayçiçeği yağı 5g 1 tatlı kaşığı  45kcal                                                      Zeytinyağı 5g 1 tatlı kaşığı 50kcal                                               Tereyağ 5g 1 tatlı kaşığı 36kcal                                                     Köfte 30g 1 yumurta kadar 59kcal                                                    Dana Antrikot 50g 1.5 yumurta kadar 82kcal                                Tavuk (Göğüs) 50g 60kcal                                                        Tavuk (But) 30g  69kcal                                                                     tavuk (kanat) 30g 70kcal                                                               Levrek 101g  125kcal                                                              Mercimek Çorbası 180g 99kcal                                               Tavuk Çorbası 180g 60kcal                                                          Peynirli omlet 130g 2 yumurta + 1 peynir 254kcal ")

# kaloripedi butonu
kaloriler_button = tk.Button(window, text="Kaloripedi", command=show_kaloriler_box, bg="#ffcc00")
kaloriler_button.place(x=5, y=50)
# Teşekkür et butonu
thank_button = tk.Button(window, text="Bilgilendirme", command=show_message_box, bg="#ffcc00")
thank_button.place(x=5, y=5)
# vki hesaplama
weight_label = tk.Label(window, text="Kilonuz (kg):", bg="#ff9933")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Boyunuz (cm):", bg="#ff9933")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # cm'yi metreye çevirme

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = "Vücut Kitle Endeksiniz: {:.2f}\n\n18.5 kg/m² 'nin altındasınız: İdeal kilonun altında".format(bmi)
    elif 18.5 <= bmi <= 24.9:
        result = "Vücut Kitle Endeksiniz: {:.2f}\n\n18.5 kg/m² ile 24.9 kg/m² arasındasınız: İdeal kiloda".format(bmi)
    elif 25 <= bmi <= 29.9:
        result = "Vücut Kitle Endeksiniz: {:.2f}\n\n25 kg/m² ile 29.9 kg/m² arasındasınız: İdeal kilonun üstünde".format(bmi)
    elif 30 <= bmi <= 39.9:
        result = "Vücut Kitle Endeksiniz: {:.2f}\n\n30 kg/m² ile 39.9 kg/m² arasındasınız: İdeal kilonun çok üstünde (obez)".format(bmi)
    else:
        result = "Vücut Kitle Endeksiniz: {:.2f}\n\n40 kg/m² üzerindesiniz: İdeal kilonun çok üstünde (morbid obez)".format(bmi)

    messagebox.showinfo("Vücut Kitle Endeksi", result)

# vki buttonu
bmi_button = tk.Button(window, text="Vücut Kitle Endeksi Hesapla", command=calculate_bmi, bg="#00cc00")
bmi_button.pack()



window.mainloop()

# sql bağlantısı kesen zamazingo
connection.close()



