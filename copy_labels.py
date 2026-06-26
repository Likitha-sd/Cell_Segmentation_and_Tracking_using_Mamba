import os
import json

base_dir = r"C:/Users/Likithasri/OneDrive/Pictures/Dokumen/CTC_Vscode/nnUNet/nnUNet_raw/Dataset001_DIC-C2DH-HeLa"
json_path = os.path.join(base_dir, "dataset.json")

# Load dataset.json
with open(json_path, "r", encoding="utf-8") as fh:
    dataset = json.load(fh)

# Count actual training entries
actual_count = len(dataset.get("training", []))
declared_count = dataset.get("numTraining", None)

print(f"Declared numTraining: {declared_count}")
print(f"Actual training entries: {actual_count}")

# Fix mismatch
if declared_count != actual_count:
    dataset["numTraining"] = actual_count
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(dataset, fh, indent=2)
    print(f"✅ Fixed numTraining to {actual_count}")
else:
    print("✅ numTraining already matches")
