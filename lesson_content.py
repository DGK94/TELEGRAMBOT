import json
import os
from datetime import datetime

class TradingAcademy:
    def __init__(self):
        self.courses_file = "trading_academy/courses.json"
        self.progress_file = "trading_academy/user_progress.json"
        self.certifications_file = "trading_academy/certifications.json"
        self.lessons = {
            'crypto_basics': {
                'title': 'Cryptocurrency Fundamentals',
                'description': 'Learn the basics of cryptocurrency and blockchain technology',
                'lessons': [
                    {
                        'id': 1,
                        'title': 'What is Bitcoin?',
                        'content': 'Bitcoin is a decentralized digital currency...',
                        'duration': 15
                    },
                    {
                        'id': 2,
                        'title': 'Blockchain Technology',
                        'content': 'Blockchain is a distributed ledger technology...',
                        'duration': 20
                    }
                ]
            },
            'technical_analysis': {
                'title': 'Technical Analysis',
                'description': 'Learn to read charts and analyze price movements',
                'lessons': [
                    {
                        'id': 1,
                        'title': 'Support and Resistance',
                        'content': 'Support and resistance are key price levels...',
                        'duration': 25
                    }
                ]
            }
        }
        self.initialize_courses()

    def initialize_courses(self):
        """Initialize course structure if not exists"""
        if not os.path.exists(self.courses_file):
            default_courses = {
                "courses": {
                    "beginner": {
                        "technical_analysis_basics": {
                            "title": "Technical Analysis Fundamentals",
                            "description": "Master the basics of chart reading and technical indicators",
                            "duration": "4 weeks",
                            "lessons": [
                                {
                                    "title": "Introduction to Chart Patterns",
                                    "content": """🎯 **TECHNICAL ANALYSIS FUNDAMENTALS**

📊 **What is Technical Analysis?**
Technical analysis is the study of price movements and trading volume to predict future price directions. Unlike fundamental analysis, which looks at company financials, technical analysis focuses purely on price action.

📈 **Key Principles:**
1. Price reflects all available information
2. Prices move in trends
3. History tends to repeat itself

🔍 **Essential Chart Types:**
- **Line Charts**: Simple price progression
- **Candlestick Charts**: Show open, high, low, close
- **Bar Charts**: Similar to candlesticks but different format

🎯 **Basic Chart Patterns:**
- **Support & Resistance**: Key price levels
- **Trend Lines**: Direction indicators
- **Triangles**: Consolidation patterns
- **Head & Shoulders**: Reversal patterns

💡 **Practice Exercise:**
Identify support and resistance levels on your favorite cryptocurrency chart.""",
                                    "video_url": "https://youtube.com/watch?v=technical-analysis-intro",
                                    "quiz": [
                                        {
                                            "question": "What is the main focus of technical analysis?",
                                            "options": ["Company financials", "Price movements", "News events", "Social media"],
                                            "correct": 1,
                                            "explanation": "Technical analysis focuses on price movements and patterns, not fundamentals."
                                        }
                                    ]
                                },
                                {
                                    "title": "Understanding Candlestick Patterns",
                                    "content": """🕯️ **CANDLESTICK PATTERNS MASTERY**

📊 **Anatomy of a Candlestick:**
- **Body**: Difference between open and close
- **Wicks/Shadows**: Highest and lowest prices
- **Color**: Green (bullish) vs Red (bearish)

🎯 **Major Reversal Patterns:**
- **Doji**: Indecision in the market
- **Hammer**: Bullish reversal at support
- **Shooting Star**: Bearish reversal at resistance
- **Engulfing**: Strong reversal signal

📈 **Continuation Patterns:**
- **Spinning Tops**: Continued uncertainty
- **Marubozu**: Strong trend continuation
- **Inside Bars**: Consolidation before move

💪 **Multi-Candlestick Patterns:**
- **Three White Soldiers**: Strong bullish trend
- **Three Black Crows**: Strong bearish trend
- **Morning Star**: Bullish reversal
- **Evening Star**: Bearish reversal

🔥 **Pro Tips:**
1. Confirm patterns with volume
2. Consider overall trend direction
3. Use with other indicators
4. Practice pattern recognition daily""",
                                    "video_url": "https://youtube.com/watch?v=candlestick-patterns",
                                    "quiz": [
                                        {
                                            "question": "What does a Doji candlestick indicate?",
                                            "options": ["Strong buying", "Strong selling", "Market indecision", "Trend continuation"],
                                            "correct": 2,
                                            "explanation": "A Doji shows market indecision with open and close prices very close."
                                        }
                                    ]
                                }
                            ]
                        }
                    },
                    "intermediate": {
                        "advanced_technical_analysis": {
                            "title": "Advanced Technical Analysis",
                            "description": "Deep dive into complex indicators and strategies",
                            "duration": "6 weeks",
                            "lessons": []
                        }
                    },
                    "advanced": {
                        "algorithmic_trading": {
                            "title": "Algorithmic Trading Mastery",
                            "description": "Build automated trading systems",
                            "duration": "8 weeks",
                            "lessons": []
                        }
                    }
                },
                "specializations": {
                    "chia_farming": {
                        "title": "Chia Network Farming Mastery",
                        "description": "Complete guide to Chia farming and green blockchain",
                        "duration": "3 weeks",
                        "lessons": []
                    }
                }
            }

            with open(self.courses_file, 'w') as f:
                json.dump(default_courses, f, indent=2)

    def get_lesson_content(self, level, course_id, lesson_index):
        """Get specific lesson content"""
        lessons = {
            "technical_analysis_basics": {
                0: {
                    "title": "Introduction to Charts and Timeframes",
                    "content": """
📊 **CHART TYPES & TIMEFRAMES**

**Chart Types:**
- Line Charts - Simple price movement
- Candlestick Charts - OHLC data (Open, High, Low, Close)
- Bar Charts - Traditional OHLC representation
- Heikin-Ashi - Smoothed candlesticks

**Timeframe Selection:**
- Scalping: 1m, 5m charts
- Day Trading: 15m, 1h charts
- Swing Trading: 4h, 1D charts
- Position Trading: 1D, 1W charts

**Reading Candlesticks:**
- Green/White: Close > Open (Bullish)
- Red/Black: Close < Open (Bearish)
- Wicks: Show high/low extremes
- Body: Difference between open/close

**Practice Exercise:**
Identify 10 different candlestick patterns on BTC/USDT 1H chart.
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/charts_basics",
                    "quiz": [
                        {
                            "question": "What does a long upper wick indicate?",
                            "options": ["Buying pressure", "Selling pressure", "Consolidation", "Breakout"],
                            "correct": 1,
                            "explanation": "A long upper wick shows that price moved higher but was rejected, indicating selling pressure at those levels."
                        }
                    ]
                },
                1: {
                    "title": "Support and Resistance Identification",
                    "content": """
🎯 **SUPPORT & RESISTANCE MASTERY**

**Support Levels:**
- Price floor where buying interest emerges
- Previous lows, moving averages, trend lines
- Psychological levels (round numbers)
- Volume-based support zones

**Resistance Levels:**
- Price ceiling where selling pressure increases
- Previous highs, moving averages
- Fibonacci retracement levels
- Supply zones from institutional orders

**Identification Techniques:**
1. Horizontal levels from price history
2. Diagonal trend lines
3. Dynamic levels (moving averages)
4. Volume profile POC (Point of Control)

**Trading Strategies:**
- Buy at support, sell at resistance
- Wait for breakouts with volume confirmation
- Use false breakouts as reversal signals
- Trail stops using support/resistance

**Real Example - BTC Analysis:**
Current Support: $95,500 (previous low)
Key Resistance: $100,000 (psychological level)
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/support_resistance",
                    "quiz": [
                        {
                            "question": "What makes a support level stronger?",
                            "options": ["High volume", "Multiple touches", "Round numbers", "All of the above"],
                            "correct": 3
                        }
                    ]
                }
            },
            "risk_management": {
                0: {
                    "title": "Position Sizing Strategies",
                    "content": """
💰 **POSITION SIZING MASTERY**

**Fixed Dollar Amount:**
- Risk same $ amount per trade
- Simple but ignores account growth
- Example: Always risk $100 per trade

**Percentage Risk Model:**
- Risk fixed % of account per trade
- Scales with account size
- Recommended: 1-3% max per trade

**Kelly Criterion:**
- Optimal position size based on win rate
- Formula: f = (bp - q) / b
- Where: b=odds, p=win probability, q=loss probability

**Position Size Calculation:**
1. Determine risk per trade (2% of $10,000 = $200)
2. Find entry and stop loss prices
3. Calculate position size: Risk ÷ (Entry - Stop Loss)

**Example Trade:**
- Account: $10,000
- Risk: 2% = $200
- BTC Entry: $97,000
- Stop Loss: $95,000
- Position Size: $200 ÷ $2,000 = 0.1 BTC

**Advanced Techniques:**
- Volatility-adjusted sizing
- Correlation-based position limits
- Dynamic position scaling
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/position_sizing",
                    "quiz": [
                        {
                            "question": "If you risk 2% on a $5,000 account with entry at $50,000 and stop at $48,000, what's your position size?",
                            "options": ["0.05 BTC", "0.1 BTC", "0.025 BTC", "0.2 BTC"],
                            "correct": 0
                        }
                    ]
                }
            },
            "advanced_technical_analysis": {
                0: {
                    "title": "Fibonacci Retracements & Extensions",
                    "content": """
🌟 **FIBONACCI TRADING MASTERY**

**Key Fibonacci Ratios:**
- 23.6% - Minor retracement
- 38.2% - Shallow correction
- 50.0% - Psychological level
- 61.8% - Golden ratio (strongest)
- 78.6% - Deep retracement

**Extension Levels:**
- 127.2% - First target
- 161.8% - Golden extension
- 261.8% - Major projection
- 423.6% - Extreme target

**Drawing Fibonacci:**
1. Identify significant swing high/low
2. Draw from swing low to swing high (uptrend)
3. Draw from swing high to swing low (downtrend)
4. Look for confluence with other indicators

**Trading Strategies:**
- Buy at 61.8% retracement in uptrend
- Set targets at extension levels
- Use multiple timeframe analysis
- Combine with volume and momentum

**BTC Example:**
Recent swing: $85,000 to $99,000
61.8% retracement: $90,346
Extension targets: $105,802 (127.2%)

**Advanced Techniques:**
- Fibonacci fans and arcs
- Time-based Fibonacci
- Confluence zones
- Multiple Fibonacci analysis
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/fibonacci",
                    "quiz": [
                        {
                            "question": "What is the golden ratio in Fibonacci retracements?",
                            "options": ["38.2%", "50%", "61.8%", "78.6%"],
                            "correct": 2
                        }
                    ]
                }
            },
            "algorithmic_trading": {
                0: {
                    "title": "Python for Trading",
                    "content": """
🐍 **PYTHON TRADING FOUNDATIONS**

**Essential Libraries:**
- pandas - Data manipulation
- numpy - Numerical computations
- matplotlib - Plotting charts
- ccxt - Exchange connectivity
- talib - Technical indicators

**Basic Trading Bot Structure:**
```python
import ccxt
import pandas as pd
import numpy as np

class TradingBot:
    def __init__(self, exchange, api_key, secret):
        self.exchange = exchange
        self.setup_exchange(api_key, secret)

    def get_ohlcv(self, symbol, timeframe, limit=100):
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        return df

    def calculate_rsi(self, closes, period=14):
        deltas = np.diff(closes)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)

        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
```

**Data Management:**
- Real-time price feeds
- Historical data storage
- Data cleaning and preprocessing
- Multiple timeframe analysis

**Strategy Development:**
- Backtesting framework
- Risk management rules
- Position sizing algorithms
- Performance metrics

**Advanced Features:**
- Machine learning integration
- Sentiment analysis
- Portfolio optimization
- Multi-asset strategies
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/python_trading",
                    "quiz": [
                        {
                            "question": "Which library is used for exchange connectivity?",
                            "options": ["pandas", "numpy", "ccxt", "matplotlib"],
                            "correct": 2
                        }
                    ]
                },
                1: {
                    "title": "Strategy Backtesting",
                    "content": """
📊 **BACKTESTING MASTERY**

**Backtesting Framework:**
```python
class Backtester:
    def __init__(self, strategy, data, initial_capital=10000):
        self.strategy = strategy
        self.data = data
        self.capital = initial_capital
        self.positions = []
        self.trades = []

    def run_backtest(self):
        for i in range(len(self.data)):
            signal = self.strategy.generate_signal(self.data.iloc[:i+1])
            if signal:
                self.execute_trade(signal, self.data.iloc[i])

        return self.calculate_performance()

    def calculate_performance(self):
        total_return = (self.capital - 10000) / 10000 * 100
        sharpe_ratio = self.calculate_sharpe()
        max_drawdown = self.calculate_max_drawdown()

        return {
            'total_return': total_return,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'total_trades': len(self.trades)
        }
```

**Key Metrics:**
- Total Return
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- Profit Factor
- Average Trade Duration

**Avoiding Pitfalls:**
- Look-ahead bias
- Survivorship bias
- Overfitting
- Transaction costs
- Slippage consideration

**Optimization:**
- Parameter tuning
- Walk-forward analysis
- Out-of-sample testing
- Cross-validation
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/backtesting",
                    "quiz": [
                        {
                            "question": "What does Sharpe ratio measure?",
                            "options": ["Total return", "Risk-adjusted return", "Maximum loss", "Win rate"],
                            "correct": 1
                        }
                    ]
                }
            },
            "cryptocurrency_fundamentals": {
                0: {
                    "title": "Bitcoin Deep Dive",
                    "content": """
₿ **BITCOIN COMPREHENSIVE ANALYSIS**

**Technical Foundation:**
- Proof of Work consensus
- SHA-256 hashing algorithm
- 21 million supply cap
- 10-minute block time
- Difficulty adjustment every 2016 blocks

**Network Metrics:**
- Hash Rate: 520+ EH/s
- Mining Difficulty: Dynamic adjustment
- Active Addresses: 950,000 daily
- Transaction Volume: $15B+ daily
- Lightning Network: 5,000+ BTC capacity

**Investment Thesis:**
- Digital gold narrative
- Store of value proposition
- Inflation hedge characteristics
- Institutional adoption
- Regulatory clarity improving

**On-Chain Analysis:**
- MVRV Ratio (Market Value to Realized Value)
- Stock-to-Flow Model
- Whale wallet movements
- Exchange flows
- Long-term holder behavior

**Trading Considerations:**
- High volatility periods
- Correlation with traditional markets
- Halving cycle impacts
- Regulatory news sensitivity
- Institutional buying patterns

**Future Developments:**
- Lightning Network expansion
- Taproot implementation benefits
- Central Bank Digital Currency interactions
- ESG considerations
- Quantum computing resistance
                    """,
                    "video_url": "https://academy.signalxpress.pro/video/bitcoin_deep_dive",
                    "quiz": [
                        {
                            "question": "What is Bitcoin's maximum supply?",
                            "options": ["18 million", "19 million", "21 million", "25 million"],
                            "correct": 2
                        }
                    ]
                }
            }
        }

    def get_lesson(self, course_name, lesson_id):
        """Get specific lesson content"""
        course = self.lessons.get(course_name, {})
        lessons = course.get('lessons', [])
        for lesson in lessons:
            if lesson['id'] == lesson_id:
                return lesson

        return None

    def get_course_list(self):
        """Get list of available courses"""
        return {
            'beginner': [
                'crypto_basics',
                'technical_analysis_101',
                'risk_management'
            ],
            'intermediate': [
                'advanced_charting',
                'market_psychology',
                'portfolio_management'
            ],
            'advanced': [
                'institutional_trading',
                'algorithmic_trading',
                'cryptocurrency_fundamentals'
            ]
        }

    def get_quiz_results(self, course_name, lesson_id, answers):
        """Evaluate quiz answers"""
        lesson = self.get_lesson(course_name, lesson_id)
        if not lesson or not lesson['quiz']:
            return None

        correct_answers = 0
        total_questions = len(lesson['quiz'])

        for i, question in enumerate(lesson['quiz']):
            if i < len(answers) and answers[i] == question['correct']:
                correct_answers += 1

        score = (correct_answers / total_questions) * 100

        return {
            'score': score,
            'correct': correct_answers,
            'total': total_questions,
            'passed': score >= 70
        }

    def save_user_progress(self, user_id, course_id, lesson_index, quiz_score=None):
        """Save user learning progress"""
        try:
            if os.path.exists(self.progress_file):
                with open(self.progress_file, 'r') as f:
                    progress = json.load(f)
            else:
                progress = {}

            if str(user_id) not in progress:
                progress[str(user_id)] = {}

            if course_id not in progress[str(user_id)]:
                progress[str(user_id)][course_id] = {
                    "completed_lessons": [],
                    "quiz_scores": {},
                    "start_date": datetime.utcnow().isoformat(),
                    "last_accessed": datetime.utcnow().isoformat()
                }

            progress[str(user_id)][course_id]["last_accessed"] = datetime.utcnow().isoformat()

            if lesson_index not in progress[str(user_id)][course_id]["completed_lessons"]:
                progress[str(user_id)][course_id]["completed_lessons"].append(lesson_index)

            if quiz_score is not None:
                progress[str(user_id)][course_id]["quiz_scores"][str(lesson_index)] = quiz_score

            with open(self.progress_file, 'w') as f:
                json.dump(progress, f, indent=2)

        except Exception as e:
            print(f"Error saving progress: {e}")

    def get_user_progress(self, user_id):
        """Get user's learning progress"""
        try:
            if os.path.exists(self.progress_file):
                with open(self.progress_file, 'r') as f:
                    progress = json.load(f)
                return progress.get(str(user_id), {})
        except:
            pass
        return {}

    def issue_certificate(self, user_id, course_id):
        """Issue course completion certificate"""
        try:
            if os.path.exists(self.certifications_file):
                with open(self.certifications_file, 'r') as f:
                    certs = json.load(f)
            else:
                certs = {}

            if str(user_id) not in certs:
                certs[str(user_id)] = []

            certificate = {
                "course_id": course_id,
                "completion_date": datetime.utcnow().isoformat(),
                "certificate_id": f"SXP-{user_id}-{course_id}-{int(datetime.utcnow().timestamp())}",
                "verification_url": f"https://academy.signalxpress.pro/verify/{certificate['certificate_id']}"
            }

            certs[str(user_id)].append(certificate)

            with open(self.certifications_file, 'w') as f:
                json.dump(certs, f, indent=2)

            return certificate

        except Exception as e:
            print(f"Certificate error: {e}")
            return None

    def get_course(self, course_name):
        """Get entire course"""
        return self.lessons.get(course_name, None)

# Create global academy instance
academy = TradingAcademy()