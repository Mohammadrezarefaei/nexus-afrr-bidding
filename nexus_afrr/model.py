import xgboost as xgb
from sklearn.metrics import mean_absolute_error

def train_and_evaluate(X_train, y_train, X_test, y_test):
    """Trains the XGBoost model and evaluates MAE."""
    model = xgb.XGBRegressor(
        n_estimators=150,
        learning_rate=0.05,
        max_depth=5,
        objective='reg:squarederror',
        random_state=42
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    return model, predictions, mae
