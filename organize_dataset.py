import os
import numpy as np
import tifffile

labels_root = r"C:/Users/Likithasri/OneDrive/Pictures/Dokumen/CTC_Vscode/nnUNet/nnUNet_raw/Dataset001_DIC-C2DH-HeLa/labelsTr"

for fname in os.listdir(labels_root):
    if fname.endswith(".tif"):
        path = os.path.join(labels_root, fname)
        arr = tifffile.imread(path)
        # Convert to binary mask
        binary = (arr > 0).astype(np.uint8)
        tifffile.imwrite(path, binary)
        print(f"Converted {fname} to binary mask")

print("✅ All labels converted to {0,1} masks")