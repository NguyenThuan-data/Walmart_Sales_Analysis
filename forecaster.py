import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class SalesForecaster:
    def __init__(self, df):
        self.df = df.copy()
        self._preprocess()
        self.model = LinearRegression()
        self._train()

    def _preprocess(self):
        # Convert date and extract features
        self.df['date'] = pd.to_datetime(self.df['date'], dayfirst=True)
        self.df['day_of_week'] = self.df['date'].dt.dayofweek
        self.df['month'] = self.df['date'].dt.month
        self.df['year'] = self.df['date'].dt.year
        
        # Calculate daily total sales
        self.daily_sales = self.df.groupby('date').agg({
            'invoice_id': 'count',
            'unit_price': lambda x: x.str.replace('$', '').astype(float).sum() if x.dtype == 'object' else x.sum(),
            'quantity': 'sum',
            'profit_margin': 'mean'
        }).reset_index()
        
        # Calculate actual Total Sales
        if 'total_sales' not in self.daily_sales.columns:
            # Re-read unit_price cleaning if needed
            self.df['unit_price_clean'] = self.df['unit_price'].str.replace('$', '', regex=False).astype(float)
            self.df['total_amount'] = self.df['unit_price_clean'] * self.df['quantity']
            self.daily_sales = self.df.groupby('date')['total_amount'].sum().reset_index()
            
        self.daily_sales['day_of_week'] = self.daily_sales['date'].dt.dayofweek
        self.daily_sales['month'] = self.daily_sales['date'].dt.month

    def _train(self):
        X = self.daily_sales[['day_of_week', 'month']]
        y = self.daily_sales['total_amount']
        self.model.fit(X, y)

    def predict_next_week(self):
        last_date = self.daily_sales['date'].max()
        future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=7)
        future_df = pd.DataFrame({
            'date': future_dates,
            'day_of_week': future_dates.dayofweek,
            'month': future_dates.month
        })
        
        future_df['predicted_sales'] = self.model.predict(future_df[['day_of_week', 'month']])
        return future_df
