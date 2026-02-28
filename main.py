"""
====================================================
  College Attendance Analysis System
  BSc Computer Science — Group Project
====================================================
  Authors  : Group Members (update with your names)
  Language : Python 3.x
  Modules  : pandas, numpy, matplotlib, seaborn,
             reportlab, openpyxl
====================================================
"""

import sys, os

# Make sure modules/ is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "modules"))

from data_generator  import generate_students, generate_attendance, save_data
from analysis        import (load_data, preprocess, student_attendance_summary,
                              students_below_threshold, classes_needed_to_reach,
                              department_summary, subject_summary, monthly_trend,
                              weekly_trend, daywise_trend, semester_summary,
                              faculty_summary, gender_analysis, overall_stats)
from visualizer      import (plot_department_bar, plot_status_pie, plot_monthly_trend,
                              plot_daywise, plot_subject_heatmap,
                              plot_attendance_histogram, plot_semester_comparison,
                              plot_defaulters, plot_gender, plot_scatter_classes_vs_pct)
from report_generator import generate_pdf_report, generate_excel_report

# ─────────────────────────────────────────────────────────────────
# STEP 1 — Generate / Load Data
# ─────────────────────────────────────────────────────────────────

print("\n" + "="*55)
print("  COLLEGE ATTENDANCE ANALYSIS SYSTEM")
print("="*55)

if not os.path.exists("data/students.csv"):
    print("\n[→] Generating sample data …")
    students_df    = generate_students(n_per_dept=25)
    attendance_raw = generate_attendance(students_df,
                                         start_date="2024-01-01",
                                         end_date="2024-04-30")
    save_data(students_df, attendance_raw)
else:
    print("\n[→] Loading existing data …")

students_df, attendance_raw = load_data()

# ─────────────────────────────────────────────────────────────────
# STEP 2 — Pre-process
# ─────────────────────────────────────────────────────────────────

print("\n[→] Pre-processing …")
df = preprocess(attendance_raw)

# ─────────────────────────────────────────────────────────────────
# STEP 3 — Analysis
# ─────────────────────────────────────────────────────────────────

print("\n[→] Running analysis …")

student_summary  = student_attendance_summary(df)
below_75         = students_below_threshold(student_summary, threshold=75)
classes_needed   = classes_needed_to_reach(student_summary, target_pct=75)
dept_df          = department_summary(df)
subject_df       = subject_summary(df)
monthly_df       = monthly_trend(df)
weekly_df        = weekly_trend(df)
daywise_df       = daywise_trend(df)
semester_df      = semester_summary(df)
faculty_df       = faculty_summary(df)
gender_df        = gender_analysis(df, students_df)
stats            = overall_stats(df, student_summary)

# ─────────────────────────────────────────────────────────────────
# STEP 4 — Print Console Summary
# ─────────────────────────────────────────────────────────────────

print("\n" + "─"*50)
print("  OVERALL STATISTICS")
print("─"*50)
for k, v in stats.items():
    print(f"  {k:<30}: {v}")

print("\n" + "─"*50)
print("  DEPARTMENT AVERAGES")
print("─"*50)
print(dept_df.to_string(index=False))

print("\n" + "─"*50)
print(f"  STUDENTS BELOW 75% : {len(below_75)}")
print("─"*50)
print(below_75[["roll_no","name","department","attendance_pct","shortage"]].head(10).to_string(index=False))

print("\n" + "─"*50)
print("  CLASSES NEEDED TO REACH 75%  (top 10)")
print("─"*50)
print(classes_needed.head(10).to_string(index=False))

# ─────────────────────────────────────────────────────────────────
# STEP 5 — Generate Charts
# ─────────────────────────────────────────────────────────────────

print("\n[→] Generating charts …")
chart_paths = [
    plot_department_bar(dept_df),
    plot_status_pie(student_summary),
    plot_monthly_trend(monthly_df),
    plot_daywise(daywise_df),
    plot_subject_heatmap(subject_df),
    plot_attendance_histogram(student_summary),
    plot_semester_comparison(semester_df),
    plot_defaulters(below_75, top_n=10),
    plot_gender(gender_df),
    plot_scatter_classes_vs_pct(student_summary),
]
print(f"[✔] {len(chart_paths)} charts saved to /charts/")

# ─────────────────────────────────────────────────────────────────
# STEP 6 — Generate Reports
# ─────────────────────────────────────────────────────────────────

print("\n[→] Generating reports …")
pdf_path   = generate_pdf_report(stats, dept_df, subject_df,
                                  below_75, monthly_df, semester_df,
                                  gender_df, chart_paths)
excel_path = generate_excel_report(student_summary, dept_df, subject_df,
                                    below_75, gender_df)

print("\n" + "="*55)
print("  ALL DONE! Files generated:")
print("="*55)
print(f"  📊 Charts  : charts/  ({len(chart_paths)} files)")
print(f"  📄 PDF     : {pdf_path}")
print(f"  📗 Excel   : {excel_path}")
print("="*55 + "\n")
