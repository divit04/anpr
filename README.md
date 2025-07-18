
# 🚗 Automatic Parking Lot System using YOLOv5 & EasyOCR

A real-time Automatic Number Plate Recognition (ANPR) system designed for smart parking management using deep learning and OCR.

## 🔧 Features

- 🚘 YOLOv5-based number plate detection  
- 🔤 EasyOCR for multilingual plate recognition (including Indian formats)  
- ✅ Regex filtering for valid Indian number plates  
- 🖼️ Live GUI using Tkinter for real-time display and interaction  
- 🗃️ SQLite database integration to manage registered vehicles and logs  
- 🔁 Stop-on-detection logic and Reset functionality  

## 🧱 Tech Stack

- Python 3.9+  
- OpenCV  
- YOLOv5 (PyTorch)  
- EasyOCR  
- SQLite3  
- Tkinter (GUI)  

## 📂 Folder Structure

```
📁 anpr_project/
 ┣ 📄 main.py               # Main GUI + detection logic  
 ┣ 📄 database.py           # SQLite DB setup and registration  
 ┣ 📁 yolov5/               # YOLOv5 model folder  
 ┃ ┗ 📁 runs/train/exp*/... # Trained weights  
 ┣ 📁 data/                 # Sample plate images or video streams  
 ┣ 📄 README.md  
 ┗ 📄 requirements.txt      # Dependencies list  
```

## 🛠️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/yourusername/automatic-parking-lot.git
cd automatic-parking-lot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the database setup:
```bash
python database.py
```

4. Launch the GUI and detection:
```bash
python main.py
```

## 📸 Demo

![Demo Screenshot](screenshot.png)

## 📌 Notes

- Ensure your webcam is connected and working.  
- The system currently uses YOLOv5 + EasyOCR only. Gemini/Google Vision can be integrated if needed.  
- Regex used: ^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$  

## 📄 License

This project is licensed under the MIT License.

---

© 2025 Divit Dwivedi
