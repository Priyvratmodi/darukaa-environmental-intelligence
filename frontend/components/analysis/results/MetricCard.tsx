import React from 'react';

interface MetricCardProps {
  name: string;
  value?: string;
  status: 'provided' | 'missing';
  description?: string;
  unit?: string;
}

export function MetricCard({
  name,
  value,
  status,
  description,
  unit,
}: MetricCardProps) {
  const isMissing = status === 'missing';

  return (
    <div
      className={`relative flex flex-col rounded-2xl border p-5 shadow-sm transition-shadow hover:shadow-md ${
        isMissing
          ? 'border-amber-200/80 bg-amber-50/50'
          : 'border-emerald-100 bg-white'
      }`}
    >
      <div className="flex items-start justify-between gap-3 mb-4">
        <h4
          className={`text-[15px] font-bold capitalize ${
            isMissing ? 'text-amber-900' : 'text-stone-800'
          }`}
        >
          {name}
        </h4>
        <span
          className={`inline-flex shrink-0 items-center rounded-full px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-widest ${
            isMissing
              ? 'bg-amber-100 text-amber-800'
              : 'bg-emerald-100 text-emerald-800'
          }`}
        >
          {status}
        </span>
      </div>

      <div className="flex-1 space-y-3">
        {value ? (
          <div className="flex items-baseline gap-1.5">
            <span className="text-3xl font-extrabold tracking-tight text-stone-900">
              {value}
            </span>
            {unit && (
              <span className="text-sm font-semibold text-stone-500 uppercase tracking-wide">{unit}</span>
            )}
          </div>
        ) : (
          <span className="inline-block text-sm font-medium italic text-stone-400">
            {isMissing ? 'Measurement required' : 'No exact value provided'}
          </span>
        )}

        {description && (
          <p
            className={`text-sm leading-relaxed ${
              isMissing ? 'text-amber-800/80' : 'text-stone-600'
            }`}
          >
            {description}
          </p>
        )}

        {isMissing && unit && !value && (
          <div className="pt-2 border-t border-amber-200/50">
             <p className="text-[11px] font-bold uppercase tracking-wider text-amber-700">
               Expected unit: {unit}
             </p>
          </div>
        )}
      </div>
    </div>
  );
}
