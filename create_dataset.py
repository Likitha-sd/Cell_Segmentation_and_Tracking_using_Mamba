import json
import os

# Define dataset structure
dataset = {
    "name": "DIC-C2DH-HeLa",
    "description": "Cell segmentation dataset",
    "tensorImageSize": "3D",
    "modality": {"0": "Microscopy"},
    "labels": {"0": "background", "1": "cell"},
    "numTraining": 168,
    "numTest": 0,
    "training": []
}

# Add 168 training entries
for i in range(168):
    dataset["training"].append({
        "image": f"./imagesTr/case{i:04d}_0000.tif",
        "label": f"./labelsTr/case{i:04d}.tif"
    })

# Path to dataset.json
out_path = r"C:\Cell_Tracking_Challenge\Cell_Segmentation_and_Tracking_using_Mamba\nnUNet\nnUNet_raw\Dataset001_DIC-C2DH-HeLa\dataset.json"

# Ensure folder exists
os.makedirs(os.path.dirname(out_path), exist_ok=True)

# Write JSON file
with open(out_path, "w") as f:
    json.dump(dataset, f, indent=4)

print("✅ dataset.json created with 168 entries")
