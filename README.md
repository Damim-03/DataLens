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
│── data/                 # ملفات Excel
│── reports/              # نتائج / تقارير PDF و Excel
│── datalens/
│   ├── model/            # منطق معالجة البيانات (pandas, profiling..)
│   ├── view/             # واجهة المستخدم (PySide6 UI)
│   ├── controller/       # الربط بين model و view
│   ├── main.py           # ملف التشغيل الرئيسي
│
│── requirements.txt      # مكتبات المشروع
│── README.md             # ملف التوثيق


⚙️ التثبيت والاستخدام
1️⃣ استنساخ المشروع

git clone https://github.com/YourUsername/DataLens.git
cd DataLens

2️⃣ إنشاء بيئة افتراضية (اختياري)
Windows:

python -m venv venv
venv\Scripts\activate

Linux / Mac:

python3 -m venv venv
source venv/bin/activate

3️⃣ تثبيت المكتبات

pip install -r requirements.txt

أو يدويًا:
pip install PySide6 pandas openpyxl ydata-profiling matplotlib seaborn reportlab xlsxwriter

4️⃣ تشغيل التطبيق
python datalens/main.py


🚀 المزايا القادمة

📡 استيراد البيانات من قواعد بيانات SQL.

📊 إنشاء Dashboards تفاعلية.

🤖 إضافة خوارزميات Machine Learning بسيطة للتوقع.
