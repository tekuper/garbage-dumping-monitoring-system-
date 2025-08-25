#  Garbage Monitoring System - YOLOv8 Fine-tuning & Evaluation

##  Project Overview

This project focuses on **fine-tuning and evaluating the YOLOv8 object detection model** for a **Garbage Monitoring System**. The model detects objects such as people, litter, garbage, and trash in images and videos, assisting in waste management and environmental monitoring.

---

## 📂 Project Structure

```bash
📁 garbage_monitoring_system/
│── 📁 __pycache__/              # Compiled Python files
│── 📁 Dataset_processing/       # Data processing scripts
│── 📁 littering_project/        # YOLO training and detection
│── 📁 outputted_images/         # Images with detections
│── 📁 test_image/               # Sample images for testing
│── 📄 .env                      # Environment variables
│── 📄 bbox_utils.py             # Bounding box utilities
│── 📄 convert_to_jpg.py         # Image conversion script
│── 📄 copy_files.py             # Script for copying files
│── 📄 detect_object.py          # Object detection script
│── 📄 Detection.py              # Main detection script
│── 📄 Finetuning & Evaluation.ipynb  # Main notebook
│── 📄 littering_data_processor.py # Data preprocessing script
│── 📄 process_images.py         # Image processing utilities
│── 📄 process_littering_data.py # Data processing for littering dataset
│── 📄 requirements.txt          # Required dependencies
│── 📄 README.md                 # Project documentation
│── 📄 yolov8n.pt                # Pre-trained YOLOv8 model
```

---

##  Installation

To run this project, you need to set up a Python environment and install dependencies.

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/tekuper/garbage_monitoring_system.git
cd garbage_monitoring_system
```

### **2️⃣ Create a Virtual Environment (Recommended)**

Using Conda:

```bash
conda create --name garbage_env python=3.8 -y
conda activate garbage_env
```

Or using venv:

```bash
python -m venv garbage_env
source garbage_env/bin/activate  # Mac/Linux
./garbage_env/Scripts/activate   # Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

##  How to Use the Model

### **1️⃣ Load the Trained Model**

The trained YOLOv8 model (`best.onnx`) is located in the `littering_project/weights/` folder.

```python
from ultralytics import YOLO

# Load the trained model
model = YOLO("littering_project/weights/best.onnx")
```

### **2️⃣ Run Inference on an Image**

To detect objects in an image:

```python
image_path = "test_image/sample.jpg"
results = model(image_path)
```

### **3️⃣ Save and Display the Detection Results**

```python
from PIL import Image
import matplotlib.pyplot as plt

# Plot detections
result = results[0]
detected_img = result.plot()
output_path = "outputted_images/sample_detected.jpg"
Image.fromarray(detected_img).save(output_path)

# Display the image
img = Image.open(output_path)
plt.figure(figsize=(10,6))
plt.imshow(img)
plt.axis("off")
plt.show()
```

---

##  How to Use the Project

### **1️⃣ Running the Full Pipeline**

To **process images, run inference, and save results**, execute:

```bash
python Detection.py
```

### **2️⃣ Fine-Tuning the Model**

To **retrain YOLOv8 with a custom dataset**, update `Finetuning & Evaluation.ipynb`:

```python
from ultralytics import YOLO

# Load a pre-trained model
model = YOLO("yolov8n.pt")

# Fine-tune on custom dataset
model.train(data="data.yaml", epochs=50, imgsz=640)
```

---

##  How to Load Files

You can load images and datasets into the project by placing them in the **appropriate directories**:

- **Images for detection:** `test_image/`
- **Images with detection results:** `outputted_images/`
- **Datasets for training:** `Dataset_processing/`

To manually load an image for testing:

```python
from PIL import Image
image_path = "test_image/sample.jpg"
img = Image.open(image_path)
img.show()
```

---

##  Troubleshooting

If you encounter issues like missing DLLs or package errors:

1. **Ensure OpenCV and dependencies are properly installed:**
   ```bash
   conda install -c conda-forge opencv
   pip install ultralytics
   ```
2. **Check Python environment:**
   ```bash
   conda activate garbage_env
   python -c "import cv2; print(cv2.__file__)"
   ```
3. **If DLL errors persist, install:**
   - [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

---


##  Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

For major changes, please open an issue first to discuss your ideas.

---

##  Contact

For questions or collaborations, reach out via: 📧 Email: [Mail](mailto\:assadihamiid@gmail.com)\
 GitHub: [ GitHub ](https://github.com/tekuper/garbage_monitoring_system)

---

🚀 **Happy Coding!**

