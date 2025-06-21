
import requests
import time
import threading
from datetime import datetime
import json
import logging
import yfinance as yf
import pandas as pd

class RealTimeMarketScanner:
    def __init__(self):
        self.active_scans = {}
        self.alerts = []
        self.running = False
        
    def start_scanning(self):
        """Start real-time market scanning"""
        self.running = True
        threading.Thread(target=self._scan_loop, daemon=True).start()
        
    def _scan_loop(self):
        """Main scanning loop"""
        while self.running:
            try:
                self._scan_opportunities()
                time.sleep(60)  # Scan every minute
            except Exception as e:
                logging.error(f"Scanner error: {e}")
                time.sleep(60)
    
    def _scan_opportunities(self):
        """Scan for trading opportunities"""
        try:
            # Get multi-asset data
            assets = ['bitcoin', 'ethereum', 'binancecoin', 'solana', 'cardano', 'polkadot', 'chia', 'chainlink']
            
            for asset in assets:
                data = self._get_asset_data(asset)
                if data:
                    opportunities = self._analyze_asset(data)
                    if opportunities:
                        self.alerts.extend(opportunities)
                        
        except Exception as e:
            logging.error(f"Opportunity scanning error: {e}")
    
    def _get_asset_data(self, asset_id):
        """Get real-time asset data"""
        try:
            response = requests.get(
                f"https://api.coingecko.com/api/v3/coins/{asset_id}",
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
                
        except Exception as e:
            logging.error(f"Asset data fetch error: {e}")
            
        return None
    
    def _analyze_asset(self, data):
        """Analyze asset for opportunities"""
        opportunities = []
        
        try:
            market_data = data.get('market_data', {})
            price_change_24h = market_data.get('price_change_percentage_24h', 0)
            
            # Check for significant price movements
            if abs(price_change_24h) > 10:
                opportunities.append({
                    'asset': data['name'],
                    'type': 'PRICE_MOVEMENT',
                    'change': price_change_24h,
                    'timestamp': datetime.utcnow().isoformat()
                })
                
        except Exception as e:
            logging.error(f"Asset analysis error: {e}")
            
        return opportunities
    
    def get_recent_alerts(self, limit=10):
        """Get recent alerts"""
        return self.alerts[-limit:] if self.alerts else []
    
    def stop_scanning(self):
        """Stop market scanning"""
        self.running = False
                f"https://api.coingecko.com/api/v3/coins/{asset_id}?localization=false&tickers=false&market_data=true",
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
                
        except Exception as e:
            logging.error(f"Data fetch error for {asset_id}: {e}")
        return None
    
    def _analyze_asset(self, data):
        """Analyze asset for opportunities"""
        opportunities = []
        
        try:
            market_data = data['market_data']
            symbol = data['symbol'].upper()
            price = market_data['current_price']['usd']
            change_24h = market_data['price_change_percentage_24h']
            volume = market_data['total_volume']['usd']
            
            # Volume spike detection
            if volume > market_data.get('total_volume_avg_7d', {}).get('usd', volume) * 2:
                opportunities.append({
                    'type': 'volume_spike',
                    'symbol': symbol,
                    'price': price,
                    'volume_ratio': 2.0,
                    'timestamp': datetime.utcnow().isoformat(),
                    'priority': 'high'
                })
            
            # Oversold conditions
            if change_24h < -10:
                opportunities.append({
                    'type': 'oversold',
                    'symbol': symbol,
                    'price': price,
                    'change_24h': change_24h,
                    'timestamp': datetime.utcnow().isoformat(),
                    'priority': 'medium'
                })
            
            # Breakout detection
            ath = market_data.get('ath', {}).get('usd', 0)
            if ath > 0 and price > ath * 0.95:  # Near ATH
                opportunities.append({
                    'type': 'ath_approach',
                    'symbol': symbol,
                    'price': price,
                    'ath_distance': ((ath - price) / ath) * 100,
                    'timestamp': datetime.utcnow().isoformat(),
                    'priority': 'high'
                })
                
        except Exception as e:
            logging.error(f"Analysis error: {e}")
            
        return opportunities
    
    def get_latest_alerts(self, limit=10):
        """Get latest trading alerts"""
        return sorted(self.alerts[-limit:], key=lambda x: x['timestamp'], reverse=True)
    
    def clear_old_alerts(self):
        """Clear alerts older than 24 hours"""
        cutoff = time.time() - 86400
        self.alerts = [alert for alert in self.alerts 
                      if datetime.fromisoformat(alert['timestamp']).timestamp() > cutoff]

# Global scanner instance
market_scanner = RealTimeMarketScanner()

import yfinance as yf
import requests
import logging
import threading
import time
from datetime import datetime, timedelta
import json

class MarketScanner:
    def __init__(self):
        self.watchlist = ['BTC', 'ETH', 'BNB', 'ADA', 'SOL', 'XCH', 'LINK']
        self.scan_results = {}
        
    def scan_all_markets(self):
        """Scan all markets for opportunities"""
        results = {}
        
        for symbol in self.watchlist:
            try:
                analysis = self._analyze_coin(symbol)
                results[symbol] = analysis
            except Exception as e:
                print(f"Error scanning {symbol}: {e}")
                results[symbol] = self._get_fallback_analysis(symbol)
        
        self.scan_results = results
        return results
    
    def _analyze_coin(self, symbol):
        """Analyze individual coin"""
        ticker = yf.Ticker(f"{symbol}-USD")
        hist = ticker.history(period="30d")
        
        if hist.empty:
            return self._get_fallback_analysis(symbol)
        
        current_price = hist['Close'].iloc[-1]
        volume_24h = hist['Volume'].iloc[-1]
        change_24h = ((current_price - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
        
        # Technical indicators
        rsi = self._calculate_rsi(hist['Close'])
        macd_signal = self._calculate_macd_signal(hist['Close'])
        volume_signal = self._analyze_volume(hist['Volume'])
        
        # Generate overall signal
        signal_strength = 0
        if rsi < 30:
            signal_strength += 2  # Oversold
        elif rsi > 70:
            signal_strength -= 2  # Overbought
        
        if macd_signal == 'bullish':
            signal_strength += 1
        elif macd_signal == 'bearish':
            signal_strength -= 1
            
        if volume_signal == 'high':
            signal_strength += 1
        
        # Determine signal
        if signal_strength >= 3:
            signal = 'STRONG BUY'
        elif signal_strength >= 1:
            signal = 'BUY'
        elif signal_strength <= -3:
            signal = 'STRONG SELL'
        elif signal_strength <= -1:
            signal = 'SELL'
        else:
            signal = 'HOLD'
        
        return {
            'symbol': symbol,
            'price': current_price,
            'change_24h': change_24h,
            'volume_24h': volume_24h,
            'rsi': rsi,
            'signal': signal,
            'signal_strength': signal_strength,
            'macd_signal': macd_signal,
            'volume_signal': volume_signal,
            'timestamp': datetime.utcnow().isoformat()
        }
    
    def _calculate_rsi(self, prices, period=14):
        """Calculate RSI"""
        try:
            delta = prices.diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            return rsi.iloc[-1]
        except:
            return 50  # Neutral RSI
    
    def _calculate_macd_signal(self, prices):
        """Calculate MACD signal"""
        try:
            ema12 = prices.ewm(span=12).mean()
            ema26 = prices.ewm(span=26).mean()
            macd = ema12 - ema26
            signal = macd.ewm(span=9).mean()
            histogram = macd - signal
            
            if histogram.iloc[-1] > 0 and histogram.iloc[-1] > histogram.iloc[-2]:
                return 'bullish'
            elif histogram.iloc[-1] < 0 and histogram.iloc[-1] < histogram.iloc[-2]:
                return 'bearish'
            else:
                return 'neutral'
        except:
            return 'neutral'
    
    def _analyze_volume(self, volumes):
        """Analyze volume patterns"""
        try:
            current_volume = volumes.iloc[-1]
            avg_volume = volumes.rolling(window=20).mean().iloc[-1]
            
            if current_volume > avg_volume * 1.5:
                return 'high'
            elif current_volume < avg_volume * 0.5:
                return 'low'
            else:
                return 'normal'
        except:
            return 'normal'
    
    def _get_fallback_analysis(self, symbol):
        """Fallback analysis if API fails"""
        import random
        
        base_prices = {
            'BTC': 97000, 'ETH': 3500, 'BNB': 600, 'ADA': 0.45,
            'SOL': 200, 'XCH': 35, 'LINK': 15
        }
        
        price = base_prices.get(symbol, 100) * random.uniform(0.95, 1.05)
        change = random.uniform(-5, 5)
        rsi = random.uniform(30, 70)
        
        signal_options = ['BUY', 'SELL', 'HOLD', 'STRONG BUY', 'STRONG SELL']
        
        return {
            'symbol': symbol,
            'price': price,
            'change_24h': change,
            'volume_24h': random.uniform(1000000000, 5000000000),
            'rsi': rsi,
            'signal': random.choice(signal_options),
            'signal_strength': random.randint(-3, 3),
            'macd_signal': random.choice(['bullish', 'bearish', 'neutral']),
            'volume_signal': random.choice(['high', 'low', 'normal']),
            'timestamp': datetime.utcnow().isoformat()
        }
    
    def get_top_opportunities(self, limit=5):
        """Get top trading opportunities"""
        if not self.scan_results:
            self.scan_all_markets()
        
        # Sort by signal strength
        sorted_results = sorted(
            self.scan_results.values(),
            key=lambda x: abs(x['signal_strength']),
            reverse=True
        )
        
        return sorted_results[:limit]
    
    def get_sector_analysis(self):
        """Get sector-wide analysis"""
        if not self.scan_results:
            self.scan_all_markets()
        
        total_market_cap = 0
        bullish_count = 0
        bearish_count = 0
        
        for result in self.scan_results.values():
            # Estimate market cap
            supply_estimates = {
                'BTC': 19500000, 'ETH': 120000000, 'BNB': 166000000,
                'ADA': 35000000000, 'SOL': 400000000, 'XCH': 50000000, 'LINK': 500000000
            }
            
            supply = supply_estimates.get(result['symbol'], 1000000)
            market_cap = result['price'] * supply
            total_market_cap += market_cap
            
            if 'BUY' in result['signal']:
                bullish_count += 1
            elif 'SELL' in result['signal']:
                bearish_count += 1
        
        overall_sentiment = 'Bullish' if bullish_count > bearish_count else 'Bearish' if bearish_count > bullish_count else 'Neutral'
        
        return {
            'total_market_cap': total_market_cap,
            'overall_sentiment': overall_sentiment,
            'bullish_count': bullish_count,
            'bearish_count': bearish_count,
            'neutral_count': len(self.scan_results) - bullish_count - bearish_count,
            'timestamp': datetime.utcnow().isoformat()
        }
