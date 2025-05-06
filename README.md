# Plate Recognition System

## Description

An automatic license plate recognition (ALPR) system using computer vision. It is designed for vehicle access control in gated communities or private residential areas.

## Features

- Real-time license plate detection with YOLOv5.
- OCR-based character recognition.
- Vehicle and access logging with SQLite.
- WhatsApp notifications using Twilio API.

## Technologies Used

- Python
- YOLOv5
- OCR (Tesseract)
- SQLite
- Twilio API for WhatsApp

## Installation

```bash
git clone https://github.com/CamJMend/placas_coto.git
cd placas_coto
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Main Files
- main.py: Entry point of the system.
- detect.py: Handles license plate detection.
- ocr.py: Extracts text from detected plates.
- database.py: Manages SQLite database operations.
- whatsapp.py: Sends WhatsApp notifications.
