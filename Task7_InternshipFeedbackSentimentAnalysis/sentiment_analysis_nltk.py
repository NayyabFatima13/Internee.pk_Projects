
# INTERNSHIP FEEDBACK SENTIMENT ANALYSIS WITH NLTK

import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Download required NLTK data
nltk.download('vader_lexicon')

class FeedbackSentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text):
        """Analyze sentiment using VADER"""
        scores = self.sia.polarity_scores(text)
        
        # Classify based on compound score
        if scores['compound'] >= 0.05:
            return 'positive'
        elif scores['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'
    
    def analyze_dataset(self, df, text_column='feedback_text'):
        """Analyze entire dataset"""
        results = []
        for _, row in df.iterrows():
            text = row[text_column]
            predicted_sentiment = self.analyze_sentiment(text)
            actual_sentiment = row['sentiment_label']
            
            results.append({
                'feedback_id': row['feedback_id'],
                'text': text,
                'actual_sentiment': actual_sentiment,
                'predicted_sentiment': predicted_sentiment,
                'compound_score': self.sia.polarity_scores(text)['compound']
            })
        
        return pd.DataFrame(results)
    
    def evaluate_model(self, results_df):
        """Evaluate model performance"""
        print("=== SENTIMENT ANALYSIS RESULTS ===")
        print(f"Accuracy: {(results_df['actual_sentiment'] == results_df['predicted_sentiment']).mean():.2%}")
        print("\nClassification Report:")
        print(classification_report(results_df['actual_sentiment'], results_df['predicted_sentiment']))
        
        # Confusion Matrix
        plt.figure(figsize=(8, 6))
        cm = confusion_matrix(results_df['actual_sentiment'], results_df['predicted_sentiment'], 
                             labels=['positive', 'neutral', 'negative'])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['positive', 'neutral', 'negative'],
                   yticklabels=['positive', 'neutral', 'negative'])
        plt.title('Sentiment Analysis Confusion Matrix')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.show()

# Usage example
if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv('internship_feedback_sentiment.csv')
    
    # Initialize analyzer
    analyzer = FeedbackSentimentAnalyzer()
    
    # Analyze sentiments
    results = analyzer.analyze_dataset(df)
    
    # Evaluate performance
    analyzer.evaluate_model(results)
    
    # Sentiment distribution visualization
    sentiment_counts = results['predicted_sentiment'].value_counts()
    plt.figure(figsize=(10, 6))
    sentiment_counts.plot(kind='bar')
    plt.title('Predicted Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Additional analysis: Sentiment trends over time
def analyze_sentiment_trends(df):
    """Analyze how sentiments change over time"""
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    daily_sentiments = df.groupby(['date', 'sentiment_label']).size().unstack(fill_value=0)
    daily_sentiments.plot(kind='area', stacked=True, figsize=(12, 6))
    plt.title('Daily Sentiment Trends')
    plt.xlabel('Date')
    plt.ylabel('Number of Feedbacks')
    plt.legend(title='Sentiment')
    plt.show()

# Department-wise sentiment analysis
def department_sentiment_analysis(df):
    """Analyze sentiments by department"""
    dept_sentiment = pd.crosstab(df['department'], df['sentiment_label'], normalize='index') * 100
    dept_sentiment.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title('Sentiment Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Percentage')
    plt.legend(title='Sentiment')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
