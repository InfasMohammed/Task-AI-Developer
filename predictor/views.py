from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

# Load the trained Prophet model
model = joblib.load(os.path.join('predictor', 'model', 'prophet_sales_model.pkl'))

def home(request):
    plot_path = None
    csv_available = False
    horizon = 12  # Default forecast horizon

    if request.method == 'POST':
        horizon = int(request.POST.get("horizon", 12))  # Get user input from form

        # Make future dataframe and forecast
        future = model.make_future_dataframe(periods=horizon, freq='W')
        forecast = model.predict(future)

        # Save plot
        fig = model.plot(forecast)

        # Draw a red line at the end of historical data
        # Use the length of the model history to determine cutoff
        cutoff_date = model.history['ds'].max()
        plt.axvline(x=cutoff_date, color='red', linestyle='--', label='Forecast Start')
        plt.legend()

        # Final touches and save
        plt.title("Sales Forecast")
        plt.tight_layout()
        forecast_image_path = os.path.join('predictor', 'static', 'forecast.png')
        plt.savefig(forecast_image_path)
        plt.close()
        plot_path = 'forecast.png'

        # Save forecast data as CSV
        csv_path = os.path.join('predictor', 'static', 'forecast.csv')
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(csv_path, index=False)
        csv_available = True


    return render(request, 'predictor/home.html', {
        'plot_path': plot_path,
        'csv_available': csv_available,
        'horizon': horizon if request.method == 'POST' else 12
    })
