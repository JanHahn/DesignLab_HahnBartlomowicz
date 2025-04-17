# 🔐 Smart Locker System using Raspberry Pi

A smart locker system designed for secure item storage and retrieval, combining Python software with hardware components such as electromagnetic locks and sensors — all managed by a Raspberry Pi.

<p align="center">
  <img src="https://github.com/user-attachments/assets/391d4a2c-2081-484e-8d96-f2a9102ba023" width="400"/>
</p>

## 📅 Project Info

**Authors:** Tomasz Bartłomowicz, Jan Hahn  
**Technologies:** Python, PyQt5, Raspberry Pi GPIO, SMTP  
**Category:** IoT, Embedded Systems, GUI

---

## 🧠 Overview

This project implements a **Smart Locker System** that allows users to safely store and retrieve items using unique unlock codes sent via email. Designed with a blend of **hardware reliability** and **software simplicity**, this solution has potential real-world applications in:

- 📦 Package delivery lockers  
- 🏫 Campus or office storage  
- 🤝 Contactless drop-off/pick-up points  

---

## 🧰 Hardware Components

- **Raspberry Pi 4B (4GB)**
- **Waveshare 7" IPS Touchscreen** (1024×600)
- **12V Electromagnetic Locks** (×2)
- **12V DC Power Supply**
- **High-Power Relays** (×2)
- **L7805ABV 5V Voltage Regulator**

🔌 Power supply:  
12V DC → Voltage Regulator → 5V for Raspberry Pi  
🔁 GPIO pins control relays that toggle lock states (open/close).

## 🧩 Block Diagram

![image](https://github.com/user-attachments/assets/0bc180da-9938-4655-8a8e-e3fafe4a3bee)

---

## 🛠️ Construction

The physical locker is built from **high-quality wood** for durability and sleek appearance.  
**Locker dimensions:**
- Width: 34 cm  
- Height: 26 cm  
- Depth: 30 cm

---

## 🖥️ Software Architecture

All code is written in **Python**, divided into:

### 🔧 Backend

Responsible for locker control logic and communication.

**Modules:**
- `backend.py` — Initializes GPIO, handles command loop  
- `locker.py` — Locker class to control individual units  
- `file_handler.py` — Reads/writes locker states to file  
- `mail_sender.py` — Sends unlock codes via SMTP  
- `codes.txt` — Stores active access codes

### 🎨 Frontend (PyQt5 GUI)

User-facing interface for storing or retrieving items.

**UI Modules:**
- `main_window.py`
- `store.py`
- `pick_up.py`
- `enter_email.py`
- `enter_code.py`
- `email_confirmation.py`
- `wrong_code.py`
- `locked_successfully.py`
- `opened_successfully.py`

**Main Launcher:**
- `main.py` — Starts GUI and backend in separate processes using queues

---

## ⚙️ How It Works

1. User selects **STORE** or **PICK UP**
2. System checks locker availability
3. For storing: user enters email → receives code
4. For pickup: user enters received code
5. If the code is valid → **locker opens automatically**

---

## 🚀 Future Improvements

- 📲 **QR code** authentication for faster access  
- 📱 **Mobile app** for remote locker interaction  
- 🧑‍💻 **Admin dashboard** to manage users & lockers  
- 🧩 Better **error handling** and **scalability**

---

