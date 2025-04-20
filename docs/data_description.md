# 📊 Veri Seti Açıklaması

Bu projede kullanılan veri seti, simüle edilmiş 2000 adet kredi başvurusunu içermektedir. Veriler `generate_data.py` script'i ile oluşturulmuştur.

## 🧩 Özellikler:

| Sütun             | Açıklama                                                                 |
|------------------|--------------------------------------------------------------------------|
| `age`            | Başvuru sahibinin yaşı (18-65)                                           |
| `income`         | Aylık gelir (TL)                                                         |
| `debt`           | Toplam mevcut borç miktarı                                               |
| `credit_score`   | Kredi skoru (300-900 arası)                                              |
| `employment_years` | Mevcut iş yerindeki toplam çalışma süresi (yıl)                         |
| `approved`       | Kredi başvurusunun sonucu (0 = Reddedildi, 1 = Onaylandı)                |

## 🧠 Etiketleme Kuralı:

Başvurunun **onaylanması** aşağıdaki kurala göre belirlenmiştir:

 ``` income > 8000 AND credit_score > 600 AND debt < 20000 AND employment_years > 2 ``` 

Bu koşulu sağlayan başvurular genellikle onaylanır, sağlamayanlar ise reddedilir. Ancak, daha gerçekçi bir veri seti oluşturmak amacıyla %10 oranında rastgelelik (noise) eklenmiştir. Böylece bazı kurallara uymayan başvurular da onaylanmış gibi etiketlenmiş olabilir.

