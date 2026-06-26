import SimpleITK as sitk
import os

labels_folder = r"C:\Users\Likithasri\OneDrive\Pictures\Dokumen\CTC_Vscode\nnUNet\nnUNet_raw\Dataset001_DIC-C2DH-HeLa\labelsTr"

for fname in os.listdir(labels_folder):
    if fname.endswith(".tif"):
        tif_path = os.path.join(labels_folder, fname)
        case_id = fname.replace(".tif", "")  # e.g. case0000_mask.tif → case0000_mask
        nii_path = os.path.join(labels_folder, case_id + ".nii.gz")

        img = sitk.ReadImage(tif_path)
        sitk.WriteImage(img, nii_path)

        print("Converted:", nii_path)

