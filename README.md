# AI Compliance Agent for Multi-Chain dApps

An AI-powered compliance and security agent that scans and validates smart contracts across multiple blockchains, including Ethereum, Solana, and Aptos. The system performs real-time analysis to detect security vulnerabilities, policy violations, and anomalous contract behavior using advanced pattern matching and risk assessment techniques.

Security and compliance rules are expressed as human-readable policies, allowing the agent to reason across multiple analysis tools and on-chain signals. For every detected issue, the agent provides a clear explanation of the risk, the underlying reasoning, and actionable recommendations to enable immediate mitigation and informed decision-making in production environments.

## 🚀 Features

### Core Capabilities
- 🔍 **Multi-Language Smart Contract Scanner**
  - **Move** (Aptos) - Detects missing signer checks, capability issues, state mutations
  - **Solidity** (Ethereum) - Identifies tx.origin, delegatecall, selfdestruct vulnerabilities
  - **Rust** (Solana) - Catches unwrap(), unsafe blocks, unchecked arithmetic
  - Pattern-based vulnerability detection with 15+ security checks
  - Full contract display with animated scanning visualization
  - Manual code input and demo vulnerable contracts
  - **File Upload**: Upload smart contract files for analysis with on-demand.io Media API

- 📊 **Real-Time Transaction Dashboard**
  - Live transaction monitoring for Aptos addresses
  - Transaction detail modal with comprehensive metadata
  - Compliance status tracking with severity levels
  - WebSocket-based real-time alerts and updates
  - Transaction hash display and verification

- 🤖 **6 Specialized AI Agents** (Powered by on-demand.io)
  - **🛡️ Security Advisor**: Vulnerability analysis and remediation
  - **✅ Compliance Checker**: Regulatory standards verification
  - **⚡ Code Optimizer**: Performance improvement suggestions
  - **📚 Vulnerability Explainer**: Educational security explanations
  - **💰 Gas Optimizer**: Cost reduction strategies
  - **📝 Audit Generator**: Comprehensive audit reports
  - Interactive chat interface with session management
  - Context-aware assistance with code analysis integration

- 🤖 **AI-Powered Risk Assessment**
  - Automated risk scoring (0-100 scale)
  - Severity classification (Critical/High/Medium/Low)
  - Anomaly detection with pattern recognition
  - Vulnerability impact analysis with recommendations
  - Policy engine for compliance validation
  - Agentic Security Analysis


## 🎯 Quick Start

### Prerequisites

- **Backend**: Python 3.9+
- **Frontend**: Node.js 18+ and npm
- **Optional**: OpenAI API key (for enhanced AI analysis features)

### Installation

#### Backend Setup

```bash
# Navigate to project root
cd aptoscomplyagent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install Python dependencies
pip install -r requirements.txt

# Configure environment (optional for OpenAI)
cp .env.example .env
# Edit .env with your OpenAI API key if using AI features
```

#### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend-next

# Install Node dependencies
npm install

### Contract Analysis
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/contracts/analyze` | Analyze a deployed contract on Aptos |
| POST | `/api/contracts/analyze-code` | Analyze contract source code (Move/Solidity/Rust) |
| GET | `/api/contracts/demo-contracts` | Get demo vulnerable contracts |
| GET | `/api/contracts/{address}/modules` | List account modules |

### Transaction Monitoring
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/transactions/{address}` | Get account transactions |
| POST | `/api/transactions/monitor` | Start monitoring an address |
| GET | `/api/transactions/{hash}/details` | Get transaction details |

### Compliance & Risk
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/compliance/check` | Check compliance policies |
| POST | `/api/compliance/validate` | Validate transaction compliance |
| GET | `/api/compliance/policies` | List available policies |

### AI Agents
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/agents/list` | List all available AI agents |
| POST | `/api/agents/chat` | Chat with specific agent |
| POST | `/api/agents/analyze-with-agents` | Multi-agent analysis |

### Real-Time Updates
| Method | Endpoint | Description |
|--------|----------|-------------|
| WS | `/ws` | WebSocket for real-time alerts |
| GET | `/health` | Health check endpoint |

### Demo Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/demo/vulnerable-contracts` | Get vulnerable contract examples |
| POST | `/api/demo/simulate-attack` | Simulate attack scenariosst suite
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
└── MULTI_LANGUAGE_TESTING.md       # Multi-language testing guid

Backend will run at `http://localhost:8000`

#### Start Frontend Server

```bash
# From frontend-next directory
npm run dev
```

Frontend will run at `http://localhost:3000`

### Access Points

- **Landing Page**: http://localhost:3000
- **Smart Contract Scanner**: http://localhost:3000/scanner
- **Transaction Dashboard**: http://localhost:3000/dashboard
- **🤖 AI Agents**: http://localhost:3000/agents
- **API Documentation**: http://localhost:8000/docs

## 🤖 AI Agents Feature

### Overview
6 specialized AI agents powered by on-demand.io Chat & Agent Tools API provide comprehensive smart contract assistance:

