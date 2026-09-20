import React from 'react';
import type {
  AnalysisResponseComplete,
  DriverAnalysis,
} from '@/types/api';
import { Badge } from '@/components/ui/Badge';
import { RecommendationCard } from '@/components/analysis/results/RecommendationCard';
import { EvidenceCard } from '@/components/analysis/results/EvidenceCard';

// ─── Main Orchestrator ────────────────────────────────────────────────────────

export function ReasoningVisualization({
  data,
}: {
  data: AnalysisResponseComplete;
}) {
  // Extract and sanitize data from the backend response
  const observations = data.evidence_chain?.Observations || [];
  const relationships = data.reasoning?.relationships_identified || '';
  const drivers = data.reasoning?.candidate_drivers || [];
  const evidenceScope = data.evidence_scope;
  
  // Flatten and deduplicate scientific evidence
  const rawEvidence =
    data.recommendations?.recommendations?.flatMap(
      (r) => r.scientific_evidence
    ) || [];
  const uniqueEvidence = Array.from(
    new Map(rawEvidence.map((item) => [item.url || item.source, item])).values()
  );

  const recommendations = data.recommendations?.recommendations || [];

  // Build the pipeline steps dynamically, omitting any missing sections
  const steps = [];

  if (observations.length > 0) {
    steps.push({
      title: 'Observations',
      content: <ObservationsView data={observations} />,
    });
  }

  if (relationships) {
    steps.push({
      title: 'Environmental Relationships',
      content: <RelationshipsView text={relationships} />,
    });
  }

  if (drivers.length > 0) {
    steps.push({
      title: 'Candidate Drivers',
      content: <DriversView drivers={drivers} />,
    });
  }

  // Handle evidence scope
  if (evidenceScope === 'provided_data_only') {
    steps.push({
      title: 'Scientific Evidence',
      content: (
        <div className="rounded-2xl border border-amber-200/60 bg-amber-50/50 p-5 shadow-sm">
          <p className="text-sm font-medium text-amber-900 flex items-center gap-2">
            <svg className="h-4 w-4 text-amber-600" viewBox="0 0 20 20" fill="currentColor">
               <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clipRule="evenodd" />
            </svg>
            Analysis based only on the information you provided.
          </p>
        </div>
      ),
    });
  } else if (uniqueEvidence.length > 0) {
    steps.push({
      title: 'Scientific Evidence',
      content: (
        <div className="space-y-4">
          {uniqueEvidence.map((evidence, i) => (
            <EvidenceCard key={i} evidence={evidence} />
          ))}
        </div>
      ),
    });
  }

  if (recommendations.length > 0) {
    steps.push({
      title: 'Recommendations',
      content: (
        <div className="space-y-5">
          {recommendations.map((rec, i) => (
            <RecommendationCard key={i} recommendation={rec} />
          ))}
        </div>
      ),
    });
  }

  if (steps.length === 0) return null;

  return (
    <div className="mx-auto max-w-4xl py-6">
      <div className="space-y-0">
        {steps.map((step, index) => (
          <FlowStep
            key={step.title}
            stepNumber={index + 1}
            title={step.title}
            isLast={index === steps.length - 1}
          >
            {step.content}
          </FlowStep>
        ))}
      </div>
    </div>
  );
}

// ─── Reusable Layout Component ────────────────────────────────────────────────

function FlowStep({
  stepNumber,
  title,
  children,
  isLast,
}: {
  stepNumber: number;
  title: string;
  children: React.ReactNode;
  isLast: boolean;
}) {
  return (
    <div className="relative flex gap-6 pb-12">
      {/* Vertical line connecting steps */}
      {!isLast && (
        <div
          className="absolute bottom-0 left-[19px] top-12 w-0.5 bg-stone-200/80 rounded-full"
          aria-hidden="true"
        />
      )}

      {/* Step Indicator */}
      <div className="relative z-10 flex h-10 w-10 shrink-0 items-center justify-center rounded-full border-[3px] border-emerald-50 bg-white shadow-sm ring-1 ring-stone-200 mt-1">
        <span className="font-mono text-[13px] font-bold text-emerald-700">
          {stepNumber}
        </span>
      </div>

      {/* Content */}
      <div className="flex-1 space-y-4 pt-2">
        <h3 className="text-xl font-bold tracking-tight text-stone-900">
          {title}
        </h3>
        <div className="text-stone-700">{children}</div>
      </div>
    </div>
  );
}

// ─── Step View Components ─────────────────────────────────────────────────────

function ObservationsView({ data }: { data: string[] }) {
  return (
    <ul className="space-y-3">
      {data.map((obs, i) => (
        <li key={i} className="flex items-start gap-3">
          <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-emerald-500/60 shadow-sm" />
          <span className="text-sm font-medium leading-relaxed text-stone-700">{obs}</span>
        </li>
      ))}
    </ul>
  );
}

function RelationshipsView({ text }: { text: string }) {
  return (
    <div className="rounded-2xl border border-sky-100/80 bg-sky-50/50 p-6 shadow-sm">
      <p className="text-[15px] font-medium leading-relaxed text-sky-900">{text}</p>
    </div>
  );
}

function DriversView({ drivers }: { drivers: DriverAnalysis[] }) {
  return (
    <div className="grid gap-5 sm:grid-cols-2">
      {drivers.map((driver, i) => (
        <div
          key={i}
          className="flex flex-col rounded-2xl border border-stone-200 bg-white p-6 shadow-sm transition-shadow hover:shadow-md"
        >
          <div className="mb-4 flex items-start justify-between gap-3">
            <h4 className="font-bold text-stone-900 capitalize text-[15px]">
              {driver.driver}
            </h4>
            {driver.is_primary && (
              <Badge className="bg-purple-50 text-purple-800 border-purple-200/60 shrink-0 shadow-sm">
                Primary
              </Badge>
            )}
          </div>

          <p className="mb-5 text-sm leading-relaxed text-stone-600 flex-1">
            {driver.reasoning}
          </p>

          <div className="space-y-4 border-t border-stone-100 pt-4">
            <div className="flex items-center justify-between gap-2 text-xs">
              <span className="font-bold text-stone-400 uppercase tracking-wider">
                Evidence
              </span>
              <span
                className={`font-bold px-2 py-0.5 rounded-md ${
                  driver.evidence_strength === 'Strong'
                    ? 'bg-emerald-50 text-emerald-700'
                    : driver.evidence_strength === 'Moderate'
                    ? 'bg-amber-50 text-amber-700'
                    : 'bg-stone-50 text-stone-500'
                }`}
              >
                {driver.evidence_strength}
              </span>
            </div>
            
            {driver.explained_metrics?.length > 0 && (
              <div className="flex flex-wrap gap-1.5 pt-1">
                {driver.explained_metrics.map((metric) => (
                  <span
                    key={metric}
                    className="inline-flex items-center rounded-md bg-stone-100/80 px-2 py-1 text-[11px] font-semibold text-stone-600 ring-1 ring-inset ring-stone-500/10"
                  >
                    {metric}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}
