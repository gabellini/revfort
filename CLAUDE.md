# Rev Fort - Chargeback Dispute Automation System

## Project Overview

**Rev Fort** is a SaaS platform that automates chargeback dispute processes. The system connects to payment providers, e-commerce platforms, and customer service tools to automatically detect chargebacks, gather evidence, generate optimized disputes following card brand best practices, submit them, and monitor outcomes.

## Core Rules

- **All code MUST be written in English** (function names, variables, classes, comments, commit messages)
- User-facing text (UI labels, messages) should be in Portuguese (pt-BR) by default with i18n support
- Follow clean code principles: small functions, clear naming, single responsibility

## Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| API         | Python 3.12+ / FastAPI         |
| Database    | PostgreSQL + Redis (cache/queue) |
| ORM         | SQLAlchemy 2.0 + Alembic       |
| Task Queue  | Celery + Redis                 |
| Website     | Node.js / Next.js / TypeScript |
| Web App     | Node.js / Next.js / TypeScript |
| Monorepo    | pnpm workspaces                |
| Containers  | Docker + Docker Compose        |

## Architecture

### Monorepo Structure

```
revfort/
├── api/              # Python FastAPI backend
├── apps/
│   ├── website/      # Commercial/marketing website (Next.js)
│   └── web-app/      # SaaS application (Next.js)
├── packages/
│   └── shared-types/ # Shared TypeScript types between frontends
├── docker/           # Dockerfiles per service
├── docs/             # Project documentation
└── scripts/          # Dev/ops utility scripts
```

### API Structure (`api/app/`)

```
app/
├── core/             # Config, security, exceptions, logging
├── db/models/        # SQLAlchemy models
├── connectors/       # External service integrations
│   ├── payment/      # Pagar.me, Cielo, Rede, PayPal
│   ├── ecommerce/    # VTEX, Betalabs, Tray, Shopify
│   ├── customer_service/  # Zendesk
│   └── card_brands/  # Visa, Mastercard (direct monitoring APIs)
├── services/         # Business logic layer
├── schemas/          # Pydantic request/response schemas
├── api/v1/           # API route handlers
└── workers/          # Celery async tasks
```

## Core Features

### 1. Chargeback Detection & Monitoring
- Polls payment providers for new chargebacks
- Active monitoring via Visa and Mastercard APIs (VROL/Mastercom)
- Real-time webhook support where available

### 2. Evidence Collection
- Fetches order details from e-commerce platform (products, delivery, customer info)
- Retrieves customer service history from Zendesk
- Cross-references all data to build a complete dispute case

### 3. Automated Dispute Generation
- Analyzes chargeback reason code and card brand rules
- Considers: merchant segment, seller profile, product type, chargeback type
- Generates dispute following card brand best practices (Visa CE 3.0, Mastercard Dispute Resolution)
- Assembles evidence package with proper documentation

### 4. Dispute Submission & Monitoring
- Submits dispute through payment provider or directly to card brand
- Tracks dispute lifecycle (submitted → under review → won/lost)
- Reports win rates and analytics

### 5. Recommendation Engine
- Connects to client's e-commerce platform
- Analyzes incoming sales against collective intelligence from all Rev Fort data
- Generates proactive recommendations to prevent chargebacks
- Risk scoring for transactions

## Connectors

### Payment Providers
| Provider  | Priority | API Type   |
|-----------|----------|------------|
| Pagar.me  | High     | REST       |
| Cielo     | High     | REST       |
| Rede      | High     | REST       |
| PayPal    | Medium   | REST       |

### E-commerce Platforms
| Platform  | Priority | API Type   |
|-----------|----------|------------|
| VTEX      | High     | REST       |
| Betalabs  | High     | REST       |
| Tray      | Medium   | REST       |
| Shopify   | Medium   | REST/GraphQL |

### Customer Service
| Platform  | Priority | API Type   |
|-----------|----------|------------|
| Zendesk   | High     | REST       |

### Card Brands (Direct Monitoring)
| Brand      | API               |
|------------|-------------------|
| Visa       | VROL / Visa Resolve Online |
| Mastercard | Mastercom API     |

## Coding Conventions

### Python (API)
- Use `snake_case` for functions and variables
- Use `PascalCase` for classes
- Type hints required on all function signatures
- Async/await for all I/O operations
- All connectors must implement the corresponding base class interface
- Use Pydantic for all data validation
- Tests: pytest with async support

### TypeScript (Frontends)
- Use `camelCase` for functions and variables
- Use `PascalCase` for components and types
- Strict TypeScript (`strict: true`)
- React Server Components where appropriate
- Tailwind CSS for styling

### Git
- Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`
- Branch naming: `feat/description`, `fix/description`, `refactor/description`
- **Do NOT add Co-Authored-By or any co-author trailers to commits** (breaks Vercel deploy)

## Environment Variables

All secrets and configuration go in `.env` files (never committed). See `.env.example` for required variables.

## Key Domain Concepts

- **Merchant**: A Rev Fort customer (the online store)
- **Chargeback**: A disputed transaction initiated by a cardholder
- **Dispute**: Rev Fort's response/contestation to a chargeback
- **Connector**: Integration module for an external service
- **Evidence Package**: Collection of documents/data supporting a dispute
- **Reason Code**: Card brand code classifying the chargeback type
