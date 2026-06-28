# Cell Segmentation and Tracking using nnU-Net

This repository contains my work on **cell segmentation and tracking** using the [nnU‑Net framework](https://github.com/MIC-DKFZ/nnUNet).  
The project explores automated biomedical image segmentation, focusing on cell datasets, preprocessing, training, and evaluation.

---

## 📌 What I Did
- Cloned and set up the **nnU‑Net v2** repository in my workspace.
- Prepared the dataset following nnU‑Net’s strict folder and naming conventions:
  - `imagesTr` → training images
  - `labelsTr` → corresponding segmentation labels
  - `imagesTs` → test images
  - `labelsTs` → test labels
- Ran preprocessing, experiment planning, and training pipelines.
- Evaluated the model performance using Dice score and other metrics.
- Documented the workflow for reproducibility.

---

## 🧩 References
- **nnU‑Net: Self-adapting Framework for Biomedical Image Segmentation**  
  [https://github.com/MIC-DKFZ/nnUNet](https://github.com/MIC-DKFZ/nnUNet)  
  Paper: Isensee et al., *Nature Methods* (2021)  
  DOI: [10.1038/s41592-020-01008-z](https://doi.org/10.1038/s41592-020-01008-z)

---

## 📷 Training Results
--loss curves, Dice scores and segmentation outputs:
<img width="935" height="697" alt="Screenshot_27-6-2026_141447_colab research google com" src="https://github.com/user-attachments/assets/5c928984-8cd7-41e7-a8c5-a21bce01eae7" />



## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/Likitha-sd/Cell_Segmentation_and_Tracking_using_Mamba.git
