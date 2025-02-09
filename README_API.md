# 🚀 REST API Demo

## 📌 API fogalma
**API (Application Programming Interface)** egy olyan interfész, amely lehetővé teszi különböző szoftverek és rendszerek közötti **szabványosított kommunikációt**.

### 🔹 API fő jellemzői:
- **Interface** – Adatok lekérdezésére és küldésére szolgáló interfész.
- **Abstraction** – Elrejti az implementációs logikát, egyszerűsítve a használatot.
- **Standardization** – Meghatározott protokollokat és formátumokat használ *(pl. REST, SOAP, GraphQL).*  

---

## 🌍 API típusok

| Típus        | Leírás |
|-------------|---------|
| **REST API** | HTTP-alapú, JSON/XML formátumú adatcsere. |
| **GraphQL API** | Rugalmas lekérdezési mód, ahol a kliens határozza meg a kért adatokat. |
| **SOAP API** | XML-alapú, szigorúbb struktúrával rendelkező protokoll. |

---

## 🔥 Mitől lesz REST a REST API?
A **REST (Representational State Transfer)** egy **architekturális minta**, amely biztosítja az API **skálázhatóságát, rugalmasságát és használhatóságát**.

### 🛠 Alapelvek:

✅ **Állapotmentesség (Stateless)** – A szerver nem tárol kliensoldali állapotot a kérések között. *(Pl.: tokenek, inputok minden kérésben szerepelnek.)*  
✅ **Erőforrások (Resources) URL-ekhez rendelése** – Egyedi URL minden erőforrásra *(pl. `/tasks/1`).*  
✅ **HTTP metódusok használata** – *GET, POST, PUT, DELETE stb.*  
✅ **Kliens-szerver architektúra** – Elkülönül a kliens és szerver logikája *(MVC, MVT minták).*  
✅ **Cache-elhetőség** – A válaszok gyorsítótárazhatóak a szerver terhelésének csökkentése érdekében.  
✅ **HATEOAS (Hypermedia as the Engine of Application State)** – Az API válaszai **linkeket tartalmazhatnak**, segítve a klienst a további műveletek felfedezésében.  

---

## ❌ Mire **nem való** az API?

🚫 **Valós idejű adatáramlás** → **WebSocket, gRPC, Kafka** megfelelőbb.  
🚫 **Nagy fájlok kezelése** → **CDN, Cloud Storage** javasolt.  
🚫 **Hosszú futásidejű folyamatok** → **Aszinkron feldolgozás (Celery, RabbitMQ, Batch Processing).**  
🚫 **Statikus adatok szolgáltatása** → **CDN, Cloudflare, statikus fájlok.**  
🚫 **Közvetlen adatbázis-hozzáférés** → **ORM, GraphQL jobb választás.**  

---

## 🔷 **Mi a GraphQL?**

A **GraphQL** egy **adatlekérdezési nyelv (query language)** és egy **API futtatási környezet**, amelyet a **Facebook fejlesztett** ki.  

### 📌 **Főbb jellemzők:**
✔ **Deklaratív lekérdezések** – A kliens határozza meg, milyen adatokat kér.  
✔ **Egyetlen végpont (`/graphql`)** – Nincs több REST végpont.  
✔ **Erőforrások összekapcsolása** – Egy kérésben több adat is lekérhető.  
✔ **Erősen típusos séma** – Az API előre meghatározza az adatok struktúráját.  

---

## ✅ **Mikor használjunk GraphQL-t?**

✔ Ha a kliensek eltérő adatokat igényelnek.  
✔ Ha több erőforrást szeretnénk egyetlen kérésben lekérni.  
✔ Ha pontosan szeretnénk kontrollálni, milyen adatokat kap a kliens.  
✔ Ha **önállóan dokumentálódó és típusos API**-ra van szükség.  

---

## ❌ **Mikor válassz inkább REST API-t?**

🚀 **Egyszerű CRUD API** esetén.  
🚀 **Cache-elés és teljesítmény** szempontjából REST előnyösebb.  
🚀 **Nagy fájlok** kezelésére.  
🚀 **Ha a szerver teljesítményét optimalizálni kell.**  

---

💡 **Összegzés**: **GraphQL-t** dinamikus, kliens-központú API-khoz használj, míg **REST** a gyors, egyszerű és skálázható megoldás! 🚀

