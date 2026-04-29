#!/usr/bin/env python3
"""
Herramientas de utilidad para Crypto Scanner Bot
"""

import sqlite3
import json
from datetime import datetime, timedelta
from config import DB_PATH

def print_header(title):
    """Imprime header formateado"""
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50 + "\n")

def get_top_tokens(limit=10):
    """Obtiene top tokens por score"""
    print_header(f"TOP {limit} TOKENS")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute('''
        SELECT symbol, score, market_cap, liquidity, holders_count,
               top_holder_percent, buy_sell_ratio, risk_level
        FROM tokens
        ORDER BY score DESC
        LIMIT ?
    ''', (limit,))

    tokens = c.fetchall()

    if not tokens:
        print("📭 No tokens found yet.")
        return

    print(f"{'#':<3} {'SYMBOL':<10} {'SCORE':<7} {'MCAP':<12} {'HOLDERS':<10} {'RISK':<15}")
    print("-" * 70)

    for i, token in enumerate(tokens, 1):
        mcap_str = f"${token['market_cap']/1000:.0f}K"
        print(f"{i:<3} {token['symbol']:<10} {token['score']:<7.1f} {mcap_str:<12} {token['holders_count']:<10} {token['risk_level']:<15}")

    conn.close()

def get_statistics():
    """Obtiene estadísticas generales"""
    print_header("ESTADÍSTICAS")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Total de tokens
    c.execute("SELECT COUNT(*) FROM tokens")
    total_tokens = c.fetchone()[0]

    # Score promedio
    c.execute("SELECT AVG(score), MIN(score), MAX(score) FROM tokens")
    avg_score, min_score, max_score = c.fetchone()

    # Por risk level
    c.execute("SELECT risk_level, COUNT(*) FROM tokens GROUP BY risk_level")
    risk_stats = c.fetchall()

    # Tokens en últimas 24h
    c.execute('''
        SELECT COUNT(*) FROM tokens
        WHERE first_seen > datetime('now', '-1 day')
    ''')
    tokens_24h = c.fetchone()[0]

    # Alertas enviadas
    c.execute("SELECT COUNT(*) FROM alerts_sent")
    alerts_total = c.fetchone()[0]

    print(f"📊 Tokens Totales: {total_tokens}")
    print(f"📊 Últimas 24h: {tokens_24h}")
    print(f"📢 Alertas Enviadas: {alerts_total}")
    print()
    print(f"📈 Score Promedio: {avg_score:.2f if avg_score else 0}")
    print(f"📈 Score Mínimo: {min_score:.2f if min_score else 0}")
    print(f"📈 Score Máximo: {max_score:.2f if max_score else 0}")
    print()

    if risk_stats:
        print("🔴 Por Riesgo:")
        for risk_level, count in risk_stats:
            print(f"  {risk_level}: {count} tokens")

    conn.close()

def get_recent_alerts(limit=5):
    """Obtiene alertas recientes"""
    print_header(f"ÚLTIMAS {limit} ALERTAS")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute('''
        SELECT a.token_symbol, a.score, a.sent_at, t.risk_level, t.market_cap
        FROM alerts_sent a
        LEFT JOIN tokens t ON a.token_symbol = t.symbol
        ORDER BY a.sent_at DESC
        LIMIT ?
    ''', (limit,))

    alerts = c.fetchall()

    if not alerts:
        print("📭 No alerts sent yet.")
        return

    for alert in alerts:
        time_str = datetime.fromisoformat(alert['sent_at']).strftime("%H:%M:%S")
        print(f"⏰ {time_str} | {alert['token_symbol']} | Score: {alert['score']:.1f} | {alert['risk_level']}")

    conn.close()

