# AI Compliance Agent for Aptos dApps

An AI-powered compliance and security agent that scans and validates smart contracts and dApp interactions on Aptos Blockchain, flagging anomalies and policy violations in real-time.

## Features

- 🔍 **Smart Contract Analysis** - Scan deployed Move modules for vulnerabilities
- 🛡️ **Compliance Policies** - Configurable rules for transaction validation
- 🤖 **AI-Powered Detection** - LLM-based anomaly detection and risk assessment
- ⚡ **Real-time Monitoring** - WebSocket-based live alerts
- 📊 **Risk Scoring** - Aggregated risk assessment with severity levels

## Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key (for AI analysis features)

### Installation

```bash
# Clone and navigate to project
cd aptoscomplyagent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your OpenAI API key
```

### Running the Server

```bash
python -m uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000` for the dashboard.

### API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation.

## Project Structure

```
app/
├── main.py              # FastAPI entry point
├── config.py            # Configuration settings
├── api/                 # REST API routes
├── core/                # Blockchain integration
├── ai/                  # AI analysis engine
└── models/              # Data models
frontend/                # Web dashboard
tests/                   # Test suite
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/contracts/analyze` | Analyze a smart contract |
| GET | `/api/contracts/{address}/modules` | List account modules |
| GET | `/api/transactions/{address}` | Get account transactions |
| POST | `/api/compliance/check` | Check compliance policies |
| WS | `/ws` | Real-time alerts WebSocket |

## Tech Stack

- **Backend**: FastAPI, Python 3.9+
- **Blockchain**: Aptos Python SDK
- **AI**: OpenAI GPT-4
- **Frontend**: Vanilla HTML/CSS/JS

## License

MIT
