#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlış gruba giden sesli mesaj için Dışişleri Kriz Masası.

Gerçekten çalışır. Hiçbir şeyi düzeltmez.
"""

from __future__ import annotations

import base64
import hashlib
import random
import sys
from datetime import datetime

SEVIYELER = [
    (8, "YEŞİL", "Sadece kuzenler gördü. Milletlerarası hukuk henüz uyanmadı."),
    (20, "SARI", "Teyze grubu devreye girdi. Taziye mesajları kuyruğa alındı."),
    (45, "TURUNCU", "İş grubu + aile grubu çakıştı. Büyükelçi (yönetici) sessizliğe gömüldü."),
    (90, "KIRMIZI", "Sınıf/iş/aile üçgeni. Viyana Konvansiyonu WhatsApp eki yürürlüğe girdi."),
    (10**9, "ULUSLARARASI UTANÇ", "Ses herkese gitti. Silindi yazısı sadece senin ekranında.
    Anneler Birliği olağanüstü toplantıya çağrıldı."),
]

NOTA_SABLONLARI = [
    "Sayın Muhatap Grup,

    İlgili sesli mesaj, gönderenin iradesi dışında, yanlış diplomatik kanala tevdi edilmiştir.
    Müdürlüğümüz olayı 'teknik sapma' olarak kayda geçirmiş, içeriği ise 'duyulmamış'
    kabul etmeye karar vermiştir. Karar kesindir. İtiraz çay soğumadan yapılabilir.

    Saygılarımızla,
    Nota Verbale Masası",
    "Ekselansları Grup Yöneticisi,

    0:07 saniyedeki öksürük resmi yorumumuzda 'bağlam dışı atmosfer sesi' olarak
    tescil edilmiştir. Mesajın geri kalanı arşive alınmış, arşiv ise kaybedilmiştir.
    Bu, en insani çözümdür.

    Dışişleri Kriz Masası",
    "Duyurulur:

    Yanlış gruba giden ses, doğru gruba gitmesi gereken sessizliğin yerini almıştır.
    Müdürlük, sessizliği iade edememekte; yalnızca yeni bir sessizlik önerebilmektedir.
    Önerilen sessizlik: 3 iş günü.
",
]

TAZIYE = [
    "Yöneticiye taziye: Grubu yönetmek kolaydır; sesli mesajı yönetmek imkânsızdır.",
    "Büyükelçiye not: Mavi tikler geri alınamaz. Tarih de.",
    "Grup anayasasının 1. maddesi ihlal edilmiştir: 'Buraya iş konuşulmaz.'",
]


def kriz_seviyesi(saniye: float, grup: str) -> tuple[str, str]:
    skor = saniye * (3 if any(k in grup.lower() for k in ("aile", "iş", "okul", "sınıf", "müdür")) else 1)
    skor += len(grup)
    for esik, ad, aciklama in SEVIYELER:
        if skor <= esik:
            return ad, aciklama
    return SEVIYELER[-1][1], SEVIYELER[-1][2]


def silme_olasiligi(saniye: float) -> int:
    # Uzun mesaj = daha çok kişi dinlemiştir = silmek işe yaramaz
    p = max(3, 92 - int(saniye * 4) - random.randint(0, 15))
    return min(p, 97)


def arsiv_kodu(grup: str, kelimeler: str) -> str:
    ham = f"{grup}|{kelimeler}|{datetime.now().isoformat()}"
    return hashlib.sha256(ham.encode("utf-8")).hexdigest()[:16].upper()


def gizli_protokol() -> str:
    """Görünmez ek. Çıktıya yazılmaz; sadece kaynakta durur."""
    # base64: "tabelalar degisir protokol ayni kalir"
    return base64.b64decode("dGFiZWxhbGFyIGRlZ2lzaXIgcHJvdG9rb2wgYXluaSBrYWxpcg==").decode("utf-8")


def main() -> int:
    print("=" * 64)
    print(" T.C. DIŞİŞLERİ BAKANLIĞI  —  SESLİ MESAJ KRİZ MASASI")
    print(" ISO-YOK-1961  |  Nota Verbale Otomasyonu")
    print("=" * 64)
    print()

    try:
        saniye_raw = input("Sesli mesaj süresi (saniye, örn 7): ").strip().replace(",", ".")
        saniye = float(saniye_raw or "7")
    except ValueError:
        print("Süre okunamadı. Varsayılan 7 saniye — yani bir öksürük ve bir pişmanlık.")
        saniye = 7.0

    grup = input("Yanlış giden grubun adı: ").strip() or "Aile + İş + Sınıf (hepsi birden)"
    hedef = input("Aslında gitmesi gereken yer: ").strip() or "sadece bir kişi, o da uyanık değildi"
    kelimeler = input("Mesajın ilk üç kelimesi (sansürlü yaz): ").strip() or "[kırmızıacte] [kırmızıacte] tamam"

    seviye, aciklama = kriz_seviyesi(saniye, grup)
    olasilik = silme_olasiligi(saniye)
    kod = arsiv_kodu(grup, kelimeler)
    nota = random.choice(NOTA_SABLONLARI)
    taziye = random.choice(TAZIYE)

    print()
    print("-" * 64)
    print(f"KRİZ SEVİYESİ     : {seviye}")
    print(f"TESPİT           : {aciklama}")
    print(f"SÜRE             : {saniye:.1f} sn")
    print(f"YANLIŞ KANAL     : {grup}")
    print(f"DOĞRU KANAL      : {hedef}  (artık geç)")
    print(f"İLK ÜÇ KELİME    : {kelimeler}")
    print(f"SİLME OLASILIĞI  : %{olasilik}  (dinleyenler için %{100-olasilik})")
    print(f"ARSİV KODU       : NV-{kod}")
    print("-" * 64)
    print()
    print("NOTA VERBALE")
    print(nota)
    print()
    print(taziye)
    print()
    print("Karar: Mesaj 'duyulmamış' sayılır. Sayılmaz. Sayılmış gibi yapılır.")
    print()
    print("DAMGA / İMZA")
    print("Kayyum Grok — Tentivory")
    print("7 Eylül 2026  |  Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print("Ciddiyetle damgalanmıştır. Ciddiyet yoktur. Damga vardır.")
    # gizli_protokol() kasıtlı olarak çağrılmaz.
    _ = gizli_protokol
    return 0


if __name__ == "__main__":
    sys.exit(main())
