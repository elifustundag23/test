from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver başlat
driver = webdriver.Chrome()

# Yargıtay kararları sayfasına git
driver.get("https://karararama.yargitay.gov.tr/#")

# Sayfanın yüklenmesini bekleyin
print("Sayfa yükleniyor... Lütfen bekleyin.")
time.sleep(5)  # Sayfanın yüklenmesi için bekleme

# Sayfanın tamamen yüklenip yüklenmediğini manuel kontrol edebilirsiniz
input("Sayfa yüklendiyse, 'Enter' tuşuna basın.")

try:
    # Arama kutusuna metin gir
    print("Arama kutusu bulunuyor...")
    search_box = driver.find_element(By.ID, "searchBox")  # Arama kutusunun ID'sini kontrol edin
    search_box.send_keys("mahkemesi")
    search_box.send_keys(Keys.RETURN)

    # Sonuçların yüklenmesini bekleyin
    print("Sonuçlar yükleniyor...")
    time.sleep(5)  # Sonuçların yüklenmesi için bekleme

    # Kararları bul
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")  # Tablo satırlarını bul

    # Satır sayısını kontrol et
    if len(rows) > 0:
        print(f"{len(rows)} karar bulundu.")  # Karar sayısını yazdır
    else:
        print("Hiç karar bulunamadı.")

    # Verileri konsola yazdırma
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        if len(columns) > 3:  # Satırda yeterli sütun olduğundan emin olun
            karar_no = columns[0].text.strip()
            mahkeme = columns[1].text.strip()
            tarih = columns[2].text.strip()
            baslik = columns[3].text.strip()

            # Veriyi konsola yazdır
            print(f"Karar No: {karar_no}")
            print(f"Mahkeme: {mahkeme}")
            print(f"Tarih: {tarih}")
            print(f"Başlık: {baslik}")
            print("-" * 40)  # Ayrıcı çizgi

    # Dosyaya yazma işlemi (isteğe bağlı olarak)
    with open('kararlar.txt', mode='w', encoding='utf-8') as file:
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            if len(columns) > 3:
                karar_no = columns[0].text.strip()
                mahkeme = columns[1].text.strip()
                tarih = columns[2].text.strip()
                baslik = columns[3].text.strip()

                # Dosyaya yazma
                file.write(f"Karar No: {karar_no}\nMahkeme: {mahkeme}\nTarih: {tarih}\nBaşlık: {baslik}\n\n")

    print("Veriler başarıyla dosyaya yazıldı.")

except Exception as e:
    print(f"Hata: {e}")

finally:
    # Tarayıcıyı kapat
    print("Tarayıcı kapanıyor...")
    driver.quit()
