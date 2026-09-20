'use client';

import { useEffect, useState } from 'react';
import { checkHealth } from '@/lib/api';

export function Header() {
  const [isBackendUp, setIsBackendUp] = useState<boolean | null>(null);

  useEffect(() => {
    // Ping health endpoint on mount
    checkHealth()
      .then((res) => setIsBackendUp(res.status === 'ok'))
      .catch(() => setIsBackendUp(false));
  }, []);

  return (
    <header className="sticky top-0 z-40 border-b border-stone-200/60 bg-white/80 backdrop-blur-md">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <svg className="h-6 w-6 text-emerald-600" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22ZM11 19.9381C7.05369 19.446 4 16.0796 4 12C4 7.92038 7.05369 4.55399 11 4.06189V19.9381ZM13 4.06189C16.9463 4.55399 20 7.92038 20 12C20 16.0796 16.9463 19.446 13 19.9381V4.06189Z"></path>
          </svg>
          <div className="flex items-baseline gap-2.5">
            <span className="text-lg font-bold tracking-tight text-stone-900">
              Darukaa
            </span>
            <span className="hidden text-[13px] font-medium tracking-wide text-stone-400 sm:inline uppercase">
              Environmental Intelligence
            </span>
          </div>
        </div>

        {/* Status area */}
        <div className="flex items-center gap-5">
          <div
            className={`flex items-center gap-2 rounded-full border px-3 py-1.5 text-xs font-medium transition-colors ${
              isBackendUp === true
                ? 'border-emerald-200/60 bg-emerald-50/50 text-emerald-700'
                : isBackendUp === false
                  ? 'border-red-200/60 bg-red-50/50 text-red-700'
                  : 'border-stone-200/60 bg-stone-50/50 text-stone-500'
            }`}
            title={
              isBackendUp === true
                ? 'Backend connected'
                : isBackendUp === false
                  ? 'Backend disconnected'
                  : 'Checking backend status...'
            }
          >
            <span
              className={`h-1.5 w-1.5 rounded-full shadow-sm ${
                isBackendUp === true
                  ? 'bg-emerald-500'
                  : isBackendUp === false
                    ? 'bg-red-500'
                    : 'bg-stone-300 animate-pulse'
              }`}
              aria-hidden="true"
            />
            <span className="hidden sm:inline">Engine</span>
            <span
              className={`font-mono font-semibold ${
                isBackendUp === true
                  ? 'text-emerald-600'
                  : isBackendUp === false
                    ? 'text-red-600'
                    : 'text-stone-400'
              }`}
            >
              Ready
            </span>
          </div>
        </div>
      </div>
    </header>
  );
}
