#!/bin/bash

# ===== CRYPTO BOT AUTO SETUP =====
# Script para instalación automática

echo "🚀 CRYPTO SCANNER BOT - AUTO SETUP"
echo "===================================="
echo ""

# Verificar Python
echo "📍 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Install from python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION found"
echo ""

# Crear venv
echo "📍 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "✅ venv already exists"
else
    python3 -m venv venv
    echo "✅ venv created"
fi

# Activar venv
echo "📍 Activating venv..."
source venv/bin/activate
echo "✅ venv activated"
echo ""

# Instalar dependencias
echo "📍 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed"
else
    echo "❌ Error installing dependencies"
    exit 1
fi
echo ""

# Crear .env
echo "📍 Setting up .env file..."
if [ -f ".env" ]; then
    echo "⚠️  .env already exists. Skipping..."
else
    cp .env.example .env
    echo "✅ .env created. Edit it with your Discord webhook URL"
fi
echo ""

# Crear database
echo "📍 Initializing database..."
python3 -c "from crypto_scanner import DatabaseManager; DatabaseManager('crypto_scanner.db')" 2>/dev/null
echo "✅ Database ready"
echo ""

echo "===================================="
echo "✅ SETUP COMPLETE!"
echo ""
echo "📋 NEXT STEPS:"
echo ""
echo "1️⃣  Edit .env with your Discord webhook URL"
echo "   nano .env"
echo ""
echo "2️⃣  Start the bot:"
echo "   source venv/bin/activate  # (si no está activado)"
echo "   python crypto_scanner.py"
echo ""
echo "3️⃣  Deploy to cloud (Railway):"
echo "   - Push code to GitHub"
echo "   - Connect Railway to GitHub"
echo "   - Add DISCORD_WEBHOOK_URL variable"
echo "   - Deploy"
echo ""
echo "📖 Documentación: README.md"
echo "===================================="
