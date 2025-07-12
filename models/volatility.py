import pandas as pd
import numpy as np
from arch import arch_model

def forecast_volatility(prices: pd.Series):
    returns = 100 * prices.pct_change().dropna()
    if len(returns) < 10: # Need enough data to model
        return 0.0, None

    model = arch_model(returns, vol='Garch', p=1, q=1, rescale=False)
    results = model.fit(disp='off', show_warning=False)
    
    forecast = results.forecast(horizon=1)
    # The variance is annualized, so we get the daily vol
    predicted_volatility = np.sqrt(forecast.variance.iloc[-1, 0])
    
    return predicted_volatility, results