# Darukaa Frontend

Next.js 15 frontend for the **Darukaa Environmental Intelligence** platform.

## Tech Stack

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS v4
- **Backend**: FastAPI at `http://localhost:8000`

## Project Structure

```
frontend/
├── app/
│   ├── globals.css        # Tailwind CSS entry point
│   ├── layout.tsx         # Root layout with metadata
│   └── page.tsx           # Home page (placeholder)
├── components/
│   └── ui/
│       ├── Badge.tsx      # Inline status pill
│       ├── Card.tsx       # Card wrapper
│       └── Spinner.tsx    # Loading indicator
├── lib/
│   ├── api.ts             # Typed API client (health, analyze, session)
│   ├── constants.ts       # Domain labels and badge classes
│   └── session.ts         # Session ID generation & persistence
├── types/
│   └── api.ts             # TypeScript types mirroring all backend schemas
├── public/                # Static assets
├── next.config.ts         # Next.js config with API rewrites
├── tsconfig.json          # TypeScript config
└── package.json
```

## API Contract

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Liveness check |
| `/analyze` | POST | Run analysis pipeline |
| `/session/:id` | GET | Fetch session state |

### POST /analyze

**Request:**
```json
{ "session_id": "string", "query": "string" }
```

**Response (complete):**
```json
{
  "status": "complete",
  "session_id": "...",
  "problem_understanding": { ... },
  "evidence_chain": { ... },
  "reasoning": { "candidate_drivers": [...] },
  "recommendations": { "recommendations": [...] }
}
```

**Response (requires more info):**
```json
{
  "status": "requires_more_info",
  "session_id": "...",
  "missing_metrics": [...],
  "message": "Additional environmental metrics are required to proceed."
}
```

## Getting Started

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

Make sure the FastAPI backend is running on port 8000.
