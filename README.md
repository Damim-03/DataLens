<div align="center">

# 🔮 DataLens  
**Smart Excel Data Analyzer with Python GUI**

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green?logo=qt&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-purple)

> 🖥️ تطبيق Python بواجهة رسومية يساعدك على **تحليل البيانات من ملفات Excel** بطريقة سهلة وجذابة.

</div>

---

## ✨ المميزات
✅ استيراد بيانات Excel كاملة (مع القيم الفارغة).  
✅ عرض البيانات في جدول رسومي داخل التطبيق.  
✅ تحليل البيانات وإنشاء تقرير **Profiling Report**.  
✅ اقتراح ومعالجة القيم الفارغة (Data Cleaning).  
✅ توليد إحصائيات ووصف شامل للبيانات.  
✅ رسومات بيانية (📊 Pie, 📈 Bar, 📉 Line).  
✅ تصدير النتائج إلى **Excel** أو **PDF**.  

---

## 🏗️ هيكل المشروع (MVC)
```bash
DataLens/
│
├─ .venv/                     
├─ main.py                    # نقطة البداية لتشغيل التطبيق
├─ ui/
│   └─ main_window.ui         # واجهة Qt Designer
├─ modules/
│   └─ ui_main_window.py      # ملف Python الناتج من تحويل .ui
├─ model/
│   └─ data_model.py          # حفظ البيانات أو الحالة
├─ controller/
│   └─ main_controller.py     # منطق التحكم
└─ view/
    └─ main_view.py           # واجهة المستخدم
        # ملف التوثيق


⚙️ التثبيت والاستخدام
1️⃣ استنساخ المشروع

git clone https://github.com/YourUsername/DataLens.git
cd DataLens

2️⃣ إنشاء بيئة افتراضية (اختياري)
Windows:

python3.11 -m venv venv
.venv\Scripts\activate

Linux / Mac:

python3.11 -m venv venv
source venv/bin/activate

3️⃣ تثبيت المكتبات

pip install -r requirements.txt

أو يدويًا:
pip install PySide6 pandas openpyxl ydata-profiling matplotlib seaborn reportlab xlsxwriter

# تثبيت PyQt6
pip install PyQt6

# (اختياري) تثبيت Qt Designer مع الأدوات
pip install pyqt6-tools

4️⃣ تشغيل التطبيق
python datalens/main.py


🚀 المزايا القادمة

📡 استيراد البيانات من قواعد بيانات SQL.

📊 إنشاء Dashboards تفاعلية.

🤖 إضافة خوارزميات Machine Learning بسيطة للتوقع.
