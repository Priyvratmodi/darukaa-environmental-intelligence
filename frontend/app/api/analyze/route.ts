import { NextRequest, NextResponse } from 'next/server';

/**
 * Server-side proxy for POST /analyze.
 * Reads NEXT_PUBLIC_API_URL on the server — no CORS issues for the browser.
 */
const BACKEND = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    const upstream = await fetch(`${BACKEND}/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      // Prevent Next.js from caching analysis responses
      cache: 'no-store',
    });

    const data: unknown = await upstream.json();
    return NextResponse.json(data, { status: upstream.status });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : 'Unknown error';
    return NextResponse.json(
      { detail: `Backend unreachable at ${BACKEND}: ${message}` },
      { status: 503 },
    );
  }
}
