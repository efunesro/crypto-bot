# 📁 ÍNDICE DE ARCHIVOS DEL BOT

## 📚 DOCUMENTACIÓN (Lee primero)

```
QUICKSTART.txt          → Lee esto PRIMERO (5 min setup)
README.md               → Documentación completa y explicada
SETUP_GUIDE.md          → Guía paso a paso detallada (Muy importante)
FILES_INDEX.md          → Este archivo (índice de todo)
```

## 🤖 CÓDIGO PRINCIPAL

```
crypto_scanner.py       → Core del bot (1200+ líneas)
                          - Dexscreener client
                          - RugCheck analyzer
                          - Scoring engine
                          - Discord alerts
                          - Database manager
                          
config.py               → Configuración (ajusta criterios aquí)
                          - Screening criteria
                          - Chains
                          - Scoring weights
                          - Alert thresholds
                          
utils.py                → Herramientas de utilidad
                          - Ver top tokens
                          - Estadísticas
                          - Buscar tokens
                          - Exportar datos
```

## ⚙️ CONFIGURACIÓN

```
.env.example            → Plantilla de variables (copia a .env)
config.py               → Parámetros del bot
.gitignore              → Para no subir archivos sensibles a GitHub
```

## 📦 DEPENDENCIAS

```
requirements.txt        → Librerías Python necesarias
Procfile                → Para Railway (production)
```

## 🎯 UTILIDADES

```
setup.sh                → Script automático de instalación (Mac/Linux)
dashboard.html          → Dashboard local para visualizar tokens
utils.py                → Menú interactivo para gestionar datos
```

---

## 🚀 ESTRUCTURA DE USO

```
1. LEE primero:
   ├─ QUICKSTART.txt (5 min)
   └─ SETUP_GUIDE.md (20 min)

2. CONFIGURA:
   ├─ Crea Discord webhook
   └─ Rellena .env

3. CORRE:
   └─ python crypto_scanner.py

4. MONITOREA:
   ├─ Discord (alertas)
   ├─ dashboard.html (visualización)
   └─ python utils.py (datos)

5. DEPLOY:
   └─ SETUP_GUIDE.md → Sección Railway
```

---

## 📊 BASE DE DATOS

**Archivo:** `crypto_scanner.db` (se crea automáticamente)

**Tablas:**
- `tokens` - Tokens encontrados
- `alerts_sent` - Historial de alertas
- `stats` - Estadísticas diarias

---

## 🎨 TAMAÑO DEL PROYECTO

```
crypto_scanner.py       ~1200 líneas
config.py               ~100 líneas
utils.py                ~300 líneas
dashboard.html          ~400 líneas
─────────────────────────────────
Total código            ~2000 líneas
```

---

## 🔧 HERRAMIENTAS INTEGRADAS

✅ **APIs (Gratis)**
- Dexscreener API
- RugCheck API
- Solscan API
- CoinGecko API

✅ **Servicios (Gratis)**
- Discord Webhooks
- Railway Cloud Hosting
- SQLite Database

✅ **Chains**
- Solana (principal)
- Ethereum
- BSC

---

## ⚡ RÁPIDO CHECKLIST

Para empezar:

- [ ] Leo QUICKSTART.txt
- [ ] Creo Discord webhook
- [ ] Descargo los archivos
- [ ] Ejecuto setup.sh (o setup manual)
- [ ] Relleno .env con webhook URL
- [ ] Corro: python crypto_scanner.py
- [ ] Veo alertas en Discord
- [ ] Deploy en Railway (opcional, para 24/7)

---

## 📞 SOPORTE RÁPIDO

**Error X**
- Mira `README.md` → Sección "TROUBLESHOOTING"
- O `SETUP_GUIDE.md` → Sección "TROUBLESHOOTING"
- O ejecuta: `python utils.py` → Ver logs

**No recibe alertas**
- Verifica webhook URL en .env
- Verifica permisos Discord
- Mira logs: `tail -f bot.log`

**Quiero cambiar criterios**
- Abre `config.py`
- Modifica `SCREENING_CRITERIA`
- Reinicia bot

---

## 🎯 SIGUIENTE PASO

👉 **Lee QUICKSTART.txt ahora mismo** (5 minutos)

Luego SETUP_GUIDE.md si necesitas más detalles.

---

**Versión:** 1.0.0  
**Actualizado:** 2026-04-29  
**Licencia:** Open Source (MIT)
