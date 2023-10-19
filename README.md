# Sohbet Odaları Uygulaması README

## Genel Bakış

Bu uygulama, kullanıcıların sohbet odaları oluşturmasına ve bu odalara katılmasına olanak tanır. Her kullanıcı, kendine ait bir kullanıcı adı seçebilir ve bu kullanıcı adıyla iletişim kurabilir.

## Gereksinimler

Bu programı çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3
- Tkinter (Python'ın standart kitaplığıdır ve genellikle Python ile birlikte gelir.)
- Firebase Admin SDK (Firebase veritabanı erişimi için)

## Kurulum

1. Firebase Admin SDK'yi yükleyin: Firebase veritabanına erişim sağlamak için Firebase Admin SDK'yi kullanıyoruz. [Firebase Console](https://console.firebase.google.com/) üzerinden bir web tabanlı proje oluşturun ve SDK'nin kimlik bilgilerini (Service Account Key) edinin (Ayarlar > Project Settings > Service  accounts  > create new private key). Daha sonra bu kimlik bilgilerini satır 11-23 arasındaki boşluklara kaydedin.(pip install firebase_admin)

2. Python kurulumunu yapın: Python 3'ü [Python resmi web sitesinden](https://www.python.org/) indirip kurun.

3. Tkinter'ı etkinleştirin: Tkinter, genellikle Python ile birlikte gelir. Ek kurulum yapmanız gerekmez.(pip install tk)

4. Kodu çalıştırın: Kodunuzun çalıştırılabilmesi için Python betiğini çalıştırın.

## Kullanım

1. Programı başlatın ve aşağıdaki seçeneklerden birini seçin:
   - "Oda Oluştur": Kendi özel sohbet odanızı oluşturun ve bir oda kodu alın.
   - "Odaya Katıl": Var olan bir odaya katılın. Oda kodunu girerek katılabilirsiniz.

2. Sohbet Odası:
   - Bir odaya katıldığınızda, o oda için yeni bir pencere açılacaktır.
   - Bu pencerede kullanıcı adınızı girin ve sohbet etmeye başlayın.
   - Göndermek istediğiniz mesajı "Mesaj Girin..." alanına yazın ve "Gönder" düğmesini tıklayarak iletebilirsiniz.

## Dikkat Edilmesi Gerekenler

- Sohbet odalarınızın özel bir oda kodu vardır. Bu oda kodu ile katılanlar o özel odada iletişim kurabilir.
- Sohbetler oturum sonlandığında veya pencere kapatıldığında kaybolabilir, bu nedenle önemli bilgileri kaybetmemek için mesajları başka bir yere kopyalamanız gerekebilir.

## Lisans

Bu kod, MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyin.

## Credits
NSFW kontrolü için @ooguz tarafından Github'da paylaşılan bir dosya kullanılmıştır.

## Yazar

- Discord: adlf_htlr
- Github: mehmet-2023
