import os
import sys
import django
import random
import uuid
from django.utils import timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigdata_api.settings")

django.setup()

from api.models import LargeDataset

def generate_unique_sku():
    """
    Egyedi SKU generálása UUID alapján.
    """
    return f"SKU-{uuid.uuid4().hex[:12]}"

def generate_large_dataset_records(n=10000):
    records = []
    for i in range(n):
        record = LargeDataset(
            name=f"Termék {i}",
            description="Véletlenszerű termékleírás.",
            category=random.choice(["Elektronika", "Ruházat", "Konyhai eszközök"]),
            sub_category=random.choice(["Mobil", "Laptop", "TV", "Póló", "Kabát", "Serpenyő"]),
            status=random.choice(["Aktív", "Inaktív", "Kifogyott"]),
            data={"custom_field": f"Érték {i}"},
            quantity=random.randint(1, 1000),
            price=round(random.uniform(10, 1000), 2),
            discount=round(random.uniform(0, 50), 2),
            stock=random.randint(0, 500),
            rating=round(random.uniform(1, 5), 1),
            is_active=random.choice([True, False]),
            is_featured=random.choice([True, False]),
            published_date=timezone.now(),
            last_purchased_date=timezone.now(),
            brand=random.choice(["Samsung", "Apple", "Nike", "Adidas"]),
            manufacturer=random.choice(["Gyártó A", "Gyártó B", "Gyártó C"]),
            model_number=f"MD-{random.randint(1000, 9999)}",
            serial_number=f"SN-{random.randint(100000, 999999)}",
            warranty=f"{random.randint(1, 5)} év",
            supplier="Beszállító Kft.",
            supplier_email=f"beszallito{i}@example.com",
            country=random.choice(["Magyarország", "Németország", "Franciaország"]),
            city=random.choice(["Budapest", "Berlin", "Párizs"]),
            zip_code=str(random.randint(1000, 9999)),
            address=f"{random.randint(1, 500)}. utca",
            color=random.choice(["Fekete", "Fehér", "Piros", "Kék"]),
            material=random.choice(["Fém", "Műanyag", "Fa"]),
            weight=round(random.uniform(0.5, 10), 2),
            dimensions=f"{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(10, 100)} cm",
            shipping_time=random.randint(1, 14),
            barcode=f"BC-{random.randint(100000, 999999)}",
            sku=generate_unique_sku(),  # Egyedi SKU generálás
            notes="Nincs megjegyzés.",
            metadata={"tulajdonság": "érték"},
            specifications={"méret": f"{random.randint(10, 50)}cm"}
        )
        records.append(record)
    return records

def load_data():
    batch_size = 10000
    total_records = 500000

    for i in range(0, total_records, batch_size):
        print(f"Feltöltés: {i}-{i+batch_size}")
        batch = generate_large_dataset_records(batch_size)
        LargeDataset.objects.bulk_create(batch, ignore_conflicts=True)

if __name__ == "__main__":
    load_data()
