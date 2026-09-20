import React from 'react';
import type { ScientificEvidenceDetail } from '@/types/api';

interface EvidenceCardProps {
  evidence: ScientificEvidenceDetail;
}

export function EvidenceCard({ evidence }: EvidenceCardProps) {
  const { source, url, claims } = evidence;

  // Since the backend doesn't differentiate between 'source title' and 'source organization',
  // we map the provided 'source' to the main title/organization display.
  return (
    <div className="flex flex-col overflow-hidden rounded-2xl border border-stone-200/80 bg-white shadow-sm transition-shadow hover:shadow-md">
      <div className="flex flex-wrap items-center justify-between gap-4 border-b border-stone-100 bg-stone-50/50 px-6 py-4">
        <h4 className="text-[15px] font-bold text-stone-800 leading-tight">
          {source}
        </h4>
        {url && (
          <a
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-600 hover:text-emerald-800 hover:underline shrink-0"
            aria-label={`View source from ${source}`}
          >
            View Source
            <svg
              className="h-3 w-3"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2.5}
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
          </a>
        )}
      </div>

      <div className="px-6 py-5">
        {claims && claims.length > 0 ? (
          <div className="space-y-3">
            <h5 className="text-[11px] font-bold uppercase tracking-widest text-stone-400">
              Evidence Summary
            </h5>
            <ul className="space-y-2.5">
              {claims.map((claim, idx) => (
                <li key={idx} className="flex items-start gap-3 text-[14px]">
                  <span
                    className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-emerald-400"
                    aria-hidden="true"
                  />
                  <span className="leading-relaxed font-medium text-stone-700">{claim}</span>
                </li>
              ))}
            </ul>
          </div>
        ) : (
          <p className="text-sm italic font-medium text-stone-400">
            No specific claims provided.
          </p>
        )}
      </div>
    </div>
  );
}
