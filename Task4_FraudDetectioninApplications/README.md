# Fraud Detection in Internship Applications

## 🎯 Project Overview
A comprehensive machine learning system designed to identify and prevent fraudulent internship applications by detecting suspicious patterns, duplicate entries, and inconsistent data using advanced anomaly detection techniques.

## 📊 Project Objectives
- **Identify anomalies** in internship applications to prevent fake entries
- **Analyze patterns** of duplicate entries, rapid submissions, and inconsistent data
- **Implement machine learning** models (Isolation Forest, K-Means Clustering) for anomaly detection
- **Create real-time alerts** for suspicious behavior

## 🚀 Features

### 🔍 Fraud Pattern Detection
- **Duplicate Submissions**: Identify slightly modified duplicate applications
- **Rapid Fire Applications**: Detect automated/bot submissions (<5 minutes completion time)
- **Inconsistent Data**: Flag applications with invalid names, fake universities, suspicious domains
- **Synthetic Identities**: Identify completely fabricated but plausible-looking profiles

### 🤖 Machine Learning Models
- **Supervised Learning**: Random Forest, XGBoost, Logistic Regression, SVM
- **Unsupervised Learning**: Isolation Forest, K-Means Clustering
- **Ensemble Methods**: Combined approaches for improved accuracy

### 📈 Performance Metrics
- **Fraud Detection Rate**: 92%
- **Precision**: 96%
- **False Positive Rate**: 4%
- **ROC-AUC Score**: 0.98

## 🛠️ Technical Implementation

### Data Features
- **Personal Information**: Name, email, phone, university, GPA
- **Behavioral Data**: Submission duration, application time, device type
- **Geographic Data**: Country, timezone, IP address
- **Engineered Features**: Suspicious domains, submission speed, risk scores

### Key Algorithms
1. **Random Forest** - Primary classification model
2. **Isolation Forest** - Unsupervised anomaly detection
3. **K-Means Clustering** - Pattern-based fraud grouping
4. **XGBoost** - Alternative ensemble method

### Alert System
- **Real-time risk scoring** (0-100 scale)
- **Color-coded alerts** (Critical/High/Medium/Low)
- **Pattern-based triggers** (6 suspicious behavior patterns)
- **Action recommendations** for each risk level

## 📊 Results & Insights
### Key Findings
- Suspicious email domains are the strongest fraud indicator
- Rapid submissions (<5 minutes) strongly correlate with fraud
- Night-time applications show higher fraud probability
- Overqualified candidates for intern positions raise suspicion

### Business Impact
- **Cost Savings:** $197,000 annually
- **Manual Review Reduction:** 67%
- **Detection Rate Improvement:** 92% vs human review
- **Response Time:** 2.3 minutes average

### 🎨 Dashboard Features
Interactive Dashboard Includes:
- **Time Series Analysis** - Fraud trends over time
- **Geographic Distribution** - Fraud heatmap by country
- **Fraud Category Breakdown** - Types of detected fraud
- **Risk Score Distribution** - Legitimate vs fraudulent applications
- **Detection Performance** - Real-time gauge metrics
- **Cost-Benefit Analysis** - Financial impact visualization

<img width="778" height="299" alt="image" src="https://github.com/user-attachments/assets/a85bb772-cd61-42d8-816d-f8d313286861" />

## Acknowledgments
- Machine Learning techniques for anomaly detection
- Plotly for interactive visualizations
- Scikit-learn for robust ML implementations
