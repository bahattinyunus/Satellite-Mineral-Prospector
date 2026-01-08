# 🌈 Spektral İmzalar ve İndeks Rehberi

## Maden Keşfinin Fiziği
Mineraller elektromanyetik radyasyonla benzersiz şekillerde etkileşime girer. Farklı dalga boylarında (Görünür, Yakın Kızılötesi, Kısa Dalga-Kızılötesi) yansımayı ölçerek, cevher yataklarıyla ilişkili belirli kristal kafes yapılarını tanımlayabiliriz.

### 1. Demir Oksitler (Gosanlar)
**Hedef**: Hematit ($\rm Fe_2O_3$), Götit ($\rm FeO(OH)$), Jarosit.
**Spektral Özellik**: Mavi/UV'de ($\sim 0.4 \mu m$) güçlü emilim ve Kırmızı/NIR'de ($\sim 0.7-1.0 \mu m$) yüksek yansıma.
**İndeks**: `Kırmızı / Mavi`
- **Sentinel-2**: Bant 4 / Bant 2
- **Yorum**: Yüksek değerler, genellikle sülfür yataklarının üzerinde bulunan demir şapkaların (gosanlar) varlığını gösterir.

### 2. Kil Mineralleri (Hidrotermal Alterasyon)
**Hedef**: Kaolinit, Alunit, Montmorillonit (Fillik/Arjilik alterasyon).
**Spektral Özellik**: Al-OH bağlarının titreşim süreçlerinin neden olduğu SWIR aralığında ($\sim 2.1 - 2.2 \mu m$) benzersiz emilim çifti.
**İndeks**: `SWIR1 / SWIR2`
- **Sentinel-2**: Bant 11 ($\sim 1.6 \mu m$) / Bant 12 ($\sim 2.2 \mu m$)
- **Yorum**: Yüksek değerler, porfiri bakır ve epitermal altın için önemli bir vektör olan yoğun hidrotermal alterasyonu düşündürür.

### 3. Demirli Mineraller
**Hedef**: Klorit, Epidot, Amfiboller (Propilitik alterasyon).
**İndeks**: `SWIR2 / NIR` + `Kırmızı / Mavi` varyantları.
- **Sentinel-2**: Bant 12 / Bant 8 (Basitleştirilmiş)
- **Yorum**: Genellikle çekirdek cevher gövdesine uzak daha geniş alterasyon bölgelerini haritalar.

---

## Maskeleme Stratejisi

### Bitki Örtüsü (NDVI)
Bitkiler NIR'de (Klorofil) muazzam bir yansıma artışına sahiptir. Bu, mineral sinyallerini baskılayabilir.
- **Formül**: $(NIR - Kırmızı) / (NIR + Kırmızı)$
- **Mantık**: Eğer $NDVI > 0.3$ ise, yanlış pozitifleri önlemek için piksel maskelenir (yoğun bir orman bir bakır madeni değildir).

---
*Referans: USGS Spektral Kütüphanesi & ESA Sentinel-2 Kullanıcı El Kitabı.*
