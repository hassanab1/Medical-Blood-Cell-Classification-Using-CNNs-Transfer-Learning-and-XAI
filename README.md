# 🩸 Medical Blood Cell Classification Using CNNs, Transfer Learning and XAI

A deep learning coursework project for classifying medical blood cell images using custom Convolutional Neural Networks (CNNs), pretrained CNN models, and Explainable Artificial Intelligence (XAI).

The project uses the **AneRBC blood smear image dataset** to classify blood cell images into their available classes. It compares custom CNN architectures with transfer learning models and uses Grad-CAM to explain how the best models make their predictions.

---

## 📁 Project Structure

```text
medical-blood-cell-classification/
│
├── data/
│   ├── raw/                 # Original downloaded dataset
│   ├── processed/           # Cleaned and prepared dataset
│   └── splits/              # Train, validation, and test split files
│
├── notebooks/
│   └── medical_image_classification.ipynb
│
├── scripts/
│   ├── download_data.py         # Dataset download or placement instructions
│   ├── validate_data.py         # Image and label validation checks
│   ├── preprocess_data.py       # Image preprocessing pipeline
│   ├── train_custom_cnn.py      # Custom CNN training
│   ├── train_pretrained.py      # Transfer learning training
│   ├── evaluate_models.py       # Model evaluation and metrics
│   └── generate_xai.py          # Grad-CAM visualizations
│
├── models/                      # Saved trained model weights
│
├── outputs/
│   ├── figures/                 # Learning curves and confusion matrices
│   ├── metrics/                 # Classification reports and scores
│   └── xai/                     # Grad-CAM output images
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Tools and Libraries

| Library | Purpose |
|---|---|
| PyTorch | Building, training, and testing deep learning models |
| torchvision | Image transforms, datasets, and pretrained CNN models |
| numpy | Numerical operations |
| pandas | Data handling and class-distribution analysis |
| matplotlib | Learning curves, confusion matrices, and XAI visualizations |
| scikit-learn | Classification report, precision, recall, F1-score, and train/test split |
| Pillow | Image loading and corrupted image validation |
| Captum | Explainable AI methods for PyTorch models |

---

## 📊 Project Overview

This project develops an end-to-end medical image classification pipeline using blood smear cell images. The workflow is divided into five main tasks required by the coursework.

### ⚙️ Task 1 — Dataset Loading, Validation and Preprocessing

The dataset is downloaded or manually placed inside the `data/raw/` folder.

The following validation checks are performed:

- Detecting unreadable or corrupted image files
- Verifying that image classes are mapped correctly
- Checking the number of images in each class
- Identifying duplicate or invalid files where applicable
- Creating a class-distribution summary

Images are then prepared through:

- Resizing images to a fixed size
- Converting images into tensors
- Normalizing pixel values
- Applying optional data augmentation to training images
- Creating reproducible train, validation, and test splits using a deterministic random seed
- Using stratified splitting where applicable to maintain balanced class distributions

### 🧠 Task 2 — Custom CNN Architectures

Three custom CNN models are developed and compared:

| Model | Description |
|---|---|
| Custom CNN-3 | CNN with 3 convolutional layers |
| Custom CNN-4 | CNN with 4 convolutional layers |
| Custom CNN-5 | CNN with 5 convolutional layers |

Each CNN includes:

- Convolutional layers with increasing filters
- ReLU activation functions
- Max pooling layers
- Dropout layers for regularization
- Fully connected classification layers
- Softmax-based class prediction

Each model is trained on the training set and validated using the validation set. The following outputs are generated:

- Training & validation loss/accuracy curves
- Classification reports (Precision, Recall, F1-score)
- Confusion matrices

### 🚀 Task 3 — Transfer Learning with Pretrained CNNs

Three pretrained CNN models are used for transfer learning:

| Model | Purpose |
|---|---|
| MobileNetV2 | Lightweight and efficient pretrained CNN |
| SqueezeNet | Compact pretrained CNN with fewer parameters |
| ResNet18 | Residual network for deeper feature learning |

For each pretrained model:

- The pretrained backbone is frozen initially.
- The original classifier head is replaced according to the dataset classes.
- Only the new top classification layers are trained.
- The best model may optionally be fine-tuned by unfreezing the final block for a short second training phase.

### 🔍 Task 4 — Explainable AI (XAI)

Grad-CAM is applied to the best-performing custom CNN model and the best-performing pretrained CNN model. Grad-CAM produces heatmaps that highlight the regions of the blood cell image that most influenced each prediction.

The visualizations are used to examine:

- Whether the model focuses on the blood cell itself
- Whether predictions depend on relevant cell characteristics
- Whether the model is being influenced by background noise or irrelevant image regions
- Whether pretrained models provide more meaningful attention compared to custom CNNs

Generated XAI outputs are saved inside `outputs/xai/`.

---

## 📈 Evaluation Metrics

Every trained model is evaluated using:

- Accuracy, Precision, Recall, and F1-score
- Detailed classification reports and confusion matrices
- Training and validation learning curves

The final comparison focuses on the trade-offs between shallow versus deeper custom CNNs, custom architectures versus transfer learning models, and model accuracy versus model interpretability through Grad-CAM.

---

## 📦 Dataset

**Dataset Name:** AneRBC — Macroscopic Blood Smear Cell Image Dataset

The dataset contains medical blood smear images representing different blood cell classes. Depending on the available version of the dataset, classes may include:

- Red Blood Cells (RBC)
- White Blood Cells (WBC)
- Platelets
- Other blood cell categories or WBC subtypes

> 📝 **Note:** The exact class names, image counts, and dataset source link will be documented here after the dataset is downloaded and validated.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd YOUR_REPOSITORY_FOLDER_NAME
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 3. Install dependencies

```bash
pip install torch torchvision numpy pandas matplotlib scikit-learn pillow captum jupyter
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

