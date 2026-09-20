import type { EvidenceChain } from '@/types/api';
import { Card } from '@/components/ui/Card';

interface Props {
  data: EvidenceChain;
}

const STEPS: Array<{ key: keyof EvidenceChain; label: string; icon: string }> = [
  { key: 'Problem', label: 'Problem', icon: '⚡' },
  { key: 'Required metrics', label: 'Required metrics', icon: '📐' },
  { key: 'Observations', label: 'Observations', icon: '🔬' },
  { key: 'Candidate driver', label: 'Candidate drivers', icon: '🧩' },
  { key: 'Causal relationship', label: 'Causal relationship', icon: '🔗' },
  { key: 'Scientific source', label: 'Scientific sources', icon: '📚' },
  { key: 'Recommendation', label: 'Recommendations', icon: '✅' },
];

function StepValue({ value }: { value: string | string[] }) {
  if (typeof value === 'string') {
    return <p className="text-sm leading-relaxed text-gray-700">{value}</p>;
  }
  return (
    <ul className="space-y-1">
      {value.map((v, i) => (
        <li key={i} className="flex items-start gap-2 text-sm text-gray-700">
          <span className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-green-500" />
          {v}
        </li>
      ))}
    </ul>
  );
}

export function EvidenceChainCard({ data }: Props) {
  return (
    <Card title="Evidence Chain">
      <ol className="relative space-y-0">
        {STEPS.map((step, idx) => {
          const value = data[step.key];
          const isEmpty =
            value === null ||
            value === undefined ||
            (Array.isArray(value) && value.length === 0) ||
            value === '';

          return (
            <li key={step.key} className="relative flex gap-4">
              {/* Connector line */}
              {idx < STEPS.length - 1 && (
                <span
                  className="absolute left-4 top-8 bottom-0 w-px bg-gray-100"
                  aria-hidden="true"
                />
              )}

              {/* Step icon */}
              <div className="relative flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-gray-200 bg-white text-sm shadow-sm">
                {step.icon}
              </div>

              {/* Content */}
              <div className="flex-1 pb-6">
                <p className="mb-1.5 text-xs font-semibold uppercase tracking-widest text-gray-400">
                  {step.label}
                </p>
                {isEmpty ? (
                  <p className="text-sm italic text-gray-300">—</p>
                ) : (
                  <StepValue value={value} />
                )}
              </div>
            </li>
          );
        })}
      </ol>
    </Card>
  );
}