def search_token(symbol):
    """Busca un token específico"""
    print_header(f"BÚSQUEDA: {symbol.upper()}")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM tokens WHERE symbol LIKE ? LIMIT 1", (f"%{symbol}%",))
    token = c.fetchone()

    if not token:
        print(f"❌ Token '{symbol}' not found")
        return

    print(f"\n🪙 SYMBOL: {token['symbol']}")
    print(f"💰 MARKET CAP: ${token['market_cap']:,.0f}")
    print(f"💧 LIQUIDITY: ${token['liquidity']:,.0f}")
    print(f"📈 VOLUMEN 24h: ${token['volume_24h']:,.0f}")
    print(f"💵 PRECIO: ${token['price']:.8f}")
    print(f"⏰ EDAD: {token['age_hours']:.1f} horas")
    print(f"👥 HOLDERS: {token['holders_count']}")
    print(f"📍 TOP HOLDER: {token['top_holder_percent']:.2f}%")
    print(f"📊 BUY/SELL RATIO: {token['buy_sell_ratio']:.2f}x")
    print(f"⚠️  HONEYPOT RISK: {token['honeypot_risk']:.1f}%")
    print(f"⭐ SCORE: {token['score']:.1f}/10")
    print(f"🔴 RISK LEVEL: {token['risk_level']}")
    print(f"⛓️  CHAIN: {token['chain']}")
    print(f"📋 CONTRACT: {token['contract']}")
    print(f"🕐 FIRST SEEN: {token['first_seen']}")

    conn.close()

def export_tokens(filename="tokens_export.json"):
    """Exporta todos los tokens a JSON"""
    print_header("EXPORTANDO TOKENS")

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("SELECT * FROM tokens ORDER BY score DESC")
    tokens = c.fetchall()

    data = []
    for token in tokens:
        data.append(dict(token))

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✅ Exported {len(data)} tokens to {filename}")
    conn.close()

def clear_old_data(days=30):
    """Limpia datos antiguos"""
    print_header(f"LIMPIANDO DATOS > {days} DÍAS")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Borrar tokens antiguos
    c.execute('''
        DELETE FROM tokens
        WHERE first_seen < datetime('now', '-' || ? || ' days')
    ''', (days,))

    deleted_tokens = c.rowcount

    # Borrar alertas antiguas
    c.execute('''
        DELETE FROM alerts_sent
        WHERE sent_at < datetime('now', '-' || ? || ' days')
    ''', (days,))

    deleted_alerts = c.rowcount

    conn.commit()
    conn.close()

    print(f"🗑️  Deleted {deleted_tokens} old tokens")
    print(f"🗑️  Deleted {deleted_alerts} old alerts")
    print("✅ Cleanup complete")

def main():
    """Menú principal"""
    print("\n🤖 CRYPTO SCANNER - UTILS")
    print("="*50)
    print("1. Ver top tokens")
    print("2. Ver estadísticas")
    print("3. Ver alertas recientes")
    print("4. Buscar token específico")
    print("5. Exportar tokens a JSON")
    print("6. Limpiar datos antiguos")
    print("7. Salir")
    print("="*50)

    choice = input("\nSelecciona opción (1-7): ").strip()

    if choice == "1":
        limit = input("¿Cuántos tokens? (default 10): ").strip() or "10"
        get_top_tokens(int(limit))

    elif choice == "2":
        get_statistics()

    elif choice == "3":
        limit = input("¿Cuántas alertas? (default 5): ").strip() or "5"
        get_recent_alerts(int(limit))

    elif choice == "4":
        symbol = input("Nombre del token: ").strip()
        if symbol:
            search_token(symbol)

    elif choice == "5":
        filename = input("Nombre del archivo (default tokens_export.json): ").strip() or "tokens_export.json"
        export_tokens(filename)

    elif choice == "6":
        days = input("¿Cuántos días atrás? (default 30): ").strip() or "30"
        confirm = input(f"¿Eliminar datos > {days} días? (s/n): ").strip().lower()
        if confirm == "s":
            clear_old_data(int(days))

    elif choice == "7":
        print("👋 Bye!")
        return

    input("\n[Presiona Enter para continuar...]")
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
