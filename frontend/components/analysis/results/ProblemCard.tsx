import type { ProblemUnderstanding } from '@/types/api';
import { Card } from '@/components/ui/Card';
import { Badge } from '@/components/ui/Badge';
import { DOMAIN_LABELS } from '@/lib/constants';

interface Props {
  data: ProblemUnderstanding;
}

const ROW = ({ label, value }: { label: string; value: string | null }) =>
  value ? (
    <div className="flex flex-col gap-1 sm:flex-row sm:gap-3">
      <dt className="w-36 shrink-0 text-xs font-bold text-stone-400 uppercase tracking-wider">
        {label}
      </dt>
      <dd className="text-sm font-medium text-stone-700">{value}</dd>
    </div>
  ) : null;

export function ProblemCard({ data }: Props) {
  return (
    <Card title="Problem Understanding">
      <div className="space-y-5">
        {/* Domain */}
        <div className="flex items-center gap-2">
          <Badge className="bg-emerald-50 text-emerald-800 border-emerald-200 shadow-sm">
            {DOMAIN_LABELS[data.domain] ?? data.domain}
          </Badge>
        </div>

        {/* Problem statement */}
        <p className="text-lg leading-relaxed text-stone-900 font-semibold">
          {data.problem_statement}
        </p>

        {/* Key fields */}
        <dl className="space-y-3 pt-3 border-t border-stone-100">
          <ROW label="Affected entity" value={data.affected_entity} />
          <ROW label="Location" value={data.location} />
          <ROW label="Ecosystem" value={data.ecosystem_context} />
          <ROW label="Suspected outcome" value={data.suspected_outcome} />
        </dl>
      </div>
    </Card>
  );
}
