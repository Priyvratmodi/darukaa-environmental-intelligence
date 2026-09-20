import type { AnalysisResponse } from '@/types/api';
import { ProblemCard } from '@/components/analysis/results/ProblemCard';
import { MetricsSection } from '@/components/analysis/results/MetricsSection';
import { ReasoningVisualization } from '@/components/analysis/results/ReasoningVisualization';

interface ResultsPanelProps {
  result: AnalysisResponse;
}

export function ResultsPanel({ result }: ResultsPanelProps) {
  // ── requires_more_info ─────────────────────────────────────────────────────
  if (result.status === 'requires_more_info') {
    return (
      <section
        className="space-y-6 border-t border-gray-100 pt-8"
        role="region"
        aria-label="Analysis results"
      >
        <SectionHeader
          label="Analysis paused"
          sessionId={result.session_id}
        />
        
        <div className="rounded-xl border border-amber-200 bg-amber-50 p-4">
          <p className="text-sm font-medium text-amber-900">
            {result.message}
          </p>
        </div>

        <MetricsSection result={result} />
      </section>
    );
  }

  // ── complete ───────────────────────────────────────────────────────────────
  return (
    <section
      className="space-y-12 border-t border-gray-100 pt-8"
      role="region"
      aria-label="Analysis results"
    >
      <div className="space-y-8">
        <SectionHeader label="Analysis complete" sessionId={result.session_id} />
        
        <ProblemCard data={result.problem_understanding} />
        
        <MetricsSection result={result} />
      </div>

      <div className="border-t border-gray-100 pt-8">
        <h2 className="mb-6 text-2xl font-semibold tracking-tight text-gray-900">
          Environmental Reasoning
        </h2>
        <ReasoningVisualization data={result} />
      </div>
    </section>
  );
}

// ── Internal header ──────────────────────────────────────────────────────────

function SectionHeader({
  label,
  sessionId,
}: {
  label: string;
  sessionId: string;
}) {
  return (
    <div className="flex items-center justify-between">
      <p className="flex items-center gap-2 text-xs font-semibold uppercase tracking-widest text-gray-400">
        <span className="h-1.5 w-1.5 rounded-full bg-green-500" />
        {label}
      </p>
      <p className="font-mono text-xs text-gray-300" title="Session ID">
        {sessionId.slice(0, 8)}&hellip;
      </p>
    </div>
  );
}
