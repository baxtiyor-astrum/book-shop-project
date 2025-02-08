# 📚 Django REST API (Books, Orders, Notifications)

## 🚀 Loyiha haqida
Bu loyiha **Django Rest Framework** asosida ishlab chiqilgan va **kitoblar, buyurtmalar va bildirishnomalar** bilan ishlash uchun API taqdim etadi. API JWT autentifikatsiyasidan foydalanadi va Swagger hujjatlari orqali test qilinishi mumkin.

---

## 🔧 O‘rnatish bo‘yicha qo‘llanma

### 1️⃣ Django loyihasini yuklab olish
```sh
git clone https://github.com/username/repo-name.git
cd repo-name
```

### 2️⃣ Virtual muhit yaratish va ishga tushirish
```sh
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
dotvenv\Scripts\activate  # Windows
```

### 3️⃣ Kerakli kutubxonalarni o‘rnatish
```sh
pip install -r requirements.txt
```

### 4️⃣ Ma’lumotlar bazasini yaratish
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Superuser yaratish (Admin panel uchun)
```sh
python manage.py createsuperuser
```

### 6️⃣ Serverni ishga tushirish
```sh
python manage.py runserver
```

---

## 📖 API Endpoints

### **1. Foydalanuvchilar (Users)**
- **`POST /users/register/`** → Ro‘yxatdan o‘tish
- **`POST /users/login/`** → Tizimga kirish
- **`POST /users/send-verification-email/`** → Email tasdiqlash
- **`GET /users/verify-email/?token=...`** → Emailni tasdiqlash
- **`POST /users/forgot-password/`** → Parolni tiklash
- **`POST /users/reset-password/`** → Yangi parol o‘rnatish
- **`GET /users/profile/`** → Profilni ko‘rish
- **`PUT /users/profile/`** → Profilni yangilash

### **2. Buyurtmalar (Orders)**
- **`GET /orders/`** → Foydalanuvchining barcha buyurtmalari
- **`POST /orders/`** → Yangi buyurtma yaratish
- **`GET /orders/{order_id}/`** → Aniq buyurtmani ko‘rish
- **`PATCH /orders/{order_id}/`** → Buyurtmani yangilash
- **`DELETE /orders/{order_id}/`** → Buyurtmani o‘chirish

### **3. Kitoblar (Books)**
- **`GET /books/`** → Kitoblar ro‘yxati
- **`POST /books/`** → Yangi kitob qo‘shish
- **`GET /books/{book_id}/`** → Kitob tafsilotlari
- **`PUT /books/{book_id}/`** → Kitob ma’lumotlarini yangilash
- **`DELETE /books/{book_id}/`** → Kitobni o‘chirish

### **4. Bildirishnomalar (Notifications)**
- **`GET /notifications/`** → Foydalanuvchining barcha bildirishnomalari
- **`POST /notifications/`** → Yangi bildirishnoma yaratish
- **`GET /notifications/{notification_id}/`** → Aniq bildirishnomani ko‘rish
- **`DELETE /notifications/{notification_id}/`** → Bildirishnomani o‘chirish

---

## 🔑 Autentifikatsiya
API **JWT tokenlar** orqali himoyalangan. 

### **1. Tizimga kirish va JWT olish**
```sh
POST /users/login/
```
**So‘rov:**
```json
{
    "email": "test@example.com",
    "password": "YourPassword123"
}
```
**Javob:**
```json
{
    "refresh": "eyJhbGciOiJIUz...",
    "access": "eyJhbGciOiJIUz..."
}
```

### **2. Token orqali API chaqirish**
Barcha himoyalangan endpointlarga so‘rov yuborishda `Authorization` header’dan foydalaning:
```http
Authorization: Bearer <ACCESS_TOKEN>
```

---

## 📜 API Hujjatlari (Swagger)
Swagger API hujjatlari orqali **barcha endpointlarni test qilish** va **Swagger JSON faylini yuklab olish** mumkin.

- **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **ReDoc UI**: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)
- **Swagger JSON**: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

---

## 🚀 Deploy qilish
Agar loyihani serverga joylamoqchi bo‘lsangiz, quyidagi qadamlarni bajaring:

### **1. Static fayllarni yig‘ish**
```sh
python manage.py collectstatic --noinput
```

### **2. Gunicorn va Nginx orqali ishga tushirish**
```sh
gunicorn project.wsgi:application --bind 0.0.0.0:8000
```

Agar **Docker** ishlatsangiz, quyidagi `docker-compose.yml` orqali loyihani konteynerda ishga tushirish mumkin:
```yml
version: '3'
services:
  web:
    build: .
    command: gunicorn project.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```

---

## 🛠 Texnologiyalar
- **Django Rest Framework** – API uchun
- **SQlite3** – Ma’lumotlar bazasi
- **JWT (Simple JWT)** – Autentifikatsiya
- **DRF Spectacular** – Swagger hujjatlari
- **Docker** – Deploy uchun (ixtiyoriy)

---

## 📩 Muammo yoki takliflar?
Agar sizda loyiha bo‘yicha **muammo yoki taklif** bo‘lsa, **GitHub Issues** orqali xabar qoldiring yoki **pull request** yuboring! 🎯

✅ **Loyihani yulduzcha bilan baholang va foydali deb topsangiz, qo‘llab-quvvatlang!** ⭐️
