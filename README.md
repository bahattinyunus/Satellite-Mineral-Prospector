# 🛰️ Satellite Mineral Prospector: İleri Seviye Uzaktan Algılama ve Jeolojik Keşif Platformu

> **Masterclass Edisyonu**: Yeni Nesil Jeolojik Keşifler ve Uydu Tabanlı Maden Arama Simülasyonu.

<div align="center">

![Banner](https://img.shields.io/badge/Durum-Aktif%20Geliştirme-success?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Teknoloji-Python_3.9%2B-blue?style=for-the-badge&logo=python)
![Lisans](https://img.shields.io/badge/Lisans-MIT_Açık_Kaynak-green?style=for-the-badge&logo=open-source-initiative)
![Sürüm](https://img.shields.io/badge/Sürüm-1.0.0_Kurumsal-orange?style=for-the-badge&logo=semantic-release)

</div>

---

## 🌍 Proje Vizyonu ve Genel Bakış

**Satellite Mineral Prospector**, geleneksel jeolojik saha çalışmalarının zorluklarını ve maliyetlerini, modern uydu teknolojisi ve hesaplamalı algoritmalarla aşmayı hedefleyen, son teknoloji bir **Uzaktan Algılama (Remote Sensing)** projesidir. Günümüzde maden arama faaliyetleri, geniş arazilerin fiziksel olarak taranmasını gerektiren ve yıllar sürebilen pahalı operasyonlardır. Bu proje, Avrupa Uzay Ajansı'nın (ESA) **Sentinel-2** ve NASA'nın **Landsat 8/9** uydu takımyıldızlarından elde edilen çok spektralli görüntüleri (Multi-spectral Imagery) kullanarak, bu süreci dijital ortama taşımakta ve otomatikleştirmektedir.

Projenin temel amacı, insan gözünün görebildiği görünür ışık spektrumunun (RGB) ötesine geçerek, minerallerin yaydığı benzersiz elektromanyetik imzaları analiz etmektir. Kısa Dalga Kızılötesi (SWIR) ve Yakın Kızılötesi (NIR) bantlarında yapılan hassas analizler sayesinde; **hidrotermal alterasyon zonları**, sülfürlü maden yataklarının habercisi olan **demir oksit şapkaları (gosanlar)** ve porfiri sistemlerin göstergesi olan **kil mineralleşmeleri** saniyeler içerisinde haritalanabilmektedir.

Bu depo, sadece işlevsel bir kod tabanı sunmakla kalmaz; aynı zamanda temiz kod prensipleri (Clean Code), modüler mimari, otomatik test süreçleri (CI/CD) ve kapsamlı dokümantasyon standartlarıyla, jeo-uzamsal yazılım mühendisliği alanında bir **"Masterclass"** niteliği taşımaktadır. Akademik araştırmacılardan maden şirketi yöneticilerine kadar geniş bir kitleye hitap eden bu platform, ölçeklenebilir ve sürdürülebilir bir keşif motoru olarak tasarlanmıştır.

---

## 🚀 Temel Teknik Yetenekler ve İnovasyonlar

### 🔬 Gelişmiş Spektral Analiz Motoru
Bu platformun kalbinde, pikseller düzeyinde çalışan yüksek performanslı bir analiz motoru yer almaktadır. Bu motor, literatürde kanıtlanmış jeolojik indeksleri (Band Ratios) matematiksel operatörler olarak uygular.
- **Otomatik İndeksleme**: Kullanıcıdan herhangi bir manuel parametre girişi beklemeksizin, sahnedeki her bir piksel için demir oksit, kil ve demirli mineral yoğunluklarını hesaplar.
- **Dinamik Maskeleme Algoritması**: Uydu görüntülerinde sıklıkla karşılaşılan ve "gürültü" olarak nitelendirilen bitki örtüsü, su kütleleri ve bulutlar, analiz sonuçlarını yanıltabilir. Geliştirdiğimiz entegre **NDVI (Normalized Difference Vegetation Index)** tabanlı maskeleme algoritması, bitki örtüsü yoğunluğunun belirli bir eşik değerin üzerinde olduğu (Örn: > 0.3) bölgeleri otomatik olarak tespit eder ve bu bölgeleri analiz dışı bırakır (Masking). Bu sayede, "yanlış pozitif" (False Positive) sonuçların önüne geçilerek sadece saf jeolojik yüzeylerin analizi sağlanır.

### 🎯 Hassas Hedef Tespiti ve Maden Grupları
Sistem, jeolojik oluşumların kimyasal yapısına göre üç ana kategoride tespit yapabilme yeteneğine sahiptir. Her bir kategori için optimize edilmiş spektral bant kombinasyonları kullanılır:

| Hedef Mineral Grubu | Jeolojik ve Ekonomik Anlamı | Kullanılan Teknik ve İndeks |
|---------------------|-----------------------------|-----------------------------|
| **Demir Oksitler** | Limonit, Götit ve Hematit gibi mineraller, genellikle bakır, kurşun ve çinko gibi sülfürlü cevherlerin yüzeydeki oksitlenmiş kalıntılarıdır. Bu "Demir Şapkalar", yeraltındaki zengin yatakların en güçlü habercisidir. | **Kırmızı / Mavi Oranı**: Demir minerallerinin mavi ışığı emip kırmızı ışığı yansıtma özelliğine dayanır. |
| **Kil Mineralleri** | Kaolinit, Alunit ve Montmorillonit, hidrotermal sıvıların kayaçları değiştirmesiyle (alterasyon) oluşur. Bu mineraller, Epitermal Altın ve Porfiri Bakır yataklarının merkezinde veya çevresinde yoğun olarak bulunur. | **SWIR1 / SWIR2 Oranı**: Kil minerallerinin 2.2 mikrometre dalga boyundaki karakteristik emilim özelliğini kullanır. |
| **Demirli Mineraller**| Klorit, Epidot ve Amfibol grubu mineraller, genellikle ana cevher yatağının daha dış çeperlerinde (Propilitik zon) gözlenir ve arama sahasının sınırlarını belirlemede kritiktir. | **SWIR2 / NIR Oranı**: Demirli silikatların spektral davranışlarını haritalar. |

### ⚡ Yüksek Performanslı ve Ölçeklenebilir Mimari
Büyük ölçekli uydu verilerini işlemek, yüksek hesaplama gücü ve bellek yönetimi gerektirir.
- **Optimize Edilmiş G/Ç (I/O)**: Proje, `RasterIO` kütüphanesinin gelişmiş yeteneklerini kullanarak, gigabaytlarca büyüklükteki GeoTIFF dosyalarını belleğe tamamen yüklemeden, "pencereleme" (windowing) veya optimize edilmiş okuma teknikleriyle işler. Bu, standart bir dizüstü bilgisayarda bile büyük sahnelerin analiz edilmesine olanak tanır.
- **Tam Modüler Tasarım**: Yazılım mimarisi, "Seperation of Concerns" (İlgi Alanlarının Ayrımı) ilkesine göre inşa edilmiştir. Veri okuma, önişleme, matematiksel analiz ve görselleştirme katmanları birbirinden tamamen izole edilmiştir. Bu sayede, sisteme yeni bir uydu sensörü (örneğin ASTER veya Hyperion) eklemek veya yeni bir analiz algoritması entegre etmek, mevcut kodu bozmadan kolayca yapılabilir.

---

## 🛠️ Teknik Mimari Detayları ve Çalışma Metodolojisi

Proje, yazılım mühendisliğinin en iyi uygulamaları olan **SOLID prensipleri** ve **Temiz Mimari** yaklaşımıyla geliştirilmiştir. Verinin ham halden işlenmiş bilgiye dönüşüm süreci titizlikle tasarlanmış bir "Pipeline" (Boru Hattı) üzerinden gerçekleşir:

1.  **Veri Alımı ve Standardizasyon (Data Ingestion)**: Farklı kaynaklardan gelen ham uydu bantları (JPEG2000 veya GeoTIFF formatında) sisteme alınır. Meta veriler (projeksiyon, koordinat sistemi, çözünürlük) okunur ve tüm bantların uzamsal olarak hizalı olduğundan emin olunur.
2.  **Sinyal Önişleme (Signal Preprocessing)**: Atmosferik etkilerden kaynaklanan bozulmalar ve analiz için engel teşkil eden unsurlar temizlenir. NDVI hesaplaması yapılarak bitki örtüsü maskesi oluşturulur. İsteğe bağlı olarak su maskesi (NDWI) de uygulanabilir.
3.  **Çekirdek Spektral Analiz (Core Spectral Analysis)**: NumPy kütüphanesinin vektörize edilmiş işlem yetenekleri kullanılarak, milyonlarca piksel üzerinde aynı anda matematiksel operasyonlar gerçekleştirilir. Bu aşama, Python'un döngüsel yavaşlığını elimine ederek C/C++ hızında hesaplama sağlar.
4.  **Sonuç Görselleştirme ve Raporlama (Visualization)**: Elde edilen sayısal matrisler, jeologların kolayca yorumlayabileceği renk kodlu (Color-coded) ısı haritalarına dönüştürülür. Sonuçlar, coğrafi referanslı (Geo-referenced) görseller olarak dışa aktarılır, böylece Google Earth veya GIS yazılımlarında (QGIS, ArcGIS) altlık olarak kullanılabilir.

### Dizin Yapısı ve Modül Sorumlulukları
```bash
Satellite-Mineral-Prospector/
├── src/
│   ├── analysis.py       # [ORKESTRATÖR] Tüm analiz akışını yöneten ana kontrol merkezi.
│   ├── indices.py        # [MATEMATİK ÇEKİRDEĞİ] Spektral formüllerin saf fonksiyonlar olarak tanımlandığı yer.
│   ├── io.py             # [VERİ KATMANI] Raster dosyalarının güvenli ve hızlı okunup yazılmasını sağlar.
│   ├── preprocessing.py  # [TEMİZLİK EKİBİ] Maskeleme ve veri normalizasyon işlemlerini yürütür.
│   └── visualize.py      # [SUNUM KATMANI] Veriyi estetik ve anlaşılır grafiklere dönüştürür.
├── tests/                # [KALİTE KONTROL] Kodun her parçasının doğru çalıştığını garanti eden test senaryoları.
└── docs/                 # [BİLGİ BANKASI] Kullanıcı kılavuzları ve teknik dokümantasyon.
```

---

## 💻 Kurulum, Yapılandırma ve Çalıştırma Rehberi

Bu güçlü analiz aracını kendi yerel geliştirme ortamınızda (Local Environment) çalıştırmak için aşağıdaki adımları sırasıyla takip edebilirsiniz. Proje, Python 3.9 ve üzeri sürümlerle tam uyumludur.

### 1. Depoyu Klonlama ve Hazırlık
Öncelikle, GitHub üzerindeki bu kaynak kodunu kendi bilgisayarınıza indirin:
```bash
git clone https://github.com/bahattinyunus/Satellite-Mineral-Prospector.git
cd Satellite-Mineral-Prospector
```

### 2. Bağımlılıkların Yüklenmesi
Projenin ihtiyaç duyduğu bilimsel kütüphaneleri (NumPy, RasterIO, Matplotlib vb.) otomatik olarak yükleyin:
```bash
pip install -r requirements.txt
# Veya kurulum scripti ile:
pip install .
```

### 3. Kullanım Senaryoları (Use Cases)

#### Seçenek A: Komut Satırı Arayüzü (CLI) ile Hızlı Analiz
Profesyonel kullanıcılar için geliştirilen CLI arayüzü sayesinde, tek bir komutla analiz başlatabilirsiniz:
```bash
python -m src.cli \
  --b02 veriler/B02.jp2 \
  --b04 veriler/B04.jp2 \
  --b08 veriler/B08.jp2 \
  --b11 veriler/B11.jp2 \
  --b12 veriler/B12.jp2 \
  --output maden_haritasi.png \
  --mask
```
*Bu komut, belirtilen bantları okur, bitki örtüsü maskesini uygular ve sonuç haritasını üretir.*

#### Seçenek B: Python API ile Özelleştirilmiş Analiz
Kendi Python scriptleriniz içinde kütüphaneyi modül olarak kullanabilir ve analiz sürecini özelleştirebilirsiniz:

```python
from src.analysis import analyze_scene
from src.visualize import plot_results

# 1. Bant Düzeninin Tanımlanması
# Sentinel-2 bant dosyalarınızın tam dosya yollarını bir sözlük (dictionary) yapısında belirtin.
bands_config = {
    'B02': 'veri/T35TPF_20230815_B02.jp2', # Mavi Bant (Blue)
    'B04': 'veri/T35TPF_20230815_B04.jp2', # Kırmızı Bant (Red)
    'B08': 'veri/T35TPF_20230815_B08.jp2', # Yakın Kızılötesi (NIR)
    'B11': 'veri/T35TPF_20230815_B11.jp2', # Kısa Dalga Kızılötesi 1 (SWIR1)
    'B12': 'veri/T35TPF_20230815_B12.jp2'  # Kısa Dalga Kızılötesi 2 (SWIR2)
}

# 2. Analiz Motorunun Çalıştırılması
# mask_vegetation=True parametresi ile NDVI > 0.3 olan alanları otomatik maskeleyin.
print("Analiz başlatılıyor...")
results = analyze_scene(bands_config, mask_vegetation=True)

# 3. Sonuçların Görselleştirilmesi ve Kaydedilmesi
# Üretilen haritayı yüksek çözünürlüklü (300 DPI) bir PNG dosyası olarak kaydedin.
plot_results(results, output_path='profesyonel_maden_haritasi.png')
print("İşlem başarıyla tamamlandı.")
```

---

## 🔮 Gelecek Vizyonu ve Yol Haritası (Roadmap)

Projenin gelişim süreci dinamik bir şekilde devam etmektedir. Gelecek sürümler için planlanan özellikler şunlardır:

- [ ] **Yapay Zeka Destekli Sınıflandırma**: Tespit edilen spektral anomalilerin, makine öğrenimi modelleri (Random Forest, SVM veya CNN) kullanılarak belirli maden türlerine (örneğin Altın, Bakır, Lityum) göre otomatik sınıflandırılması.
- [ ] **Mikroservis Mimarisi**: Analiz motorunun FastAPI kullanılarak bir RESTful API servisine dönüştürülmesi ve bulut tabanlı (Cloud-native) dağıtıma uygun hale getirilmesi.
- [ ] **Çoklu Sensör Füzyonu**: Landsat 9 ve ASTER uydularından gelen verilerin de sisteme entegre edilmesi ve farklı uyduların verilerinin birleştirilerek (Fusion) daha yüksek doğruluk sağlanması.
- [ ] **3 Boyutlu Görselleştirme**: Elde edilen mineral haritalarının, Dijital Yükseklik Modelleri (DEM) üzerine giydirilerek 3 boyutlu topografik analiz imkanı sunulması.

---

## 👨‍💻 Geliştirici ve Mimar Hakkında
 
Bu proje, teknolojinin dönüştürücü gücüne inanan ve mühendislik disiplinini sanatla birleştirmeyi hedefleyen **Bahattin Yunus Çetin** tarafından tasarlanmış, mimarisi kurgulanmış ve kodlanmıştır.

<div align="left">

### **Bahattin Yunus Çetin**
**IT Architect (Bilişim Teknolojileri Mimarı) | Full-Stack Yazılım Mühendisi**

Türkiye'nin teknoloji üssü olma yolunda ilerleyen Trabzon'un Of ilçesinde üniversite eğitimini sürdüren Bahattin Yunus, **Anka Silicon Dynamics** vizyonunun kurucusu ve baş mimarıdır. Çalışmaları, savunma sanayii teknolojileri, uzaktan algılama sistemleri, büyük veri analitiği ve yapay zeka tabanlı otonom sistemler üzerine yoğunlaşmıştır.

Sadece kod yazmayı değil, karmaşık problemleri zarif, ölçeklenebilir ve sürdürülebilir yazılım mimarileriyle çözmeyi bir tutku haline getirmiştir. Misyonu, yerel potansiyeli küresel standartlarda mühendislik çözümleriyle birleştirerek katma değerli teknolojiler üretmektir.

---

[![GitHub](https://img.shields.io/badge/GitHub-Portfolyo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bahattinyunus)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profesyonel_Ağ-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bahattinyunus/)
[![Email](https://img.shields.io/badge/Email-İletişim-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:iletisim@ankasilicondynamics.com)

</div>

---
*© 2026 Anka Silicon Dynamics. Tüm Hakları Saklıdır. Bu yazılım, insanlığın bilimsel ilerlemesine katkı sağlamak amacıyla açık kaynak olarak sunulmuştur.*


