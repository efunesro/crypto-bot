# 🤖 CRYPTO SCANNER BOT - ENTERPRISE EDITION

**Bot profesional de screening on-chain 24/7 | Multi-chain | 100% Gratuito**

---

## 📋 ¿QUÉ INCLUYE?

✅ **Scanning automático** cada 5 minutos  
✅ **Multi-chain** (Solana, Ethereum, BSC)  
✅ **APIs públicas** (0 costo)  
✅ **Análisis anti-scam** (honeypot detection)  
✅ **Scoring inteligente** (0-10)  
✅ **Alertas Discord** en tiempo real  
✅ **Database SQLite** con histórico  
✅ **Deployment cloud gratuito** (Railway.app)  

---

## 🚀 INSTALACIÓN RÁPIDA (5 MIN)

### **PASO 1: Requisitos**
```bash
# Necesitas tener instalado:
- Python 3.9+
- Git
- Cuenta en Railway.app (gratis)
```

### **PASO 2: Clonar/Descargar el repo**
```bash
# Opción 1: Si tienes git
git clone <tu-repo>
cd crypto-bot

# Opción 2: Manual
# Descarga los archivos en una carpeta
```

### **PASO 3: Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **PASO 4: Crear servidor Discord**
```
1. Ve a https://discord.new
2. Nombra tu servidor "Crypto Bot"
3. Crea un canal #alertas
4. Click derecho en canal → Integrations → Webhooks
5. New Webhook → Copy URL
```

### **PASO 5: Configurar variables**
```bash
# Crea archivo .env
echo "DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/TU_WEBHOOK_URL" > .env
```

### **PASO 6: Prueba local**
```bash
python crypto_scanner.py
```

Deberías ver:
```
🚀 CRYPTO SCANNER BOT - STARTING
✅ Bot ready. Waiting for first scan...
```

---

## ☁️ DEPLOYMENT EN RAILWAY (CLOUD GRATUITO)

### **PASO 1: Crear cuenta Railway**
1. Ve a https://railway.app
2. Sign up con GitHub (gratis)
3. Click "New Project"

### **PASO 2: Conectar GitHub**
```bash
# Sube tu código a GitHub
git push origin main

# En Railway:
# 1. Add from GitHub
# 2. Selecciona tu repo
```

### **PASO 3: Configurar variables**
En Railway dashboard:
```
Variables → New Variable
Nombre: DISCORD_WEBHOOK_URL
Valor: Tu webhook URL
```

### **PASO 4: Deploy**
```bash
# En Railway:
Click "Deploy" 
Espera a que diga "Running"
```

✅ Tu bot corre 24/7 en cloud GRATIS

---

## 🎯 CÓMO AJUSTAR CRITERIOS

Abre `config.py`:

```python
SCREENING_CRITERIA = {
    "liquidity_min": 10000,          # Cambiar si quieres riesgos mayores
    "market_cap_min": 50000,         # Bajar para tokens ultra nuevos
    "pair_age_min_hours": 0.5,       # Bajar para earlies
    "volume_24h_min": 10000,         # Volumen mínimo
    "top_holder_max_percent": 30,    # % máximo top holder (< 30 es safe)
    "min_holders": 50,               # Mínimo holders
    "buy_sell_ratio_min": 1.2,       # Compras > ventas
    "max_honeypot_risk": 30,         # Risk score máximo
}
```

**Perfiles predefinidos:**

```python
# CONSERVATIVE (Muy seguro, pocos false positives)
liquidity_min: 25000
market_cap_min: 100000
top_holder_max_percent: 20

# AGGRESSIVE (Más riesgos, más oportunidades)
liquidity_min: 5000
market_cap_min: 25000
top_holder_max_percent: 40

# ULTRA (Earlies, máximo riesgo)
liquidity_min: 1000
market_cap_min: 5000
pair_age_min_hours: 0.1
```

---

