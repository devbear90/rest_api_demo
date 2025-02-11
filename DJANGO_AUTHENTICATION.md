# 🔐 Authentication (Hitelesítés)

Az API különböző hitelesítési módszereket támogat, amelyek lehetővé teszik a biztonságos hozzáférést az erőforrásokhoz.

---

## **1️⃣ Basic Authentication**
🔑 **User - Password páros** alapú hitelesítés.  

### 📌 **Használata**  
A request során az **Authorization** fejlécben a következő információt kell átadni:  
Authorization: Basic Base64-kódolt(felhasználónév:jelszó)


---

## **2️⃣ Token Based Authentication**
🔑 **Felhasználóhoz rendelt token** alapú hitelesítés.  

### 📌 **Működés**  
- A userhez tartozik egy token, amelyet a Django egy **külön adatbázistáblában (`authtoken_token`)** tárol.  
- **Alapértelmezés szerint ez a token nem jár le.**  
- Manuálisan lehet **tokent cserélni**.  
- A Django REST Framework alapértelmezett Token Authentication rendszere **nem támogatja a tokenek automatikus lejáratát**.  
- Egyedi **modellt vagy middleware-t** kell használni a lejárat implementálásához.  

### 📌 **További jellemzők**  
✅ Automatizálható, hogy egy új user létrehozásakor **automatikusan generálódjon token**.  
✅ **Minden felhasználónak egyetlen tokenje lehet érvényben**.  
✅ Ha a user törlődik, **a tokenje is automatikusan törlődik** (*cascade delete* mechanizmus).  
✅ A token annak a validálására van, hogy a felhasználó jogosult az API használatára.  
✅ Az API-n belüli műveletek jogosultságát **Authorization-nel lehet szabályozni**.  

---

## **3️⃣ JWT Token Authentication**
🔑 **JSON Web Token alapú hitelesítés**.  

### 📌 **Működés**  
- A **JWT (JSON Web Token)** egy **biztonságos és skálázható** autentikációs módszer.  
- A szerver **aláírt tokent generál** a bejelentkezés után.  
- **Django nem tárolja** a tokeneket az adatbázisban.  
- Az API kliensek **minden kérésnél elküldik a tokent** az Authorization fejlécben.

### 📌 **JWT komponensei**  
A token szerkezete **három részből áll**:  
1️⃣ **Header** – az algoritmus és a token típusa  
2️⃣ **Payload** – a felhasználói adatok és egyéb metaadatok  
3️⃣ **Signature** – a szerver titkos kulccsal aláírt rész, amely biztosítja a token érvényességét  

### 📌 **Access Token és Refresh Token**  
A JWT két fő részből áll:  
- **Access Token**: Rövid élettartamú (*pl. 5 perc*), minden API hívásnál ezt kell használni.  
- **Refresh Token**: Hosszabb élettartamú (*pl. 1 nap*), új **Access Token** generálására szolgál anélkül, hogy a felhasználónak újra be kellene jelentkeznie.  
- A **Django REST Framework Simple JWT csomag** biztosítja ezt a funkciót.

### 📌 **Használat az API hívások során**  
A JWT Token a következő formátumban kerül elküldésre minden API híváskor:  
Authorization: Bearer <access_token>


### 📌 **További jellemzők**  
✅ A JWT **stateless**, vagyis a szerver nem tárolja a tokeneket, csupán ellenőrzi az aláírásukat.  
✅ Az API-n belüli műveletek jogosultságát **Authorization-nel lehet szabályozni**.  

---