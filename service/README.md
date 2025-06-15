# SimpleAgent Service

Visual browser automation platform built with Python, FastAPI, and browser-use.

## Features

- **Browser Automation Engine**: Powered by browser-use with Playwright backend
- **Visual Agent Builder API**: RESTful API for creating and managing agents
- **Secure File Tools**: Granular file system access with permissions
- **Workflow Orchestration**: Sequential and parallel execution support
- **Real-time Monitoring**: Execution tracking and debugging

## Installation

1. **Create virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies with uv**:
```bash
pip install uv
uv pip install -e ".[dev]"
uv pip install pydantic-settings
```

3. **Set up environment variables**:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Quick Start

1. **Run the service**:
```bash
python -m app.main
```

2. **Access the API**:
- API Documentation: http://localhost:8000/api/v1/docs
- Health Check: http://localhost:8000/api/v1/health

3. **Test browser automation**:
```bash
python test_browser.py
```

## API Endpoints

### Agents
- `POST /api/v1/agents` - Create new agent
- `GET /api/v1/agents` - List agents
- `GET /api/v1/agents/{agent_id}` - Get agent details
- `PUT /api/v1/agents/{agent_id}` - Update agent
- `DELETE /api/v1/agents/{agent_id}` - Delete agent

### Workflows
- `POST /api/v1/agents/{agent_id}/workflows` - Create workflow
- `GET /api/v1/agents/{agent_id}/workflows` - List workflows

### Execution
- `POST /api/v1/agents/{agent_id}/execute` - Execute agent
- `GET /api/v1/executions/{execution_id}` - Get execution details

### Testing
- `POST /api/v1/test-action` - Test single browser action

## Development

### Project Structure
```
service/
├── app/
│   ├── api/          # API routes and endpoints
│   ├── core/         # Core functionality (config, browser engine)
│   ├── models/       # Database models
│   ├── schemas/      # Pydantic schemas
│   ├── services/     # Business logic services
│   ├── utils/        # Utility functions
│   └── workers/      # Background task workers
├── tests/            # Test files
├── logs/             # Application logs
├── screenshots/      # Browser screenshots
├── downloads/        # Downloaded files
└── workspace/        # File access workspace
```

### Running Tests
```bash
pytest
```

### Code Quality
```bash
# Format code
black app tests

# Lint code
ruff app tests

# Type checking
mypy app
```

## Configuration

Key configuration options in `.env`:

- `BROWSER_HEADLESS`: Run browser in headless mode
- `FILE_ACCESS_BASE_DIR`: Base directory for file operations
- `DATABASE_URL`: Database connection string
- `REDIS_URL`: Redis connection for caching and queuing

## Security

- File access is restricted to allowed directories
- Granular permissions system for file operations
- JWT authentication for API access
- Rate limiting on API endpoints

## License

MIT