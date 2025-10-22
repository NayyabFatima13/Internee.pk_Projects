
# PERFORMANCE METRICS AUTOMATION SCRIPT
import pandas as pd
import numpy as np
from datetime import datetime

def generate_monthly_report(month, year=2024):
    """Generate monthly performance report for supervisors"""
    
    # Load datasets
    monthly_df = pd.read_csv('monthly_performance_metrics.csv')
    task_df = pd.read_csv('task_level_metrics.csv')
    feedback_df = pd.read_csv('detailed_feedback.csv')
    
    # Filter for specific month
    monthly_data = monthly_df[(monthly_df['month'] == month) & (monthly_df['year'] == year)]
    
    # Generate summary statistics
    report = {
        'report_month': f"{year}-{month:02d}",
        'total_interns': monthly_data['intern_id'].nunique(),
        'avg_completion_rate': monthly_data['completion_rate'].mean(),
        'avg_quality_score': monthly_data['avg_quality_score'].mean(),
        'avg_performance_score': monthly_data['monthly_performance_score'].mean(),
        'top_performing_dept': monthly_data.groupby('department')['monthly_performance_score'].mean().idxmax()
    }
    
    # Department-wise breakdown
    dept_breakdown = monthly_data.groupby('department').agg({
        'monthly_performance_score': 'mean',
        'completion_rate': 'mean',
        'intern_id': 'count'
    }).round(2)
    
    return report, dept_breakdown

def calculate_kpi_trends():
    """Calculate month-over-month KPI trends"""
    monthly_df = pd.read_csv('monthly_performance_metrics.csv')
    
    trends = monthly_df.groupby('month').agg({
        'completion_rate': 'mean',
        'avg_quality_score': 'mean', 
        'monthly_performance_score': 'mean'
    })
    
    return trends

# Example usage
if __name__ == "__main__":
    # Generate report for latest month
    report, breakdown = generate_monthly_report(6)
    print("Monthly Performance Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
    
    print("\nDepartment Breakdown:")
    print(breakdown)
