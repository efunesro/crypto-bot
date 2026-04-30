#!/usr/bin/env python3
"""
Cryptocurrency Scanner Bot with Flask Dashboard
Scans multiple blockchain networks for tokens and displays alerts via dashboard
"""

import os
import json
import threading
import time
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# DATABASE SETUP
# ============================================================================

DB_PATH = 'scanner.db'

def init_database():
    """Initialize SQLite database for storing scan results"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Create tables if they don't exist
        c.execute('''CREATE TABLE IF NOT EXISTS tokens
                    (id INTEGER PRIMARY KEY,
                     address TEXT UNIQUE,
                     name TEXT,
                     symbol TEXT,
                     chain TEXT,
                     risk_score REAL,
                     timestamp DATETIME)''')

        c.execute('''CREATE TABLE IF NOT EXISTS alerts
                    (id INTEGER PRIMARY KEY,
                     token_address TEXT,
                     token_name TEXT,
                     risk_score REAL,
                     reason TEXT,
                     timestamp DATETIME)''')

        c.execute('''CREATE TABLE IF NOT EXISTS logs
                    (id INTEGER PRIMARY KEY,
                     message TEXT,
                     level TEXT,
                     timestamp DATETIME)''')

        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization error: {e}")

def log_activity(message, level="INFO"):
    """Log activity to database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO logs (message, level, timestamp) VALUES (?, ?, ?)",
                 (message, level, datetime.now()))
        conn.commit()
        conn.close()
    except Exception as e:
        logger.error(f"Error logging activity: {e}")

def add_alert(token_address, token_name, risk_score, reason):
    """Add high-risk token alert to database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO alerts (token_address, token_name, risk_score, reason, timestamp) VALUES (?, ?, ?, ?, ?)",
                 (token_address, token_name, risk_score, reason, datetime.now()))
        conn.commit()
        conn.close()
        logger.warning(f"ALERT: {token_name} ({token_address}) - Risk Score: {risk_score}")
    except Exception as e:
        logger.error(f"Error adding alert: {e}")

def get_stats():
    """Get statistics from database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("SELECT COUNT(*) FROM tokens")
        unique_tokens = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM alerts WHERE risk_score > 7.0")
        alerts_sent = c.fetchone()[0]

        c.execute("SELECT COUNT(*) FROM logs")
        total_scans = c.fetchone()[0]

        conn.close()

        return {
            'total_scans': total_scans,
            'unique_tokens': unique_tokens,
            'alerts_sent': alerts_sent,
            'status': 'running',
            'chains': ['Solana', 'Ethereum', 'BSC']
        }
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        return {'error': str(e)}

def get_alerts():
    """Get all high-risk alerts"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("""SELECT token_name, token_address, risk_score, reason, timestamp
                    FROM alerts WHERE risk_score > 7.0
                    ORDER BY timestamp DESC LIMIT 100""")
        alerts = c.fetchall()
        conn.close()

        result = []
        for alert in alerts:
            result.append({
                'name': alert[0],
                'address': alert[1],
                'risk_score': alert[2],
                'reason': alert[3],
                'timestamp': alert[4]
            })
        return result
    except Exception as e:
        logger.error(f"Error getting alerts: {e}")
        return []

def get_logs():
    """Get activity logs"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("SELECT message, level, timestamp FROM logs ORDER BY timestamp DESC LIMIT 100")
        logs = c.fetchall()
        conn.close()

        result = []
        for log in logs:
            result.append({
                'message': log[0],
                'level': log[1],
                'timestamp': log[2]
            })
        return result
    except Exception as e:
        logger.error(f"Error getting logs: {e}")
        return []

# ============================================================================
# FLASK APP SETUP - ROUTES DEFINED BEFORE THREAD STARTS
# ============================================================================

api_app = Flask(__name__)
CORS(api_app)

