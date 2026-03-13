<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">share-investment-agent</h1>

<p align="center">
  <strong>A comprehensive AI agent for Chinese A-share investment analysis</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/share-investment-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/share-investment-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://img.shields.io/github/license/Paraschamoli/share-investment-agent">
    <img src="https://img.shields.io/github/license/Paraschamoli/share-investment-agent" alt="License">
  </a>
  <img src="https://img.shields.io/badge/status-production%20ready-brightgreen" alt="Status">
</p>

---

## 📖 Overview

A sophisticated AI-powered investment analysis agent specifically designed for Chinese A-share markets. Built on the [Bindu Agent Framework](https://github.com/getbindu/bindu) for Internet of Agents, providing comprehensive financial analysis through multiple specialist agents.

**Key Capabilities:**
- � **Technical Analysis**: MACD, RSI, Bollinger Bands, Moving Averages, Volume Analysis
- 💰 **Fundamental Analysis**: ROE, debt ratios, margins, growth rates, cash flow analysis
- 📰 **Sentiment Analysis**: News sentiment, social media analysis, market psychology
- 💎 **Valuation Analysis**: DCF analysis, comparable company analysis, scenario modeling
- 🐂 **Bullish Research**: Optimistic investment thesis and growth opportunities
- 🐻 **Bearish Research**: Risk assessment and downside analysis
- ⚖️ **Debate Room**: Balanced synthesis of bull/bear arguments
- �️ **Risk Management**: VaR calculation, stress testing, risk mitigation
- 🌍 **Macro Analysis**: Economic indicators, policy impact, market cycles
- 📈 **Portfolio Management**: Final investment decisions with position sizing

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- OpenRouter API key (free tier available)

### Installation

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/share-investment-agent.git
cd share-investment-agent

# Create virtual environment
uv venv --python 3.12.9
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
```

### Configuration

Edit `.env` and add your API keys:

| Key | Get It From | Required |
|-----|-------------|----------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | If you want to use Mem0 tools |

### Run the Agent

```bash
# Start the investment analysis agent
uv run -m share_investment_agent

# Agent will be available at http://localhost:3773
```

### Github Setup

```bash
# Initialize git repository and commit your code
git init -b main
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push (replace with your GitHub username)
gh repo create Paraschamoli/share-investment-agent --public --source=. --remote=origin --push
```

---

## 💡 Usage

### Example Queries

```bash
# Comprehensive analysis request
"Provide balanced investment analysis for Ping An Bank (000001) including:
- Technical analysis with MACD, RSI, Bollinger Bands
- Fundamental analysis with profitability metrics
- Sentiment analysis with market psychology
- Valuation analysis with DCF
- Bullish researcher perspective
- Bearish researcher perspective
- Debate room synthesis
- Final portfolio management recommendation"

# Quick analysis
"Analyze stock 000001 for investment potential"

# Risk-focused analysis
"What are the main risks and opportunities for Tencent (007)?"
```

### Input Formats

**Plain Text:**
```
Analyze [TICKER] for investment opportunities including technical, fundamental, and sentiment analysis
```

**JSON:**
```json
{
  "ticker": "000001",
  "analysis_type": "comprehensive",
  "focus": ["technical", "fundamental", "sentiment", "valuation"]
}
```

### Output Structure

The agent returns comprehensive investment reports with:
- **Final Investment Decision**: Action (BUY/SELL/HOLD), confidence, position sizing
- **Technical Analysis**: Trading signals, indicator analysis, chart patterns
- **Fundamental Analysis**: Profitability, growth, financial health metrics
- **Sentiment Analysis**: Market sentiment, news analysis, psychology factors
- **Valuation Analysis**: Intrinsic value, DCF models, relative valuation
- **Research Team Perspectives**: Bullish and bearish theses with confidence scores
- **Debate Room Outcome**: Balanced synthesis and mixed confidence
- **Risk Assessment**: Risk levels, VaR estimates, mitigation strategies
- **Macro Analysis**: Economic outlook, policy impact, market cycles

---

## 🔌 API Usage

The agent exposes a RESTful API when running. Default endpoint: `http://localhost:3773`

### Quick Start

For complete API documentation, request/response formats, and examples, visit:

📚 **[Bindu API Reference - Send Message to Agent](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)**


### Additional Resources

- 📖 [Full API Documentation](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)
- 📦 [Postman Collections](https://github.com/GetBindu/Bindu/tree/main/postman/collections)
- 🔧 [API Reference](https://docs.getbindu.com)

---

## 🎯 Skills

### share_investment (v1.0.0)

**Primary Capability:**
- Comprehensive Chinese A-share investment analysis using multiple specialist agents
- Multi-agent debate system for balanced investment recommendations
- Risk-aware portfolio management with position sizing

**Features:**
- 10+ specialist agents covering all aspects of investment analysis
- Real-time market data integration with Akshare API
- Advanced technical indicators and chart pattern recognition
- Fundamental financial metrics and DCF valuation models
- Sentiment analysis from news and social media
- Bull/bear research with structured debate methodology
- Comprehensive risk management with VaR calculations
- Macro-economic analysis and policy impact assessment

**Best Used For:**
- Chinese A-share investment research and analysis
- Portfolio risk assessment and optimization
- Market sentiment and trend analysis
- Fundamental valuation and technical trading signals
- Multi-perspective investment decision making

**Not Suitable For:**
- Real-time trading execution (analysis only)
- Cryptocurrency or non-A-share markets
- High-frequency trading strategies
- Automated portfolio rebalancing

**Performance:**
- Average processing time: ~360 seconds (comprehensive multi-agent analysis)
- Max concurrent requests: 1 (sequential processing)
- Memory per request: ~500MB (multi-agent LLM processing)

---

## 🐳 Docker Deployment

### Local Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Agent will be available at http://localhost:3773
```

### Docker Configuration

The agent runs on port `3773` and requires:
- `OPENROUTER_API_KEY` environment variable
- `MEM0_API_KEY` environment variable

Configure these in your `.env` file before running.

### Production Deployment

```bash
# Use production compose file
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🌐 Deploy to bindus.directory

Make your agent discoverable worldwide and enable agent-to-agent collaboration.

### Setup GitHub Secrets

```bash
# Authenticate with GitHub
gh auth login

# Set deployment secrets
gh secret set BINDU_API_TOKEN --body "<your-bindu-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

Get your keys:
- **Bindu API Key**: [bindus.directory](https://bindus.directory) dashboard
- **Docker Hub Token**: [Docker Hub Security Settings](https://hub.docker.com/settings/security)

### Deploy

```bash
# Push to trigger automatic deployment
git push origin main
```

GitHub Actions will automatically:
1. Build your agent
2. Create Docker container
3. Push to Docker Hub
4. Register on bindus.directory

---

## 🛠️ Development

### Project Structure

```
share-investment-agent/
├── share_investment_agent/
│   ├── skills/
│   │   └── share_investment/
│   │       ├── skill.yaml          # Skill configuration
│   │       └── __init__.py
│   ├── agents.py                  # Multi-agent system implementation
│   ├── tools/
│   │   ├── data_acquisition.py    # Market data collection
│   │   └── financial_analysis.py  # Financial metrics calculation
│   ├── utils/
│   │   └── logging_config.py     # Logging configuration
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py                   # Agent entry point
│   └── agent_config.json         # Agent configuration
├── tests/
│   └── test_main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile.agent
└── pyproject.toml
```

### Running Tests

```bash
uv run pytest              # Run all tests
uv run pytest --cov       # With coverage report
```

### Code Quality

```bash
uv run ruff check          # Run linter
uv run ruff format         # Format code
uv run ty check .          # Type checking
uv run pre-commit run -a   # All pre-commit checks
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run manually
uv run pre-commit run -a
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Powered by Bindu

Built with the [Bindu Agent Framework](https://github.com/getbindu/bindu)

**Why Bindu?**
- 🌐 **Internet of Agents**: A2A, AP2, X402 protocols for agent collaboration
- ⚡ **Zero-config setup**: From idea to production in minutes
- 🛠️ **Production-ready**: Built-in deployment, monitoring, and scaling

**Build Your Own Agent:**
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

## 📚 Resources

- 📖 [Full Documentation](https://Paraschamoli.github.io/share-investment-agent/)
- 💻 [GitHub Repository](https://github.com/Paraschamoli/share-investment-agent/)
- 🐛 [Report Issues](https://github.com/Paraschamoli/share-investment-agent/issues)
- 💬 [Join Discord](https://discord.gg/3w5zuYUuwt)
- 🌐 [Agent Directory](https://bindus.directory)
- 📚 [Bindu Documentation](https://docs.getbindu.com)

---

<p align="center">
  <strong>Built with 💛 for intelligent investment analysis 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/share-investment-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://bindus.directory">🌐 Agent Directory</a>
</p>
