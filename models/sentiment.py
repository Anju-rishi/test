from transformers import pipeline

# This is a large model, initialize it once
try:
    sentiment_analyzer = pipeline(
        "sentiment-analysis", 
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
except Exception as e:
    print(f"Could not load sentiment model, will use mock data. Error: {e}")
    sentiment_analyzer = None


def analyze_sentiment(texts: list) -> dict:
    if not sentiment_analyzer or not texts:
        return {'average_score': 0, 'positive_count': 0, 'negative_count': 0}

    results = sentiment_analyzer(texts)
    
    positive_count = 0
    negative_count = 0
    total_score = 0.0
    
    for result in results:
        if result['label'] == 'POSITIVE':
            positive_count += 1
            total_score += result['score']
        else:
            negative_count += 1
            total_score -= result['score']
            
    avg_score = total_score / len(results) if results else 0
    
    return {
        'average_score': avg_score,
        'positive_count': positive_count,
        'negative_count': negative_count,
    }