## 📊 ENTENDIENDO LAS ALERTAS

Cuando recibas alerta en Discord:

```
🚨 TOKEN ENCONTRADO: MOON
SCORE: 8.5/10
🟢 RIESGO: SAFE
💰 Market Cap: $125,000
💧 Liquidity: $12,500
📈 Volumen 24h: $45,000
⏰ Edad: 2.5h
👥 Holders: 234
📍 Top Holder: 2.8%
📊 Buy/Sell Ratio: 2.1x
```

**Significado:**
- **Score 8+** = Token prometedor
- **Top Holder < 10%** = Distribución muy buena
- **Buy/Sell > 1.5** = Buena presión de compra
- **🟢 SAFE** = No honeypot detectado

---

## 🔴 RED FLAGS EN ALERTAS

**Evita si ves:**
- Top Holder > 50%
- Buy/Sell Ratio < 1.0
- Risk Level = 🔴 DANGER
- Honeypot Risk > 50%

---

## 📱 COMANDOS ÚTILES

```bash
# Ver logs en tiempo real
tail -f bot.log

# Ver datos encontrados
sqlite3 crypto_scanner.db "SELECT symbol, score, risk_level FROM tokens ORDER BY score DESC LIMIT 10;"

# Limpiar base de datos (CUIDADO)
rm crypto_scanner.db

# Cambiar intervalo de scan
# En config.py: SCAN_INTERVAL_SECONDS = 300  (5 min)
```

---

## 📈 ESTADÍSTICAS

Después de 24h, el bot tendrá:
- 288 scans completados (cada 5 min)
- ~50-200 tokens analizados
- ~5-20 alertas enviadas (según criterios)
- Database con histórico

Para ver stats:
```bash
sqlite3 crypto_scanner.db "SELECT COUNT(*) as total_tokens, AVG(score) as avg_score FROM tokens;"
```

---

## 🆘 TROUBLESHOOTING

**Error: "Discord webhook not found"**
```
→ Verifica que el webhook URL es correcto
→ Comprueba que el canal #alertas existe
```

**Error: "Rate limit exceeded"**
```
→ El bot espera automáticamente
→ Aumenta SCAN_INTERVAL_SECONDS en config.py
```

**Bot no envía alertas**
```
→ Verifica ALERT_THRESHOLDS["score_min"] en config.py
→ Verifica que el canal tiene permisos
```

**Database corrupted**
```
→ rm crypto_scanner.db
→ Reinicia el bot (recrea DB)
```

---

## 🔒 SEGURIDAD

✅ **No guardamos claves privadas**  
✅ **No conectamos wallets**  
✅ **Solo datos públicos de blockchain**  
✅ **Webhook Discord es local**  
✅ **Database local (tu máquina)**  

---

## 📈 ROADMAP FUTURO

- [ ] Photon API integration (si tienes suscripción)
- [ ] Telegram alerts
- [ ] Email reports
- [ ] Web dashboard
- [ ] Telegram bot commands
- [ ] Smart money tracker
- [ ] Backtesting engine

---

## 💡 TIPS PRO

1. **Ajusta criterios según tu risk tolerance**
2. **No entres en todos los alertas** - filtra por score
3. **Mantén cuidado con top holder % > 30%**
4. **Espera confirmación de volumen antes de entrar**
5. **Guarda un registro de trades en Excel**

---

## 📞 SOPORTE

Si algo no funciona:

1. **Verifica Python 3.9+**: `python --version`
2. **Verifica dependencias**: `pip list | grep requests`
3. **Mira logs**: `tail -f bot.log`
4. **Reset completo**:
   ```bash
   rm crypto_scanner.db
   python crypto_scanner.py
   ```

---

## 📜 LICENSE

Open Source | MIT | Úsalo libremente

---

**Creado con ❤️ para traders inteligentes**

**Última actualización:** 2026-04-29  
**Versión:** 1.0.0
