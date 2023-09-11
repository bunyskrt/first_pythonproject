sorular = ("hangisi bir memelidir ? ",
           "en pahalı araba markası ? ",
           "kadınların en çok zevk aldıkları yer ? ",
           "insan vücüdunda kaç kemik vardır ? ",
           "canlı yaşamı hangi elemen olmasaydı oluşmazdı ? ")

seçenekler=(("A: kartal", "B: yunus", "C: yılan", "D: deve kuşu"),
              ("A: ford", "B: porsche", "C: maserati", "D: bugatti"),
              ("A: meme ucu", "B: ağız", "C: boyun", "D: klitoris"),
              ("A: 201", "B: 204", "C: 205", "D: 209"),
              ("A: azot", "B: helyum", "C: karbon", "D: oksijen"))

cevaplar = ("B", "D", "D", "D", "C")
tahminler = []
puan = 0
soru_num = 0

for soru in sorular:
    print("----------------------------")
    print(soru)
    for seçenek in seçenekler[soru_num]:
        print(seçenek)

    tahmin = input("Giriş (A, B, C, D): ").upper()
    tahminler.append(tahmin)
    if tahmin == cevaplar[soru_num]:
        puan += 1
        print("DOĞRU")
    else:
        print("YANLIŞ")
        print(f"{cevaplar[soru_num]} doğru cevap")
    soru_num += 1

print("----------------------------")
print("          SONUÇLAR          ")
print("----------------------------")

print("cevaplar : ", end="")
for cevap in cevaplar:
    print(cevap, end=" ")
print()

print("tahminler: ", end="")
for tahmin in tahminler:
    print(tahmin, end=" ")
print()

puan = (puan / len(sorular)*100)
print(f"Senin puanın : {puan}%")
