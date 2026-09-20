import { NextResponse } from 'next/server';

const BACKEND = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000';

export async function GET() {
  try {
    const upstream = await fetch(`${BACKEND}/health`, { cache: 'no-store' });
    const data: unknown = await upstream.json();
    return NextResponse.json(data, { status: upstream.status });
  } catch {
    return NextResponse.json(
      { detail: `Backend unreachable at ${BACKEND}` },
      { status: 503 },
    );
  }
}
