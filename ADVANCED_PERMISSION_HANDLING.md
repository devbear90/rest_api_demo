## 🧩 Haladó jogosultsági lehetőségek (Django oldalon)

| Funkció                          | Leírás                                                               |
|----------------------------------|----------------------------------------------------------------------|
| ✅ Permission kombinálás         | Több engedélyosztály együttes használata, akár `get_permissions()` metódusban |
| ✅ Műveletszintű engedélyezés    | `self.action` alapján más engedély `list`, `create`, `destroy`, stb. műveletekre |
| ✅ Throttling                     | Sebességkorlátozás felhasználónként vagy API-kulcsonként (`100/hour`) |
| ✅ APIView / GenericAPIView       | Egyedi engedélyezés testreszabott nézetekben                         |
| ✅ SSO / SAML / OIDC integráció   | Központi hitelesítési rendszerek (Azure AD, Okta, Keycloak) támogatása |

---

## 🏢 Active Directory (AD) integrációs lehetőségek

### 🔗 Áttekintés

A Django REST Framework integrálható vállalati környezetekbe, ahol a jogosultságkezelést egy **Active Directory** (vagy bármilyen LDAP) szolgáltatás végzi. Az AD biztosítja a központi felhasználó- és csoportkezelést, míg a Django/DRF az alkalmazás-specifikus üzleti logikát és finomhangolt jogosultságokat.

### ⚙️ Technikai eszközök

| Megoldás                     | Használat                          |
|------------------------------|------------------------------------|
| `django-auth-ldap`           | Közvetlen AD / LDAP kapcsolat      |
| `django-auth-adfs`           | ADFS + SAML2 hitelesítés           |
| `mozilla-django-oidc`        | OpenID Connect (pl. Azure AD SSO)  |
| `social-auth-app-django`     | Többféle külső authentikáció       |

### 🔐 Példa: LDAP hitelesítés beállítása

```python
# settings.py
import ldap
from django_auth_ldap.config import LDAPSearch

AUTH_LDAP_SERVER_URI = "ldap://your.ad.server"
AUTH_LDAP_BIND_DN = "CN=binduser,OU=Users,DC=corp,DC=local"
AUTH_LDAP_BIND_PASSWORD = "secret123"

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "OU=Users,DC=corp,DC=local",
    ldap.SCOPE_SUBTREE,
    "(sAMAccountName=%(user)s)"
)
```

> A `User` objektum automatikusan létrejön az első sikeres AD-bejelentkezéskor, a csoporttagság pedig leképezhető Django `Group`-okra.

---

## 📊 Jogosultsági típusok és AD-lefedettség

| Jogosultsági típus             | Lefedhető AD-vel? | Megjegyzés                                                         |
|--------------------------------|-------------------|--------------------------------------------------------------------|
| Globális jogosultságok         | ✔️                | AD csoport alapján (`IsInGroup`)                                   |
| Objektumszintű jogosultságok   | ⚠️ Részben        | Csak Django oldalon: `obj.owner == request.user`                   |
| Csoportszintű jogosultságok    | ✔️                | AD Group → Django Group mapping                                    |
| Egyedi objektumszintű jogosl.  | ⚠️                | AD nem képes objektumszintű szabályozásra                           |
| Modell-permission              | ✔️                | Csoporthoz rendelt `add`, `view`, `change`, `delete` engedély       |
| Sor-szintű jogosultságok       | ❌                | AD nem kezel adatbázis rekord szintű jogosultságot                 |
| Kontextus-alapú jogosultságok  | ❌                | Request-alapú döntés (idő, IP, header) csak DRF oldalon             |
| Token / API-kulcs alapú        | ❌                | Alkalmazás-oldali logika, AD-tól független                          |

---

## ✅ Ajánlott best practice

- **AD/SSO hitelesítés**:  `django-auth-ldap` vagy OIDC/SAML csomagokat.
- **Csoporttagság → Django `Group`**: Szinkronizálni kell az AD csoportokat Django csoportokra.
- **Csoportalapú jogosultságok**: Ne egyedi usereknek adjunk jogot, hanem használjunk csoportokat.
- **Backend validáció**: Minden jogosultság-ellenőrzés a szerveren történjen (DRF permission osztályok).
- **Kombinált engedélyek**: `IsAuthenticated` + `DjangoModelPermissions` + egyedi `BasePermission` kombinációja.
- **Request-specifikus logika** (idő, IP, header) maradjon DRF permission osztályokban.
- **Ne keverd** AD által kezelt és alkalmazás-specifikus logikát: az AD a *hitelesítést* és a *csoportkezelést* adja, a DRF a *üzleti jogosultságokat*.

---

## 📦 Ajánlott csomagok

| Csomag                        | Funkció                                                 |
|-------------------------------|---------------------------------------------------------|
| `django-auth-ldap`            | AD/LDAP hitelesítés                                     |
| `django-auth-adfs`            | ADFS + SAML2                                            |
| `mozilla-django-oidc`         | OpenID Connect (OIDC)                                   |
| `social-auth-app-django`      | Több külső hitelesítési provider                        |
| `dj-rest-auth`                | Auth endpointok DRF-ben                                 |
| `django-guardian`             | Objektumszintű jogosultság per user                     |

---

