from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load the trained Prophet model
model = joblib.load(os.path.join('predictor', 'model', 'prophet_sales_model.pkl'))

def home(request):
    plot_path = None
    csv_available = False
    horizon = 12  # Default value
    mae = None
    rmse = None

    if request.method == 'POST':
        horizon = int(request.POST.get("horizon", 12))  # Get from user form

        # Generate forecast
        future = model.make_future_dataframe(periods=horizon, freq='W')
        forecast = model.predict(future)

        # Load actual historical data
        df = pd.read_csv(os.path.join('predictor', 'data', 'filtered_sales.csv'))
        df['ds'] = pd.to_datetime(df['ds'])

        # Merge with predicted to calculate metrics
        merged = pd.merge(df[['ds', 'y']], forecast[['ds', 'yhat']], on='ds', how='inner')

        if not merged.empty:
            mae = mean_absolute_error(merged['y'], merged['yhat'])
            rmse = mean_squared_error(merged['y'], merged['yhat'], squared=False)

        # Plot forecast
        fig = model.plot(forecast)

        # Add red vertical line at forecast start
        cutoff_date = model.history['ds'].max()
        plt.axvline(x=cutoff_date, color='red', linestyle='--', label='Forecast Start')
        plt.legend()
        plt.title("Sales Forecast")
        plt.tight_layout()

        # Save plot
        forecast_image_path = os.path.join('predictor', 'static', 'forecast.png')
        plt.savefig(forecast_image_path)
        plt.close()
        plot_path = 'forecast.png'

        # Save forecast as CSV
        csv_path = os.path.join('predictor', 'static', 'forecast.csv')
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(csv_path, index=False)
        csv_available = True

    return render(request, 'predictor/home.html', {
        'plot_path': plot_path,
        'csv_available': csv_available,
        'horizon': horizon,
        'mae': round(mae, 2) if mae is not None else None,
        'rmse': round(rmse, 2) if rmse is not None else None,
    })
