# 📖 Django Authorization Dokumentáció

Az **Authorization (jogosultságkezelés)** meghatározza, hogy egy hitelesített felhasználó milyen műveleteket hajthat végre egy API-n belül. Django REST Framework (DRF) több szinten is lehetőséget biztosít a jogosultságok szabályozására.

---

## 📌 1. Globális jogosultságok (Default Permissions)
A globális jogosultságokat a **DRF beállításaiban** adhatjuk meg, ezek minden API végpontnál automatikusan érvényesek.

Django REST Framework beépített jogosultságosztályokat biztosít, mint pl.:
- ✅ `AllowAny` – minden felhasználó elérheti az API-t.
- ✅ `IsAuthenticated` – csak hitelesített felhasználók férhetnek hozzá.
- ✅ `IsAdminUser` – csak adminoknak engedélyezett a hozzáférés.
- ✅ `IsAuthenticatedOrReadOnly` – hitelesített felhasználók módosíthatnak, de mindenki olvashatja az adatokat.

Ezeket a `DEFAULT_PERMISSION_CLASSES` listában lehet megadni, így minden végpont alapértelmezett védelmet kap.

---

## 🔒 2. Objektumszintű jogosultságok (Object-level Permissions)
Az objektumszintű jogosultságok azt szabályozzák, hogy egy adott felhasználó **csak bizonyos rekordokra kapjon engedélyt**. Ez azt jelenti, hogy a kérés attól függően engedélyezett vagy elutasított, hogy a felhasználó a kért adat tulajdonosa-e.

Ezek a jogosultságok tipikusan **üzleti logikától** függenek, pl. egy felhasználó **csak a saját adatait szerkesztheti**, de az adminok minden adathoz hozzáférhetnek.

---

## 🏷️ 3. Csoportszintű jogosultságok (Group Permissions)
A Django **Groups & Permissions** rendszere lehetővé teszi, hogy egy adott felhasználót **csoportokhoz rendeljünk**, majd ezekre a csoportokra **egyedi engedélyeket** állítsunk be.

Ezek a jogosultságok az **Admin Panelen keresztül kezelhetőek**, így az adminok könnyen megadhatják, hogy ki milyen API végpontokat vagy funkciókat érhet el.

---

## 🛠️ 4. Egyedi objektumszintű jogosultságok (Custom Object Permissions)
Bizonyos esetekben **egyedi szabályokat kell alkalmazni** az objektumokra. Ezeket az egyéni **`BasePermission`** osztályokban lehet megvalósítani.

Például egy API végpontban csak **adminok** törölhetnek adatokat, de mindenki módosíthatja azokat. Ehhez egyedi **`has_permission`** és **`has_object_permission`** metódusok használhatóak.

---

## 📋 5. Modell-alapú jogosultságok (Django Model Permissions)
Django alapból támogatja a **modell-alapú jogosultságokat**, amelyek az **Admin Panel jogosultságaival** integrálhatók. A Django **beépített `view`, `add`, `change`, `delete` engedélyeket** biztosít az egyes modellekhez.

Ha a DRF **`DjangoModelPermissions`** osztályát használjuk, akkor az API automatikusan tiszteletben tartja az admin felületen beállított jogosultságokat.

---

## 📂 6. Adatbázis-alapú jogosultságok (Row-Level Permissions)
Ez a jogosultsági szint akkor hasznos, ha a felhasználók **csak bizonyos rekordokat láthatnak**, amelyeket kifejezetten rájuk vagy a csoportjukra szabtak.

Ezt általában **egyedi SQL lekérdezésekkel** vagy egyedi jogosultsági táblákkal lehet kezelni, ahol minden rekordhoz tartozik egy engedélyezett felhasználólista vagy csoport.

---

## ⏳ 7. Kontextus-alapú jogosultságok (Request Context Permissions)
Néha a jogosultságokat **dinamikusan kell kezelni** a kérés adatai alapján.

Például egy API csak bizonyos **időszakokban** engedélyezett, vagy egyes felhasználók más jogosultságot kapnak attól függően, hogy milyen típusú kérést küldtek be.

---

## 🔑 8. Token- vagy API-kulcs alapú jogosultságok
Ha külső rendszerek használják az API-t, akkor **speciális API-kulcsokat vagy tokent** lehet használni a jogosultságok meghatározására.

Ez lehetővé teszi, hogy különböző **hozzáférési szinteket** biztosítsunk API-kulcsokon keresztül.

---

## 🎯 Összegzés

| **Típus** | **Leírás** | **Mikor használd?** |
|-----------|-----------|-------------------|
| **Globális jogosultságok** | `DEFAULT_PERMISSION_CLASSES` | Ha minden végpontnál egyformán kell szabályozni a hozzáférést. |
| **Objektumszintű jogosultságok** | `has_object_permission()` | Ha minden rekordhoz egyedi jogosultságok tartoznak. |
| **Csoportszintű jogosultságok** | Django Groups & Permissions | Ha csoportok szerint akarod kezelni a felhasználók jogosultságait. |
| **Egyedi objektumszintű jogosultságok** | Custom `BasePermission` | Ha speciális feltételeket kell ellenőrizni. |
| **Modell-alapú jogosultságok** | `DjangoModelPermissions` | Ha a Django Admin jogosultságokat akarod API-ra is kiterjeszteni. |
| **Adatbázis-alapú jogosultságok** | SQL szintű jogosultságok | Ha bizonyos rekordokat csak egyes felhasználók érhetnek el. |
| **Kontextus-alapú jogosultságok** | `has_permission()` a request adatai alapján | Ha a jogosultságokat egyéni feltételek alapján akarod szabályozni. |
| **API-kulcs vagy token alapú jogosultságok** | `request.auth` ellenőrzés | Ha különböző hozzáférési szinteket akarsz API-kulcsokkal megvalósítani. |

---