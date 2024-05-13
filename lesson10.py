"""
Task bank sistemilə bağlıdı. 

İlk classımızda bizim hesab nömrəsi (int) və balans argumentlərimiz olacaq.
Metod olaraq 3 fərqli metoddan istifadə edəcəyik Balansı artırmaq,  Pul çıxarmaq  və balansı göstərmək üçün metodlar.
İkinci classımız isə kreditlə bağlıdır. İlk classımızı bu classa inheritance eliyəcəyik və  super initdən  istifadə edəcəyik.   Bu classda bizim 2 metodumuz olacaq. Kredit vermək və kredit ödənişi. Bu səbəbdən classımızın əlavə kimi 1 argumenti olacaq.                                                        Kredit götürüləcək məbləğ. Kredit sadəcə 1 il müddəti üçündür və faiz yoxdur (kreditinməbləği / 12=aylıq ödəniş).

"""






# ----------------Home Task  METHOD 1 ----------------------- 




class BankHesabi:



    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans


    def pul_cixar(self, mebleq):
        if self.balans >= mebleq:
            self.balans -= mebleq
            print(f"{mebleq} AZN çıxarıldı. Yeni balansınız: {self.balans} AZN")
        else:
            print("Balansınız kifayət qədər deyil.")


    def balans_goster(self):
        print(f"Balansınız: {self.balans} AZN")


    def balans_artir(self, mebleq):
        self.balans += mebleq
        print(f"Balansınız {mebleq} AZN artırıldı. Yeni balansınız: {self.balans} AZN")





class Kredit(BankHesabi):
    def __init__(self, hesab_nomresi, balans, kredit_mebli):
        super().__init__(hesab_nomresi, balans)
        self.kredit_mebli = kredit_mebli

    def kredit_odenisi(self):
        aylıq_odenis = self.kredit_mebli / 12
        self.balans -= aylıq_odenis
        print(f"Kredit ödənişi olan {aylıq_odenis:.2f} AZN  balansdan çıxarıldı. Yeni balansınız: {self.balans} AZN")


    def kredit_ver(self):
        self.balans += self.kredit_mebli
        print(f"{self.kredit_mebli} AZN kredit verildi. Yeni balansınız: {self.balans} AZN")


# Hesab obyektini yaratmaq
bank_hesabi = BankHesabi(123456, 1000)
bank_hesabi.balans_goster()
bank_hesabi.balans_artir(500)
bank_hesabi.pul_cixar(200)
bank_hesabi.balans_goster()

# Bank Hesabı Kredit obyektini yaratmaq
kredit_hesabi = Kredit(654321, 2000, 10000)
kredit_hesabi.balans_goster()
kredit_hesabi.kredit_ver()
kredit_hesabi.balans_goster()
kredit_hesabi.kredit_odenisi()
kredit_hesabi.balans_goster()

