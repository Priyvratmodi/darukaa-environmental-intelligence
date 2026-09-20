import React from 'react';
import type { EvidenceBackedRecommendation } from '@/types/api';
import { Badge } from '@/components/ui/Badge';

interface RecommendationCardProps {
  recommendation: EvidenceBackedRecommendation;
}

export function RecommendationCard({ recommendation }: RecommendationCardProps) {
  const {
    recommendation: title,
    why_it_works,
    impacted_metrics,
    expected_time_horizon,
    confidence,
  } = recommendation;

  return (
    <div className="flex flex-col rounded-2xl border border-emerald-100 bg-white shadow-sm transition-shadow hover:shadow-md">
      <div className="border-b border-stone-50 bg-emerald-50/40 p-6">
        <div className="flex flex-wrap items-start justify-between gap-4">
          <h4 className="flex-1 text-[17px] font-bold text-stone-900 leading-snug">
            {title}
          </h4>
          <div className="flex shrink-0 items-center gap-2.5">
            {expected_time_horizon && (
              <Badge className="bg-white text-stone-600 shadow-sm ring-1 ring-inset ring-stone-200">
                {expected_time_horizon}
              </Badge>
            )}
            {confidence && (
              <Badge
                className={
                  confidence === 'High'
                    ? 'bg-emerald-100 text-emerald-800 ring-1 ring-inset ring-emerald-200 shadow-sm'
                    : confidence === 'Medium'
                    ? 'bg-blue-100 text-blue-800 ring-1 ring-inset ring-blue-200 shadow-sm'
                    : 'bg-stone-100 text-stone-800 ring-1 ring-inset ring-stone-200 shadow-sm'
                }
              >
                {confidence} Confidence
              </Badge>
            )}
          </div>
        </div>
      </div>

      <div className="p-6">
        <div className="mb-5 space-y-2">
          <h5 className="text-[11px] font-bold uppercase tracking-widest text-stone-400">
            Mechanism / Reason
          </h5>
          <p className="text-[15px] leading-relaxed text-stone-700 whitespace-pre-wrap font-medium">
            {why_it_works}
          </p>
        </div>

        {impacted_metrics && impacted_metrics.length > 0 && (
          <div className="space-y-3 pt-4 border-t border-stone-100/80">
            <h5 className="text-[11px] font-bold uppercase tracking-widest text-stone-400">
              Impacted Metrics
            </h5>
            <div className="flex flex-wrap items-center gap-2">
              {impacted_metrics.map((metric) => (
                <span
                  key={metric}
                  className="inline-flex items-center rounded-md bg-stone-50 px-2.5 py-1 text-xs font-semibold text-stone-600 ring-1 ring-inset ring-stone-500/10"
                >
                  {metric}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
