import pandas as pd
import numpy as np

def simulate_bidding_revenue(y_true, y_pred, battery_mw=2.5, bid_markdown=0.92):
    """Simulates market clearance and calculates revenue."""
    results = pd.DataFrame({
        'Actual_aFRR_Price': y_true.values,
        'Predicted_aFRR_Price': y_pred
    }, index=y_true.index)
    
    results['Our_Bid'] = results['Predicted_aFRR_Price'] * bid_markdown
    results['Bid_Accepted'] = results['Our_Bid'] <= results['Actual_aFRR_Price']
    results['Revenue_EUR'] = np.where(
        results['Bid_Accepted'], 
        results['Actual_aFRR_Price'] * battery_mw, 
        0.0
    )
    results['Optimal_Revenue'] = results['Actual_aFRR_Price'] * battery_mw
    return results
