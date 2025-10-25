
-- KEY BEHAVIOR ANALYSIS QUERIES FOR INTERNEE.PK

-- 1. CONVERSION FUNNEL ANALYSIS
SELECT 
    funnel_stage,
    COUNT(DISTINCT user_id) as users_reached,
    LAG(COUNT(DISTINCT user_id)) OVER (ORDER BY 
        CASE funnel_stage 
            WHEN 'Awareness' THEN 1
            WHEN 'Consideration' THEN 2 
            WHEN 'Evaluation' THEN 3
            WHEN 'Application' THEN 4
        END) as previous_stage_users,
    ROUND((1 - COUNT(DISTINCT user_id) * 1.0 / LAG(COUNT(DISTINCT user_id)) OVER (ORDER BY 
        CASE funnel_stage 
            WHEN 'Awareness' THEN 1
            WHEN 'Consideration' THEN 2 
            WHEN 'Evaluation' THEN 3
            WHEN 'Application' THEN 4
        END)) * 100, 2) as dropoff_rate
FROM conversion_funnel 
GROUP BY funnel_stage
ORDER BY 
    CASE funnel_stage 
        WHEN 'Awareness' THEN 1
        WHEN 'Consideration' THEN 2 
        WHEN 'Evaluation' THEN 3
        WHEN 'Application' THEN 4
    END;

-- 2. PAGE PERFORMANCE AND EXIT POINTS
SELECT 
    page_url,
    COUNT(*) as pageviews,
    ROUND(AVG(time_on_page_seconds), 2) as avg_time_seconds,
    ROUND(SUM(CASE WHEN is_exit = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as exit_rate_percent
FROM pageview_analytics 
GROUP BY page_url
ORDER BY exit_rate_percent DESC;

-- 3. USER SEGMENT BEHAVIOR COMPARISON
SELECT 
    a.user_segment,
    COUNT(DISTINCT a.user_id) as total_users,
    ROUND(AVG(s.pages_viewed), 2) as avg_pages_per_session,
    ROUND(AVG(s.session_duration_seconds) / 60, 2) as avg_session_minutes,
    ROUND(SUM(CASE WHEN s.application_submitted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(DISTINCT a.user_id), 2) as conversion_rate
FROM applicant_demographics a
JOIN user_sessions s ON a.user_id = s.user_id
GROUP BY a.user_segment
ORDER BY conversion_rate DESC;

-- 4. TRAFFIC SOURCE EFFECTIVENESS
SELECT 
    traffic_source,
    COUNT(DISTINCT user_id) as visitors,
    ROUND(SUM(CASE WHEN application_submitted = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(DISTINCT user_id), 2) as conversion_rate,
    ROUND(AVG(pages_viewed), 2) as avg_pages_per_visit
FROM applicant_demographics a
JOIN user_sessions s ON a.user_id = s.user_id
GROUP BY traffic_source
ORDER BY conversion_rate DESC;

-- 5. BOTTLENECK IDENTIFICATION (High exit pages)
SELECT 
    page_url,
    exit_rate_percent,
    pageview_count,
    RANK() OVER (ORDER BY exit_rate_percent DESC) as bottleneck_rank
FROM (
    SELECT 
        page_url,
        ROUND(SUM(CASE WHEN is_exit = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as exit_rate_percent,
        COUNT(*) as pageview_count
    FROM pageview_analytics 
    GROUP BY page_url
) WHERE exit_rate_percent > 30.0
ORDER BY bottleneck_rank;
