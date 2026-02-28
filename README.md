# 🎓 College Attendance Analysis System
### BSc Computer Science — Group Project

---

## 📌 Project Overview
A complete Python-based system that **collects, analyses, visualizes, and reports** student attendance data for a multi-department college. The system produces professional PDF reports, Excel sheets, and 10 types of charts.

---

## 🗂 Project Structure

```
attendance_project/
│
├── main.py                       # ← Run this
│
├── modules/
│   ├── data_generator.py         # Generates/loads sample attendance data
│   ├── analysis.py               # All analysis functions (student, dept, subject, trend …)
│   ├── visualizer.py             # 10 chart types using matplotlib & seaborn
│   └── report_generator.py       # PDF (reportlab) + Excel (openpyxl) report builder
│
├── data/
│   ├── students.csv              # Auto-generated student records
│   └── attendance.csv            # Auto-generated attendance records
│
├── charts/                       # Auto-generated PNG charts (10 files)
│
└── reports/
    ├── Attendance_Analysis_Report.pdf
    └── Attendance_Data.xlsx
```

---

## 📦 Requirements

```
Python 3.8+
pandas
numpy
matplotlib
seaborn
openpyxl
reportlab
```

Install all dependencies:
```bash
pip install pandas numpy matplotlib seaborn openpyxl reportlab
```

---

## ▶️ How to Run

```bash
cd attendance_project
python main.py
```

---

## 🔍 Features

### 📊 Analysis Modules
| Module | What It Does |
|--------|-------------|
| `student_attendance_summary()` | Per-student attendance %, status (Critical/Low/Moderate/Good/Excellent) |
| `students_below_threshold()` | Identifies defaulters below 75% with shortage count |
| `classes_needed_to_reach()` | Calculates how many classes a student must attend to reach 75% |
| `department_summary()` | Average attendance per department |
| `subject_summary()` | Average attendance per subject per department |
| `monthly_trend()` | Month-by-month attendance trend |
| `daywise_trend()` | Day-of-week attendance pattern |
| `semester_summary()` | Semester-wise comparison |
| `faculty_summary()` | Faculty-wise attendance analysis |
| `gender_analysis()` | Male vs Female attendance comparison |

### 📈 Charts Generated
| # | Chart | Type |
|---|-------|------|
| 1 | Department-wise Average Attendance | Horizontal Bar |
| 2 | Student Attendance Status Distribution | Pie Chart |
| 3 | Monthly Attendance Trend | Line Chart |
| 4 | Day-wise Attendance Pattern | Bar Chart |
| 5 | Subject-wise Heatmap by Department | Heatmap |
| 6 | Attendance Distribution | Histogram |
| 7 | Semester-wise Comparison | Bar Chart |
| 8 | Top 10 Defaulters | Horizontal Bar |
| 9 | Gender-wise Comparison | Bar Chart |
| 10 | Classes vs Attendance % | Scatter Plot |

### 📋 Reports
- **PDF Report** — Professional 13-section report with charts, tables, and recommendations
- **Excel Workbook** — 5 sheets: All Students, Below 75%, Dept Summary, Subject Summary, Gender Analysis

---

## 👥 Group Members
*(Replace with your names)*
1. Member 1 — Roll No: XXX
2. Member 2 — Roll No: XXX
3. Member 3 — Roll No: XXX
4. Member 4 — Roll No: XXX

---

## 🛠 Technologies Used
- **Python** — Core language
- **pandas** — Data manipulation & analysis
- **numpy** — Numerical computations
- **matplotlib** — Chart plotting
- **seaborn** — Statistical visualizations
- **reportlab** — PDF report generation
- **openpyxl** — Excel file creation

---

## 📐 Formulas Used

**Attendance Percentage:**
```
attendance_pct = (classes_present / total_classes) × 100
```

**Classes needed to reach target (75%):**
```
classes_needed = ceil((target × total_classes - classes_present) / (1 - target))
```

**Shortage (classes missed beyond allowed):**
```
shortage = ceil(total_classes × 0.75) - classes_present
```

---

*Project Submitted to: Department of Computer Science*
*Academic Year: 2024-25*
