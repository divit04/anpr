

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import cv2
import torch
import easyocr
 
from PIL import Image, ImageTk
import numpy as np
import re
import tkinter as tk
from tkinter import Label, Button
from ultralytics import YOLO
import os


# 🧠 EasyOCR Fallback
reader = easyocr.Reader(['en'])

# ✅ Indian Plate Format Filter
def is_valid_plate(text):
    pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$'
    return re.match(pattern, text) is not None

# 🔍 Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp9/weights/best.pt')

# 🖼️ GUI
root = tk.Tk()
root.title("Hybrid ANPR (Gemini + EasyOCR)")
label = Label(root)
label.pack()

# 🎮 Buttons and State
stop_on_detect = False
plate_output = tk.StringVar()
plate_output.set("Detected Plate: None")

output_label = Label(root, textvariable=plate_output, font=("Arial", 16))
output_label.pack()

def reset_detection():
    global stop_on_detect
    stop_on_detect = False
    plate_output.set("Detected Plate: None")

Button(root, text="Reset Detection", command=reset_detection).pack(pady=10)

cap = cv2.VideoCapture(0)

def detect_and_display():
    global stop_on_detect
    if stop_on_detect:
        root.after(100, detect_and_display)
        return

    ret, frame = cap.read()
    if not ret:
        root.after(10, detect_and_display)
        return

    results = model(frame)
    boxes = results.xyxy[0].cpu().numpy()

    for *xyxy, conf, cls in boxes:
        x1, y1, x2, y2 = map(int, xyxy)
        plate_img = frame[y1:y2, x1:x2]

        if plate_img.size == 0:
            continue


        # 🔁 Use EasyOCR only (Gemini removed)
        easy_text = reader.readtext(plate_img, detail=0)
        text = easy_text[0] if easy_text else ""

        text = ''.join(filter(str.isalnum, text.upper()))
        if is_valid_plate(text):
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            print(f"[DETECTED] Plate: {text}")
            plate_output.set(f"Detected Plate: {text}")
            stop_on_detect = True

    # GUI Frame Update
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(rgb).resize((800, 600))
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    root.after(1, detect_and_display)

# 🚀 Start Loop
detect_and_display()
root.mainloop()

# 🧹 Cleanup
cap.release()
cv2.destroyAllWindows()
