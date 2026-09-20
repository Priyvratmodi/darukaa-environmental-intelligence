import type {
  AnalysisRequest,
  AnalysisResponse,
  ApiErrorPayload,
  HealthResponse,
} from '@/types/api';

// ─── Error class ───────────────────────────────────────────────────────────────

export class ApiError extends Error {
  constructor(
    public readonly status: number,
    message: string,
  ) {
    super(message);
    this.name = 'ApiError';
  }
}

// ─── Internal helper ───────────────────────────────────────────────────────────

async function fetchJSON<T>(endpoint: string, options?: RequestInit): Promise<T> {
  let res: Response;

  // We use the /api prefix which is rewritten by next.config.ts to the 
  // NEXT_PUBLIC_API_URL backend to avoid CORS issues.
  const url = `/api${endpoint}`;

  try {
    res = await fetch(url, {
      headers: { 'Content-Type': 'application/json' },
      ...options,
    });
  } catch {
    // Network failure — backend unreachable
    throw new ApiError(
      0,
      `Cannot reach the backend. Make sure the server is running and try again.`,
    );
  }

  if (!res.ok) {
    let detail = `HTTP ${res.status}`;
    try {
      const payload = (await res.json()) as ApiErrorPayload;
      detail = payload.detail ?? detail;
    } catch {
      // ignore — use status text
    }
    throw new ApiError(res.status, detail);
  }

  return res.json() as Promise<T>;
}

// ─── Public API ────────────────────────────────────────────────────────────────

/**
 * GET /health
 * Liveness check — call this to verify the backend is reachable.
 */
export async function checkHealth(): Promise<HealthResponse> {
  return fetchJSON<HealthResponse>('/health');
}

/**
 * POST /analyze
 * Run the full Darukaa analysis pipeline.
 *
 * Returns either:
 *  - AnalysisResponseComplete   when status === 'complete'
 *  - AnalysisResponseRequiresInfo  when status === 'requires_more_info'
 *
 * Throws ApiError on any HTTP or network failure.
 */
export async function runAnalysis(
  request: AnalysisRequest,
): Promise<AnalysisResponse> {
  return fetchJSON<AnalysisResponse>('/analyze', {
    method: 'POST',
    body: JSON.stringify(request),
  });
}
