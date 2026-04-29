"""
CONFIGURACIÓN DEL BOT CRYPTO SCANNER
=====================================
Ajusta estos parámetros según tus necesidades
"""

# ===== CRITERIOS DE SCREENING =====
SCREENING_CRITERIA = {
    "liquidity_min": 10000,          # USD - Liquidez mínima
    "market_cap_min": 50000,         # USD - Market cap mínimo
    "pair_age_min_hours": 0.5,       # Horas - Edad mínima
    "volume_24h_min": 10000,         # USD - Volumen mínimo 24h
    "top_holder_max_percent": 30,    # % - Top holder máximo
    "min_holders": 50,               # Cantidad mínima de holders
    "buy_sell_ratio_min": 1.2,       # Ratio compras/ventas mínimo
    "max_honeypot_risk": 30,         # % - Riesgo honeypot máximo
}

# ===== CHAINS A MONITOREAR =====
CHAINS = {
    "solana": {
        "name": "Solana",
        "dex": ["raydium", "orca", "pumpfun"],
        "enabled": True,
    },
    "ethereum": {
        "name": "Ethereum",
        "dex": ["uniswap_v2", "uniswap_v3"],
        "enabled": True,
    },
    "bsc": {
        "name": "BSC",
        "dex": ["pancakeswap"],
        "enabled": True,
    },
}

# ===== DISCORD WEBHOOK =====
# Dejaremos esto vacío - se genera automáticamente
DISCORD_WEBHOOK_URL = ""  # Se llenará después de crear el servidor

# ===== SCORING SYSTEM =====
SCORING_WEIGHTS = {
    "liquidity": 0.15,
    "market_cap": 0.10,
    "holders_distribution": 0.20,
    "buy_sell_ratio": 0.15,
    "age": 0.10,
    "volume_trend": 0.15,
    "smart_money": 0.15,
}

# ===== ALERTAS =====
ALERT_THRESHOLDS = {
    "score_min": 7.0,           # Score mínimo para alerta
    "urgency_high": 8.5,        # Score para alerta urgente
    "momentum_min": 1.5,        # Momentum mínimo (buy/sell ratio)
}

# ===== DATABASE =====
DB_PATH = "crypto_scanner.db"
KEEP_HISTORY_DAYS = 30

# ===== TIMING =====
SCAN_INTERVAL_SECONDS = 300  # Cada 5 minutos
ALERT_COOLDOWN_MINUTES = 15  # No alertar del mismo token en 15 min

# ===== LOGGING =====
LOG_LEVEL = "INFO"
LOG_FILE = "bot.log"

# ===== APIS =====
DEXSCREENER_API = "https://api.dexscreener.com/latest"
RUGCHECK_API = "https://api.rugcheck.xyz"
SOLSCAN_API = "https://api.solscan.io"
COINGECKO_API = "https://api.coingecko.com/api/v3"
GOPLUS_API = "https://api.gopluslabs.io"

# ===== RATE LIMITS =====
API_RATE_LIMIT = 60  # Requests por minuto
REQUEST_TIMEOUT = 10  # Segundos
