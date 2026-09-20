import type { MissingMetric } from '@/types/api';
import { Card } from '@/components/ui/Card';

interface Props {
  message: string;
  metrics: MissingMetric[];
}

export function MissingMetricsCard({ message, metrics }: Props) {
  return (
    <Card title="Additional Information Required">
      <div className="space-y-4">
        <p className="text-sm leading-relaxed text-gray-600">{message}</p>

        {metrics.length > 0 && (
          <div className="space-y-2">
            <p className="text-xs font-semibold uppercase tracking-widest text-gray-400">
              Please provide the following metrics
            </p>
            <ul className="divide-y divide-gray-100 rounded-lg border border-gray-100 overflow-hidden">
              {metrics.map((m, idx) => (
                <li
                  key={idx}
                  className="flex flex-col gap-0.5 bg-amber-50/50 px-4 py-3"
                >
                  <div className="flex items-center justify-between gap-4">
                    <span className="text-sm font-medium text-gray-800">
                      {m.metric_name}
                    </span>
                    <span className="shrink-0 rounded-full border border-amber-200 bg-amber-50 px-2 py-0.5 font-mono text-xs text-amber-700">
                      {m.expected_unit}
                    </span>
                  </div>
                  <p className="text-xs leading-relaxed text-gray-500">
                    {m.why_it_matters}
                  </p>
                </li>
              ))}
            </ul>
          </div>
        )}

        <p className="text-xs text-gray-400">
          Add these values to your description and submit again to continue the
          analysis.
        </p>
      </div>
    </Card>
  );
}
