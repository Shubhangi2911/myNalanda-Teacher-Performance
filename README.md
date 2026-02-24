🚀 myNalanda AI Analytics Dashboard
Project Overview
This is a professional, high-end HR Analytics Dashboard built using Python and Streamlit. It provides the administration of Ideal International School with deep insights into teacher performance, compliance metrics, and attrition risks.

🔑 Login Credentials
Username: admin

Password: 1234

Role: myN_Admin

🛠️ Technical Features
Dynamic Data Loading: The dashboard automatically reads data from Teacher_Dataset.csv.

Interactive Performance Metrics:

KPI Cards: Real-time tracking of Total Teachers (55), Attrition Risk, and Late Counts.

Gauges: Visualization for Compliance Scores and Benchmarks.

Performance Landscape: Area charts showing school-wide performance trends.

Teacher Deep-Dive: Individual profile analysis with dynamic Status Badges (Active, Monitoring, At Risk).

Error Handling: Robust CSV parsing with automated skip-logic for formatting errors.

📊 Meaningful Insights (Dataset of 55 Teachers)
Staff Overview: A comprehensive review of 55 faculty members across various departments.

Attrition Analysis: High-risk candidates are identified based on compliance scores below 1.5, often linked to "lack of interest" or "external opportunities".

Performance Leaders: Departments like Math and Physics show the highest compliance stability.

Behavioral Correlation: Analysis shows a direct link between "Late Arrivals" and decreasing "Compliance Scores" among at-risk staff.

📂 Folder Organization
Plaintext
Shubhangi Salve_9766250771/
├── main.py              # Application logic and UI
├── Teacher_Dataset.csv  # Full dataset of 55 teachers
├── requirements.txt     # Necessary Python libraries
└── README.md            # Documentation and Insights
🚀 Setup Instructions
Extract the folder.

Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
python -m streamlit run main.py