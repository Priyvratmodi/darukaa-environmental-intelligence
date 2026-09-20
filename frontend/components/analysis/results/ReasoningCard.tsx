import type { MultiMetricReasoning } from '@/types/api';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { EVIDENCE_STRENGTH_CLASSES } from '@/lib/constants';

interface Props {
  data: MultiMetricReasoning;
}

export function ReasoningCard({ data }: Props) {
  return (
    <Card title="Multi-Metric Reasoning">
      <div className="space-y-6">
        {/* Relationships overview */}
        <div className="space-y-1.5">
          <p className="text-xs font-semibold uppercase tracking-widest text-gray-400">
            Relationships identified
          </p>
          <p className="text-sm leading-relaxed text-gray-700">
            {data.relationships_identified}
          </p>
        </div>

        {/* Divider */}
        {data.candidate_drivers.length > 0 && (
          <hr className="border-gray-100" />
        )}

        {/* Drivers */}
        {data.candidate_drivers.length > 0 && (
          <div className="space-y-4">
            <p className="text-xs font-semibold uppercase tracking-widest text-gray-400">
              Candidate drivers
            </p>
            <ol className="space-y-4">
              {data.candidate_drivers.map((driver, idx) => (
                <li
                  key={idx}
                  className="rounded-lg border border-gray-100 bg-gray-50 p-4 space-y-3"
                >
                  {/* Driver header */}
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-sm font-semibold text-gray-900">
                      {driver.driver}
                    </span>
                    {driver.is_primary && (
                      <Badge className="bg-green-50 text-green-800 border-green-200">
                        Primary
                      </Badge>
                    )}
                    <Badge
                      className={
                        EVIDENCE_STRENGTH_CLASSES[driver.evidence_strength] ??
                        'bg-gray-100 text-gray-600 border-gray-200'
                      }
                    >
                      {driver.evidence_strength}
                    </Badge>
                  </div>

                  {/* Explained metrics */}
                  {driver.explained_metrics.length > 0 && (
                    <div className="flex flex-wrap gap-1.5">
                      {driver.explained_metrics.map((m) => (
                        <Badge
                          key={m}
                          className="bg-white text-gray-600 border-gray-200"
                        >
                          {m}
                        </Badge>
                      ))}
                    </div>
                  )}

                  {/* Reasoning text */}
                  <p className="text-xs leading-relaxed text-gray-600">
                    {driver.reasoning}
                  </p>
                </li>
              ))}
            </ol>
          </div>
        )}
      </div>
    </Card>
  );
}
