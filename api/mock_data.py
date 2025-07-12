import random
import time

def get_mock_analysis():
    """Generates a complete, realistic-looking mock response."""
    print("--- GENERATING MOCK DATA (Could not fetch live data) ---")
    time.sleep(1) # Simulate processing time
    
    risk_score = random.uniform(15, 85)
    volatility = random.uniform(1.5, 7.0)
    sentiment = random.uniform(-0.6, 0.6)
    
    if risk_score > 70:
        reco = "High Risk Detected. Consider hedging with options or reducing exposure."
        timing = "Avoid entry. Wait for volatility to subside post-upgrade."
    elif risk_score < 30:
        reco = "Low Risk. Upgrade appears stable. Consider accumulating on dips."
        timing = "Optimal entry window may be 24-48 hours before the upgrade."
    else:
        reco = "Moderate Risk. Maintain current position but set tight stop-losses."
        timing = "Monitor liquidity pools closely for any sudden TVL drops."
        
    return {
        "upgrade_risk_score": round(risk_score, 2),
        "expected_volatility_impact": round(volatility, 2),
        "liquidity_shift_prediction": f"${random.randint(-25, 15)}M TVL shift expected",
        "execution_timing": timing,
        "portfolio_rebalancing_recommendations": reco,
        "risk_mitigation_strategies": "Use stop-loss orders at 15% below entry.",
        "sentiment_score": round(sentiment, 2),
        "source": "Mock Data"
    }