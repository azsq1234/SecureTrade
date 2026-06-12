import pandas as pd

class TradingEngine:
    def __init__(self, data):
        self.data = data
        self.data.columns = [col.lower() for col in self.data.columns]
        
    def calculate_indicators(self):
        if 'close' not in self.data.columns:
            return None
            
        self.data['ema_10'] = self.data['close'].ewm(span=10, adjust=False).mean()
        self.data['ema_20'] = self.data['close'].ewm(span=20, adjust=False).mean()
        
        delta = self.data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['rsi'] = 100 - (100 / (1 + rs))
        return self.data

    def check_signal(self):
        last_row = self.data.iloc[-1]
        if pd.isna(last_row['ema_10']) or pd.isna(last_row['rsi']):
            return None
        
        if last_row['ema_10'] > last_row['ema_20'] and last_row['rsi'] < 30:
            return "BUY 🟢"
        elif last_row['ema_10'] < last_row['ema_20'] and last_row['rsi'] > 70:
            return "SELL 🔴"
        return None