"# rest_api_demo" 

API fogalma: Application Programming Interface
Egy olyan interface, amely lehetővé teszi kölönböző szoftverek és rendszerek közötti 
kommunikációt szabványosított formában.

Interface: Az API egy meghatározott módot biztosít az adatok lekérdezésére és küldésére.
Abstraction: Az API "elrejti" az implementációs logikát és egy könnyen használható réteget biztosít.
Standardization: Meghatározott protokollokat és formátumokat használ. pl. Rest, SOAP, GraphQL

*********************************************************************************************
API típusok:
REST API – HTTP alapú, JSON-t vagy XML-t használ adatcserére.
GraphQL API – Rugalmas adatlekérdezési mód, ahol a kliens határozza meg, milyen adatokat kér el.
SOAP API – XML alapú, szigorúbb struktúrával.
*********************************************************************************************
Mitől lesz Rest a Rest API?
A REST (Representational State Transfer) egy architekturális pattern
Olyan szabályokat és elveket fogalmaz meg a REST, amelyeket az API-nak követnie kell ahhoz,
hogy skálázható, rugalmas és jól használható legyen.

Alapelvek:
Állapotmentesség (Stateless) - A Szerver nem tárol semmilyen kliensoldali állapotot a kérések között, minden kérésnek tartalmaznia kell a szükséges adatokat. Pl. tokenek, inputok.

Erőforrások (Resources) URL-ekhez rendelése - Minden erőforrásnak egye egyedi URL címe van - pl. /task/1

HTTP metódusok használata (GET, POST, PUT, DELETE)

Kliens-szerver architektúra - MVC, MVT pattern: szerver az adatok eléréséért felel, a kliens a feldolgozásért és megjelenítésért

Cache-elhetőség - Az API válaszai cachelhetőek, így csökkenthető a szerver terhelése

Hiperhivatkozások (HATEOAS) -Az API válaszai tartalmazhatnak linkeket (hiperhivatkozásokat), amelyek segítenek a klienseknek a további elérhető műveletek felfedezésében
*********************************************************************************************

Mire nem való az API?
API-k nem megfelelőek olyan esetekben, amikor:
✅ Valós idejű, folyamatos adatáramlás kell → WebSocket, gRPC, Kafka
✅ Nagy fájlokat kell kezelni → CDN, Cloud Storage
✅ Hosszú futásidejű folyamatokat kell kezelni → Üzenetsorok aszinkron feldolgozással (Celery, RabbitMQ),
                                                  Batchelt feldolgozás
✅ Statikus adatokat kell szolgáltatni → Statikus HTML/CSS/JS fájlok vagy JSON fájlok CDN-en keresztül.
                                          Edge Computing és caching (pl. Cloudflare, Varnish).
✅ Adatbázis közvetlen elérése API-val → ORM, GraphQL

*********************************************************************************************
Mi az a GraphQL?
A GraphQL egy adatlekérdezési nyelv (query language) és egy API futtatási környezet

📌 Főbb jellemzők:
✔ Deklaratív lekérdezések – A kliens határozza meg, milyen adatokat szeretne.
✔ Egyetlen végpont (/graphql) – Nincs több különálló REST végpont.
✔ Erőforrások összekapcsolása – Egyetlen kérésben több kapcsolódó adat lekérhető.
✔ Erősen típusos séma – A szerver előre meghatározza az adatok struktúráját.

✔ GraphQL-t használj, ha...
✅ A kliensek eltérő adatokat igényelnek.
✅ Több erőforrást akarsz egyetlen kérésben lekérni.
✅ Pontosan szeretnéd kontrollálni, milyen adatot kér le a kliens.
✅ Öndokumentáló és típusos API-ra van szükség.

❌ REST API-t használj, ha...
✅ Egyszerű CRUD API-ra van szükséged.
✅ Cache-elés és teljesítmény kiemelten fontos.
✅ Nagy fájlokat kell kezelni.
✅ A szerver teljesítményének optimalizálása kritikus szempont.