@api_app.route('/')
def dashboard():
    """Serve the dashboard HTML"""
    dashboard_path = os.path.join(os.path.dirname(__file__), 'dashboard.html')
    try:
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return jsonify({'error': 'Dashboard not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@api_app.route('/api/stats')
def stats():
    """Get bot statistics"""
    return jsonify(get_stats())

@api_app.route('/api/alerts')
def alerts():
    """Get high-risk token alerts"""
    return jsonify({'alerts': get_alerts()})

@api_app.route('/api/log')
def logs():
    """Get activity logs"""
    return jsonify({'logs': get_logs()})

@api_app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@api_app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

# ============================================================================
# FLASK SERVER THREAD
# ============================================================================

def run_api_server():
    """Run Flask API server in background thread"""
    try:
        port = int(os.environ.get("PORT", os.environ.get("API_PORT", 5000)))
        host = '0.0.0.0'
        logger.info(f"Starting Flask API server on {host}:{port}")
        api_app.run(host=host, port=port, debug=False, use_reloader=False, threaded=True)
    except Exception as e:
        logger.error(f"Flask server error: {e}")

def start_api_server():
    """Start Flask in a separate daemon thread"""
    try:
        api_thread = threading.Thread(target=run_api_server, daemon=False, name="FlaskAPIServer")
        api_thread.start()
        logger.info("Flask API server thread started")
        return api_thread
    except Exception as e:
        logger.error(f"Error starting Flask thread: {e}")
        return None

# ============================================================================
# BOT SIMULATION LOGIC
# ============================================================================

def simulate_token_scan(chain_name):
    """Simulate scanning a blockchain for tokens"""
    chains = {
        'Solana': ['TokenA_Sol', 'TokenB_Sol', 'HighRiskToken_Sol'],
        'Ethereum': ['TokenA_Eth', 'TokenB_Eth', 'FakeToken_Eth'],
        'BSC': ['TokenA_BSC', 'HighRiskToken_BSC', 'TokenB_BSC']
    }

    tokens = chains.get(chain_name, [])

    for token in tokens:
        # Simulate risk scoring
        risk_score = 3.5
        if 'HighRisk' in token or 'Fake' in token:
            risk_score = 8.5

        log_activity(f"📍 Scanning {chain_name}... - Found: {token} (Risk: {risk_score})")

        if risk_score > 7.0:
            add_alert(
                token_address=f"0x{token.lower()}",
                token_name=token,
                risk_score=risk_score,
                reason="Suspicious contract behavior detected"
            )

        time.sleep(0.5)

def bot_scan_loop():
    """Main bot scanning loop"""
    chains = ['Solana', 'Ethereum', 'BSC']
    scan_count = 0

    try:
        while True:
            scan_count += 1
            log_activity(f"SCAN #{scan_count} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            log_activity("=" * 50)

            for chain in chains:
                log_activity(f"🔍 Scanning {chain}...")
                simulate_token_scan(chain)
                log_activity("=" * 50)

            log_activity(f"✅ Scan complete. Found: 0 | Alerts: 0")
            log_activity("=" * 50)

            # Scan every 5 minutes
            time.sleep(300)

    except KeyboardInterrupt:
        logger.info("Bot shutdown requested")
    except Exception as e:
        logger.error(f"Bot loop error: {e}")
        log_activity(f"ERROR: {e}", level="ERROR")

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """Main entry point"""
    logger.info("Initializing Cryptocurrency Scanner Bot")

    # Initialize database
    init_database()
    log_activity("Bot started", level="INFO")

    # Start Flask API server FIRST (in background thread)
    logger.info("Starting Flask API server")
    api_thread = start_api_server()

    # Give Flask a moment to start
    time.sleep(2)

    # Start bot scanning loop in main thread
    logger.info("Starting bot scan loop")
    try:
        bot_scan_loop()
    except KeyboardInterrupt:
        logger.info("Shutting down bot")
    except Exception as e:
        logger.error(f"Fatal error: {e}")

if __name__ == '__main__':
    main()
