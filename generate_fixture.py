import json
import random
import os

# Ensure fixtures folder exists
os.makedirs("products/fixtures", exist_ok=True)

categories = ["Mac", "iPad", "iPhone", "Watch", "Accessories"]

# Generate 100 products
products = []
for i in range(1, 101):
    category = random.choice(categories)
    product = {
        "model": "products.product",
        "pk": i,
        "fields": {
            "name": f"{category} Model {i}",
            "description": f"High-quality {category} product number {i}",
            "image": f"product_images/{category.lower()}{i%10+1}.jpg"
        }
    }
    products.append(product)

# Generate 50 iPhone features
features = []
for i in range(1, 51):
    feature = {
        "model": "products.iphonefeature",
        "pk": i,
        "fields": {
            "title": f"Feature {i}",
            "description": f"Description of feature {i} for iPhone",
            "image": f"feature_images/feature{i%10+1}.jpg"
        }
    }
    features.append(feature)

# Combine all data
all_data = products + features

# Save to fixtures folder
with open("products/fixtures/sample_data_large.json", "w") as f:
    json.dump(all_data, f, indent=4)

print("sample_data_large.json created successfully!")