Then open: `notebooks/medical_image_classification.ipynb`

---

## ▶️ Running the Project

Run the individual pipeline stages via the terminal:

```bash
# Dataset validation
python scripts/validate_data.py

# Train custom CNN models
python scripts/train_custom_cnn.py

# Train pretrained CNN models
python scripts/train_pretrained.py

# Evaluate trained models
python scripts/evaluate_models.py

# Generate Grad-CAM visualizations
python scripts/generate_xai.py
```

---

## 🧾 Git Commit Workflow

This coursework requires distinct commits after every subtask.

Example workflow commands:

```bash
git add .
git commit -m "Task1.1: Add dataset download instructions"
git push
```

Standardized commit message roadmap:

- `Task1.1: Add dataset download instructions`
- `Task1.2: Implement image validation and class distribution checks`
- `Task1.3: Add preprocessing and normalization pipeline`
- `Task1.4: Create stratified train validation test splits`
- `Task2.1: Implement custom 3, 4, and 5 layer CNNs`
- `Task2.2: Train and validate custom CNN models`
- `Task2.3: Evaluate custom CNN models with confusion matrices`
- `Task3.1: Add MobileNetV2 transfer learning model`
- `Task3.2: Add SqueezeNet transfer learning model`
- `Task3.3: Add ResNet18 transfer learning model`
- `Task4.1: Generate Grad-CAM for best custom CNN`
- `Task4.2: Generate Grad-CAM for best pretrained CNN`
- `Task5.1: Add final report and project documentation`

---

## 👤 Author

- **Name:** Hassan Abdurehman
- **RN:** 303-221002
- **Programme:** BS Artificial Intelligence
- **Course:** Deep Learning

---

## 📌 Coursework Requirements Covered

- [x] Dataset loading, cleaning, validation, and preprocessing
- [x] Deterministic train, validation, and test split
- [x] Three custom CNN architectures with 3, 4, and 5 convolutional layers
- [x] Three pretrained CNN transfer learning models
- [x] Model evaluation using precision, recall, F1-score, and confusion matrices
- [x] Grad-CAM explainability for one custom and one pretrained model
- [x] Git-based development with meaningful, structured commits
- [x] Final Jupyter Notebook, README, and coursework report
