/**
 * Generates a new UUID-based session ID.
 * Uses the native Web Crypto API — no extra dependency required (Node 19+, all modern browsers).
 */
export function generateSessionId(): string {
  if (typeof crypto !== 'undefined' && crypto.randomUUID) {
    return crypto.randomUUID();
  }
  // Fallback for older environments
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    const v = c === 'x' ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

/**
 * Retrieves a persisted session ID from localStorage, or creates a new one.
 * Returns a fallback for server-side rendering environments.
 */
export function getOrCreateSessionId(): string {
  if (typeof window === 'undefined') return 'ssr-placeholder';
  const key = 'darukaa_session_id';
  const existing = localStorage.getItem(key);
  if (existing) return existing;
  const newId = generateSessionId();
  localStorage.setItem(key, newId);
  return newId;
}

/**
 * Resets the session ID in localStorage (starts a new conversation).
 */
export function resetSession(): string {
  const key = 'darukaa_session_id';
  const newId = generateSessionId();
  if (typeof window !== 'undefined') {
    localStorage.setItem(key, newId);
  }
  return newId;
}
