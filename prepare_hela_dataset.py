import os
import json

# Base path where nnUNet_raw is located
base_path = r"C:\Users\Likithasri\OneDrive\Pictures\Dokumen\CTC_Vscode\nnUNet\nnUNet_raw"

# Dataset folder
dataset_id = "Dataset001_DIC-C2DH-HeLa"
dataset_path = os.path.join(base_path, dataset_id)

# Subfolders
imagesTr = os.path.join(dataset_path, "imagesTr")
labelsTr = os.path.join(dataset_path, "labelsTr")
imagesTs = os.path.join(dataset_path, "imagesTs")

# Create folders
for folder in [imagesTr, labelsTr, imagesTs]:
    os.makedirs(folder, exist_ok=True)

print("Dataset folders created at:", dataset_path)

# Example dataset.json
dataset_json = {
    "name": "DIC-C2DH-HeLa",
    "description": "Cell Tracking Challenge HeLa dataset",
    "tensorImageSize": "3D",
    "modality": {
        "0": "DIC"
    },
    "labels": {
        "0": "background",
        "1": "cell"
    },
    "numTraining": 2,
    "numTest": 1,
    "training": [
        {
            "image": "./imagesTr/case0000_0000.tif",
            "label": "./labelsTr/case0000.nii.gz"
        },
        {
            "image": "./imagesTr/case0001_0000.tif",
            "label": "./labelsTr/case0001.nii.gz"
        }
    ],
    "test": [
        "./imagesTs/case0002_0000.tif"
    ]
}

# Save dataset.json
json_path = os.path.join(dataset_path, "dataset.json")
with open(json_path, "w") as f:
    json.dump(dataset_json, f, indent=4)

print("✅ dataset.json created at:", json_path)
