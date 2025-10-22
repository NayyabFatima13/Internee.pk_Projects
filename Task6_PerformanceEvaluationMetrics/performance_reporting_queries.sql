
-- MONTHLY PERFORMANCE REPORT QUERY
SELECT 
    department,
    month,
    AVG(completion_rate) as avg_completion_rate,
    AVG(avg_quality_score) as avg_quality_score,
    AVG(mentor_feedback_score) as avg_feedback_score,
    AVG(monthly_performance_score) as overall_score,
    COUNT(DISTINCT intern_id) as intern_count
FROM monthly_performance_metrics 
WHERE year = 2024 
GROUP BY department, month 
ORDER BY department, month;

-- TOP PERFORMERS QUERY
SELECT 
    intern_id,
    department,
    AVG(monthly_performance_score) as avg_performance_score,
    AVG(completion_rate) as avg_completion_rate
FROM monthly_performance_metrics 
GROUP BY intern_id, department 
HAVING AVG(monthly_performance_score) > 80 
ORDER BY avg_performance_score DESC;

-- TASK COMPLETION ANALYSIS
SELECT 
    task_type,
    completion_status,
    COUNT(*) as task_count,
    AVG(actual_hours) as avg_hours,
    AVG(quality_score) as avg_quality
FROM task_level_metrics 
GROUP BY task_type, completion_status 
ORDER BY task_type, completion_status;
