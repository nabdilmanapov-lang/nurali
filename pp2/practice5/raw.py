import re
import json

# Read raw receipt text
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------
# 1. Extract item blocks
# -------------------------
item_pattern = re.compile(
    r"\d+\.\s*\n"                    # Item number
    r"(.+?)\n"                       # Product name
    r".*?\n"                         # Quantity line
    r"([\d\s]+,\d{2})\n"             # Item total price
    r"Стоимость",
    re.DOTALL
)

items = []
prices = []

for match in item_pattern.finditer(text):
    name = match.group(1).strip()
    price_raw = match.group(2).replace(" ", "").replace(",", ".")
    price = float(price_raw)

    items.append({
        "name": name,
        "total_price": price
    })

    prices.append(price)

# -------------------------
# 2. Extract Total
# -------------------------
total_match = re.search(r"ИТОГО:\s*\n?([\d\s]+,\d{2})", text)
total = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else None

# -------------------------
# 3. Extract Date & Time
# -------------------------
datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", text)
date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

# -------------------------
# 4. Extract Payment Method
# -------------------------
payment_match = re.search(r"(Банковская карта):", text)
payment_method = payment_match.group(1) if payment_match else None

# -------------------------
# 5. Structured Output
# -------------------------
receipt_data = {
    "items": items,
    "extracted_prices": prices,
    "calculated_total": sum(prices),
    "receipt_total": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(receipt_data, indent=4, ensure_ascii=False))
