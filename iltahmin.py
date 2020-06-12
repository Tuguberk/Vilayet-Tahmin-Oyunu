import random


class Tahmin:
    sehirler = ["ANKARA", "IZMIR", "ISTANBUL", "BURSA", "ANTALYA", "KONYA", "GAZIANTEP", "ESKIŞEHIR", "MUĞLA", "MERSIN",
                "KAHRAMANMARAŞ", "VAN", "ŞANLIURFA", "SIVAS", "SAMSUN", "KIRIKKALE", "KAYSERI", "BATMAN", "BITLIS",
                "KOCAELI", "NIĞDE", "NEVŞEHIR", "SAKARYA", "BOLU", "TRABZON", "RIZE", "TOKAT", "GIRESUN", "ORDU", "ARTVIN",
                "AYDIN", "DENIZLI", "BURDUR", "BALIKESIR", "MANISA", "KÜTAHYA", "ÇANKIRI", "ÇORUM", "YOZGAT", "ADANA",
                "OSMANIYE", "ERZURUM", "ERZINCAN", "KIRŞEHIR", "HATAY", "KILIS", "MARDIN", "ŞIRNAK", "HAKKARI", "AĞRI", "TUNCELI",
                "GÜMÜŞHANE", "BAYBURT", "BINGÖL", "MALATYA", "MUŞ", "KARS", "ZONGULDAK", "BILECIK"]

    def __init__(self):
        self.seçim = random.choice(Tahmin.sehirler)
        self.bulunan = ["-" for i in self.seçim]
        self.kalanhak_harf = len(self.seçim)
        self.kalanhak_tahmin = 3
        self.kazanma = False
        print(
            self.seçim, "Test etmek için ekrana yazdırılır. Gerçek Oyunda Kaldırılmalıdır.")
        if self.oyna(self.bulunan):
            print("Oyunu Kazandınız!")
            self.kazanma = True
        else:
            print("Oyunu Kaybettiniz!")
            self.kazanma = False

    def __str__(self):
        return str(self.kazanma)

    def harf_yerlestirme(self, durum, harf):
        for i in range(len(self.seçim)):
            if harf == self.seçim[i]:
                durum[i] = harf
        return durum

    def oyna(self, durum):
        if list(self.seçim) != durum:
            print(*self.bulunan)
            print(
                f"Kalan Harf Hakkınız: {self.kalanhak_harf} --- Kalan Tahmin Hakkınız: {self.kalanhak_tahmin}")
            harf = input(
                "Lütfen bir harf giriniz..(Tahmin Yapmak için . koyunuz!):").upper()
            if len(harf) > 1:
                print("lütfen her seferinde 1 harf giriniz..")
            elif harf == ".":
                if self.kalanhak_tahmin == 0:
                    print("Tahmin Hakkınız Kalmamıştır!")
                else:
                    tahmin = input("Tahmininizi Yazınız: ").upper()
                    if tahmin == self.seçim:
                        durum = [i for i in self.seçim]
                    else:
                        print("Yanlış Tahmin!")
                        self.kalanhak_tahmin -= 1
            elif harf in self.seçim:
                durum = self.harf_yerlestirme(durum, harf)
            else:
                print("Malesef girdiğiniz harf {} şehir isminde yok".format(harf))
                self.kalanhak_harf -= 1
                if self.kalanhak_harf == 0:
                    print(
                        "Malesef hakkınız doldu bulamadınız seçtiğim şehir {} ".format(self.seçim))
                    return False
            if self.oyna(durum):
                return True
            else:
                return False
        return True


if __name__ == "__main__":
    puan = 0
    while True:
        print("İl Tahmin Oyununa Hoş Geldiniz! Puanınız:", puan)
        if bool(Tahmin()):
            puan += 10
