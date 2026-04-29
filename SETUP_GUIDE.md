# 🚀 GUÍA DE SETUP COMPLETA - PASO A PASO

## 📋 TABLA DE CONTENIDOS
1. [Requisitos](#requisitos)
2. [Crear Discord Webhook](#crear-discord-webhook)
3. [Setup Local (Tu Máquina)](#setup-local)
4. [Deploy en Railway (Cloud Gratis)](#deploy-en-railway)
5. [Verificar que Funciona](#verificar-que-funciona)

---

## ✅ REQUISITOS

Necesitas tener (gratis):
- [ ] Python 3.9+ instalado (https://python.org)
- [ ] Git instalado (https://git-scm.com) [Opcional pero recomendado]
- [ ] Cuenta Discord (https://discord.com)
- [ ] Cuenta Railway (https://railway.app) [Gratis]
- [ ] Cuenta GitHub (https://github.com) [Gratis, para Railway]

**Tiempo total:** ~20 minutos

---

## 🎮 CREAR DISCORD WEBHOOK (5 MIN)

### **PASO 1: Crear Servidor Discord**

1. Ve a https://discord.new
2. Dale un nombre (ej: "Crypto Bot")
3. Elige "For me and my friends"
4. Click "Create"

✅ Servidor creado

### **PASO 2: Crear Canal #alertas**

1. En tu servidor, click en **+** (junto a "CHANNELS")
2. Selecciona "Text Channel"
3. Nombre: `alertas`
4. Click "Create Channel"

✅ Canal creado

### **PASO 3: Crear Webhook**

1. En el canal #alertas, click en **⚙️ (Settings)**
2. En el sidebar, selecciona **Integrations**
3. Click en **Webhooks**
4. Click en **New Webhook**
5. Dale un nombre: `CryptoBot`
6. Click en **Copy Webhook URL**

```
Verás algo así:
https://discord.com/api/webhooks/123456789/abc_def_ghi
```

✅ **GUARDA ESTA URL - LA NECESITARÁS**

---

## 💻 SETUP LOCAL (Tu Máquina)

### **PASO 1: Descargar los archivos**

**Opción A: Con Git** (recomendado)
```bash
# Abre terminal/PowerShell
git clone https://github.com/TU_USUARIO/crypto-bot.git
cd crypto-bot
```

**Opción B: Manual**
1. Descarga la carpeta `crypto-bot` completa
2. Abre terminal en esa carpeta

### **PASO 2: Ejecutar setup automático**

**En Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**En Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x setup.sh
./setup.sh
```

✅ Dependencias instaladas

### **PASO 3: Configurar Discord Webhook**

1. Abre el archivo `.env` (copia `.env.example` si no existe)

**Contenido de .env:**
```
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/TU_WEBHOOK_URL
LOG_LEVEL=INFO
SCAN_INTERVAL=300
```

2. Reemplaza `TU_WEBHOOK_URL` con tu webhook URL real

3. Guarda el archivo

✅ Webhook configurado

### **PASO 4: Prueba Local**

```bash
# Asegúrate que venv está activado
python crypto_scanner.py
```

Deberías ver:
```
🚀 CRYPTO SCANNER BOT - STARTING
✅ Bot ready. Waiting for first scan...
```

**Presiona Ctrl+C para detener**

✅ Bot funcionando localmente

---

## ☁️ DEPLOY EN RAILWAY (Cloud Gratis)

Railway ejecuta tu bot 24/7 sin que tengas que dejar tu computadora encendida.

### **PASO 1: Crear cuenta Railway**

1. Ve a https://railway.app
2. Click "Sign Up"
3. Elige "Login with GitHub" o "Login with Google"
4. Completa el registro

✅ Cuenta creada

### **PASO 2: Crear Repo en GitHub**

1. Ve a https://github.com/new
2. Nombre: `crypto-bot`
3. Descripción: "Crypto Scanner Bot 24/7"
4. Click "Create repository"

✅ Repo creado

### **PASO 3: Subir código a GitHub**

En tu carpeta `crypto-bot`, abre terminal y ejecuta:

```bash
# Inicializar git
git init

# Agregar archivos
git add .

# Commit
git commit -m "Initial commit: Crypto Scanner Bot"

# Agregar remoto (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/crypto-bot.git

# Subir a GitHub
git branch -M main
git push -u origin main
```

✅ Código en GitHub

### **PASO 4: Conectar Railway a GitHub**

1. Ve a https://railway.app/dashboard
2. Click en "+ New Project"
3. Selecciona "Deploy from GitHub"
4. Haz login con GitHub
5. Selecciona tu repo `crypto-bot`
6. Click "Deploy"

✅ Proyecto creado en Railway

### **PASO 5: Configurar Variables**

En Railway dashboard:

1. Click en tu proyecto
2. Ve a la pestaña **Variables**
3. Click "+ New Variable"
4. Configura:
   ```
   DISCORD_WEBHOOK_URL = https://discord.com/api/webhooks/...
   LOG_LEVEL = INFO
   ```

✅ Variables configuradas

### **PASO 6: Deploy**

Railway debería estar deployando automáticamente. Espera a que muestre:
```
✓ Service Running
```

✅ **¡Tu bot está corriendo en cloud!**

---

## 🧪 VERIFICAR QUE FUNCIONA

### **Verificar localmente:**

1. Abre el Discord (#alertas)
2. Ejecuta `python crypto_scanner.py`
3. Espera ~5 minutos
4. Deberías ver mensajes en Discord como:

```
🚨 TOKEN ENCONTRADO: MOON
SCORE: 8.5/10
🟢 RIESGO: SAFE
...
```

### **Verificar en Railway:**

1. Ve a https://railway.app/dashboard
2. Click en tu proyecto
3. Ve a "Deployments"
4. Deberías ver status: ✅ Deploying o ✅ Active
5. Click en "Logs" para ver que el bot está corriendo

Si ves esto, ¡está perfecto!:
```
🚀 CRYPTO SCANNER BOT - STARTING
✅ Bot ready. Waiting for first scan...
```

---

## 🎛️ AJUSTAR PARÁMETROS

**Para cambiar qué tokens alerta:**

1. Abre `config.py`
2. Modifica `SCREENING_CRITERIA`

Ejemplos:

```python
# MÁS CONSERVADOR (menos falsas alarmas)
"liquidity_min": 25000,
"market_cap_min": 100000,
"top_holder_max_percent": 20,

# MÁS AGRESIVO (más oportunidades, más riesgo)
"liquidity_min": 5000,
"market_cap_min": 25000,
"top_holder_max_percent": 40,
```

3. Haz commit y push a GitHub
4. Railway redeploy automáticamente

---

## 🆘 TROUBLESHOOTING

### **Discord no recibe alertas:**
```
1. Verifica que el webhook URL es correcto en .env
2. Verifica permisos del bot en Discord
3. Mira los logs: cat bot.log
```

### **Error "Rate limit exceeded":**
```
Aumenta SCAN_INTERVAL en config.py:
SCAN_INTERVAL_SECONDS = 600  # En lugar de 300
```

### **Railway dice "Failed to build":**
```
1. Verifica que requirements.txt está completo
2. Que Procfile existe y está correcto
3. Que NO hay errores en el código
```

### **Database corrupted:**
```
rm crypto_scanner.db
El bot recrea la base de datos automáticamente
```

---

## 📊 MONITOREAR EL BOT

### **Ver logs en Railway:**
1. Dashboard → Proyecto → Logs
2. Filtra por nivel "INFO" o "ERROR"

### **Ver tokens encontrados:**
```bash
sqlite3 crypto_scanner.db \
  "SELECT symbol, score, risk_level FROM tokens ORDER BY score DESC LIMIT 10;"
```

### **Ver estadísticas:**
```bash
sqlite3 crypto_scanner.db \
  "SELECT COUNT(*) as total, AVG(score) as avg_score FROM tokens;"
```

---

## 🚀 ¡LISTO!

Tu bot está ahora corriendo 24/7 en la nube sin costo.

**Próximos pasos:**
- [ ] Monitorea Discord diariamente para alertas
- [ ] Ajusta criterios si hay muchos falsos positivos
- [ ] Investiga los tokens que alertan
- [ ] Mantén un registro de trades

---

## 📚 Recursos Útiles

- Documentación de Discord Webhooks: https://discord.com/developers/docs/resources/webhook
- Railway Docs: https://docs.railway.app
- Python Docs: https://docs.python.org/3
- Dexscreener API: https://docs.dexscreener.com

---

**¡Dudas? Lee README.md o ejecuta `python crypto_scanner.py --help`**

**Última actualización:** 2026-04-29