1. **Security Advisor** - Analyzes vulnerabilities and provides remediation
2. **Compliance Checker** - Verifies regulatory compliance
3. **Code Optimizer** - Suggests performance improvements
4. **Vulnerability Explainer** - Educational security explanations
5. **Gas Optimizer** - Cost reduction strategies
6. **Audit Generator** - Comprehensive audit reports

### Usage
- Navigate to `/agents` page
- Click on any agent card to start a conversation
- Ask questions about smart contracts, security, compliance
- Get expert AI assistance with context from your analyses

For detailed documentation, see [AI_AGENTS_INTEGRATION.md](AI_AGENTS_INTEGRATION.md)

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.9+)
- **Database**: MongoDB (Motor async driver)
- **Blockchain SDKs**: 
  - Aptos Python SDK
  - Web3.py (Ethereum)
  - Solana.py (Solana)
- **AI/ML**: 
  - Groq API (llama-3.3-70b-versatile)
  - on-demand.io Chat & Agent Tools API
- **Real-time**: WebSockets
- **API Docs**: Swagger/OpenAPI
- **File Processing**: on-demand.io Media API

### Frontend
- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **UI Components**: React 19
- **3D Graphics**: Three.js, React Three Fiber
- **Styling**: CSS Modules, Custom CSS
- **State Management**: React Hooks
- **HTTP Client**: Fetch API

### Third-Party Integrations
- **on-demand.io**: AI agents and media processing
- **Groq**: LLM-powered vulnerability detection
- **MongoDB**: Contract storage and analytics

### Blockchain Support
- **Aptos**: Move language analysis
- **Ethereum**: Solidity contract scanning
- **Solana**: Rust program analysis

## 🔍 Vulnerability Detection Patterns

### Move (Aptos) - 4 Patterns
- ❌ Missing signer authorization (CRITICAL)
- ⚠️ Capability struct with copy ability (HIGH)
- ⚠️ Public functions with state mutation (HIGH)
- ⚡ Global state mutation operations (MEDIUM)

### Solidity (Ethereum) - 6 Patterns
- ❌ tx.origin for authorization (CRITICAL)
- ⚠️ selfdestruct usage (HIGH)
- ⚠️ delegatecall to user addresses (HIGH)
- ⚠️ Unprotected public functions (HIGH)
- ⚡ transfer/send instead of call (MEDIUM)
- ⚡ block.timestamp dependency (MEDIUM)

### Rust (Solana) - 5 Patterns
- ❌ Missing signer validation (CRITICAL)
- ⚠️ Unchecked arithmetic operations (HIGH)
- ⚠️ Unsafe blocks without validation (HIGH)
- ⚡ unwrap() without error handling (MEDIUM)
- ⚡ Missing account constraints (MEDIUM)

## 📚 Documentation

- **[Multi-Language Testing Guide](MULTI_LANGUAGE_TESTING.md)** - Complete guide with test examples for all supported languages
- **[API Documentation](http://localhost:8000/docs)** - Interactive Swagger UI (when backend running)
- **[Frontend README](frontend-next/README.md)** - Next.js-specific documentation

## 🧪 Testing

### Backend Tests
```bash
# Run Python tests
pytest tests/

# Run with coverage
pytest --cov=app tests/
```

### Frontend Tests
```bash
# Navigate to frontend
cd frontend-next

# Run tests (if configured)
npm test
```

### Manual Testing
See [MULTI_LANGUAGE_TESTING.md](MULTI_LANGUAGE_TESTING.md) for:
- Vulnerable contract examples
- Expected detection results
- Step-by-step testing procedures

## 🚀 Deployment

### Backend Deployment
```bash
# Production server
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Or with uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Frontend Deployment
```bash
# Build production bundle
cd frontend-next
npm run build

# Start production server
npm start
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- Aptos Labs for the Move language and blockchain infrastructure
- Ethereum Foundation for Solidity standards
- Solana Labs for Rust/Anchor framework
- OpenAI for AI analysis capabilities

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review test examples in MULTI_LANGUAGE_TESTING.md

---

## 🚀 Deployment

The application is production-ready with deployment configurations for:

- **Backend**: Render (recommended) or Azure
- **Frontend**: Vercel

### Quick Deploy

```bash
# Run deployment guide
./deploy.sh
```

### Backend (Render)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → New → Blueprint
3. Connect repository (render.yaml auto-detected)
4. Set environment variables:
   ```
   ONDEMAND_API_KEY=XBKmaTtF167mfnJaEQte41YZbw6zj08S
   GROQ_API_KEY=your_groq_key (optional)
   CORS_ORIGINS=https://your-app.vercel.app
   ```

### Frontend (Vercel)

1. Go to [vercel.com](https://vercel.com) → New Project
2. Import repository, set root: `frontend-next`
3. Set environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://aptoscomply-backend.onrender.com
   ```
4. Deploy!

**📚 Full Guide**: See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

---

**Built with ❤️ for secure multi-chain dApp development** core/                # Blockchain integration
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
