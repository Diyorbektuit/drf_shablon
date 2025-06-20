# DRF Shablon

Bu shablon [Django REST Framework (DRF)](https://www.django-rest-framework.org/) asosida tezkor va samarali API ishlab chiqishni boshlash uchun tayyorlangan. Shablon modular arxitekturaga asoslangan bo'lib, rivojlantirishni tezlashtiradi va loyihani oson boshqarish imkonini beradi.

## Xususiyatlar

- **Modular arxitektura**: Ilovalar yaxshi tashkil etilgan.
- **DRF integratsiyasi**: RESTful API yaratuvchi komponentlar tayyor.
- **Sozlanadigan konfiguratsiyalar**: `settings` turli muhitlarga moslashgan.
- **Asosiy CRUD operatsiyalari**: API'lar uchun umumiy funktsiyalar tayyor.
- **Yordamchi skriptlar va konfiguratsiyalar**: Osonroq boshlash uchun.

## Loyiha Tuzilishi

```plaintext
drf_shablon/
├── apps/                # Alohida ilovalar joylashgan
├── core/                # Asosiy konfiguratsiya va yordamchi funksiyalar
├── deployment/          # Ishlab chiqarish va deployment uchun sozlamalar
├── envs/                # Turli muhitlarga mos sozlamalar
├── requirements/        # Bog‘liqliklar
├── manage.py            # Django boshqaruv fayli
└── README.md            # Loyihaning o'zi haqida hujjatlar
```

O‘rnatish
Reponi klonlash:

```plaintext
git clone <repository-url>
cd drf_shablon
```