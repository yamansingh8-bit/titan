# AUTOCRYPT V4 — Project Configuration
PROJECT_NAME = "AUTOCRYPT_V4"
PROJECT_VERSION = "1.0.0"
DOCTRINE = "CORRECTNESS > REPRODUCIBILITY > SAFETY > ROBUSTNESS > PERFORMANCE > SPEED"
TRADING_AUTHORITY = "RISK > STRATEGY > MODEL/LLM"
HARD_GOALS = {
    "OOS_Sharpe": ">= 1.50",
    "average_trades_per_day": ">= 4.00",
    "max_drawdown": "<= 20.00%",
}
SECONDARY_PREFERENCES = [
    "higher OOS Sharpe",
    "higher Sortino",
    "better expectancy",
    "better cost robustness",
    "better WFO stability",
    "better coin robustness",
    "better regime robustness",
]
COIN_UNIVERSE = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT"]
PRIMARY_TIMEFRAME = "15m"
