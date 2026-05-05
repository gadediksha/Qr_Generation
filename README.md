
# 🚀 Flask QR Code Generator

A modern and user-friendly **QR Code Generator Web Application** built with **Flask (Python)**.
This application allows users to generate QR codes for **text, URLs, and UPI payments** quickly and efficiently.

---

## ✨ Features

* 🔤 Generate QR Code from Text
* 🌐 Generate QR Code from URL
* 💳 Generate UPI Payment QR Code
* 🎨 Clean and responsive UI
* ⚡ Fast and lightweight application

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Library:** qrcode (PIL)

---

## 📂 Project Structure

```
Qr_Generation/
│
├── app.py
├── qr_logic.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── qrcodes/
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/gadediksha/Qr_Generation.git
cd Qr_Generation
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

*(If not working, use:)*

```
pip install flask qrcode[pil]
```

---

### 3. Run the application

```
python app.py
```

---

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📸 Usage

1. Select QR type (Text / URL / Payment)
2. Enter the required details
3. Click **Generate QR**
4. QR code will be displayed instantly

---

## 💳 UPI QR Format

```
upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=INR
```

---

## 📌 Notes

* QR codes are stored in `static/qrcodes/`
* Make sure this folder exists before running the app

---

## 🚧 Future Improvements

* 📥 Download QR Code
* 🎨 Custom QR colors
* 🌙 Dark mode
* 📜 QR history

---

## 👩‍💻 Author

**Diksha**
GitHub: https://github.com/gadediksha

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
