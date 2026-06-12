import pandas as pd

class MasterTradeEngine:
    def __init__(self):
        pass

    def get_indicators(self, df):
        # RSI
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        # MACD (Fast 12, Slow 26)
        ema_fast = df['close'].ewm(span=12).mean()
        ema_slow = df['close'].ewm(span=26).mean()
        macd = ema_fast - ema_slow
        
        return rsi.iloc[-1], macd.iloc[-1]

    def analyze(self, price_data):
        df = pd.DataFrame(price_data)
        rsi, macd = self.get_indicators(df)
        
        # نظام التصويت الذكي (الذكاء الاصطناعي المدمج)
        buy_score = 0
        sell_score = 0
        
        # تحليل المؤشرات
        if rsi < 30: buy_score += 1
        if rsi > 70: sell_score += 1
        if macd > 0: buy_score += 1
        if macd < 0: sell_score += 1
        
        # القرار النهائي: لا يرسل إشارة إلا إذا كانت النتيجة مؤكدة
        if buy_score >= 2:
            return "شراء"
        elif sell_score >= 2:
            return "بيع"
        else:
            return "انتظار"

# كائن المحرك الثابت
engine = MasterTradeEngine()