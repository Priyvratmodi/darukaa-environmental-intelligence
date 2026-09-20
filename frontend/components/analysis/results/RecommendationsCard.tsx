import type { RecommendationPlan } from '@/types/api';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { CONFIDENCE_CLASSES } from '@/lib/constants';

interface Props {
  data: RecommendationPlan;
}

export function RecommendationsCard({ data }: Props) {
  return (
    <Card title="Recommendations">
      <ol className="space-y-6">
        {data.recommendations.map((rec, idx) => (
          <li key={idx} className="space-y-3">
            {idx > 0 && <hr className="border-gray-100" />}

            {/* Number + recommendation */}
            <div className="flex items-start gap-3">
              <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-green-800 text-xs font-bold text-white">
                {idx + 1}
              </span>
              <p className="text-sm font-semibold leading-snug text-gray-900">
                {rec.recommendation}
              </p>
            </div>

            {/* Why it works */}
            <p className="pl-9 text-sm leading-relaxed text-gray-600">
              {rec.why_it_works}
            </p>

            {/* Metadata row */}
            <div className="pl-9 flex flex-wrap items-center gap-3">
              {/* Confidence */}
              <Badge
                className={
                  CONFIDENCE_CLASSES[rec.confidence] ??
                  'bg-gray-100 text-gray-600 border-gray-200'
                }
              >
                {rec.confidence} confidence
              </Badge>

              {/* Time horizon */}
              <span className="text-xs text-gray-400">
                ⏱ {rec.expected_time_horizon}
              </span>
            </div>

            {/* Impacted metrics */}
            {rec.impacted_metrics.length > 0 && (
              <div className="pl-9 flex flex-wrap gap-1.5">
                {rec.impacted_metrics.map((m) => (
                  <Badge
                    key={m}
                    className="bg-green-50 text-green-800 border-green-200"
                  >
                    {m}
                  </Badge>
                ))}
              </div>
            )}

            {/* Scientific evidence */}
            {rec.scientific_evidence.length > 0 && (
              <div className="pl-9 space-y-1.5">
                <p className="text-xs font-medium text-gray-400 uppercase tracking-wide">
                  Evidence
                </p>
                <ul className="space-y-1">
                  {rec.scientific_evidence.map((ev, ei) => (
                    <li key={ei} className="text-xs text-gray-500">
                      <span className="font-medium text-gray-700">
                        {ev.source}
                      </span>
                      {ev.url && (
                        <>
                          {' '}
                          &mdash;{' '}
                          <a
                            href={ev.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="underline underline-offset-2 text-green-700 hover:text-green-900"
                          >
                            source ↗
                          </a>
                        </>
                      )}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </li>
        ))}
      </ol>
    </Card>
  );
}
