import { MetricCard } from '@/components/analysis/results/MetricCard';
import type { AnalysisResponse } from '@/types/api';

interface MetricsSectionProps {
  result: AnalysisResponse;
}

// Utility to attempt extracting a metric name and value from a free-text observation string.
// Example: "soil pH: 5.2" -> name: "soil pH", value: "5.2"
// Example: "Soil organic carbon is 0.5%" -> name: "Soil organic carbon", value: "0.5%"
function parseObservation(obs: string): { name: string; value?: string } {
  // Try colon split
  if (obs.includes(':')) {
    const [name, ...rest] = obs.split(':');
    return { name: name.trim(), value: rest.join(':').trim() };
  }
  
  // Try " is " split
  if (obs.toLowerCase().includes(' is ')) {
    const match = obs.match(/^(.*?)\s+is\s+(.*)$/i);
    if (match) {
      return { name: match[1].trim(), value: match[2].trim() };
    }
  }

  // Try " has decreased by " or similar
  if (obs.toLowerCase().includes(' has ')) {
    const match = obs.match(/^(.*?)\s+has\s+(.*)$/i);
    if (match) {
      return { name: match[1].trim(), value: `has ${match[2].trim()}` };
    }
  }

  // Fallback: just use the whole string as the name, no specific value
  return { name: obs.trim() };
}

export function MetricsSection({ result }: MetricsSectionProps) {
  const isMissing = result.status === 'requires_more_info';

  if (isMissing) {
    return (
      <div className="space-y-4">
        <h3 className="text-sm font-semibold tracking-wide text-gray-900 uppercase">
          Required Metrics
        </h3>
        <p className="text-sm text-gray-600">
          The following environmental metrics are required to complete the analysis.
        </p>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {result.missing_metrics.map((metric, idx) => (
            <MetricCard
              key={`${metric.metric_name}-${idx}`}
              name={metric.metric_name}
              status="missing"
              description={metric.why_it_matters}
              unit={metric.expected_unit}
            />
          ))}
        </div>
      </div>
    );
  }

  // For complete status, display the observed values and mentioned factors
  const observations = result.problem_understanding.observed_values || [];
  const factors = result.problem_understanding.mentioned_factors || [];

  if (observations.length === 0 && factors.length === 0) {
    return null; // Don't render the section if there are absolutely no metrics
  }

  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold tracking-wide text-gray-900 uppercase">
        Extracted Environmental Metrics
      </h3>
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {/* Render explicit observations (usually have values) */}
        {observations.map((obs, idx) => {
          const { name, value } = parseObservation(obs);
          return (
            <MetricCard
              key={`obs-${idx}`}
              name={name}
              value={value}
              status="provided"
            />
          );
        })}

        {/* Render mentioned factors (usually lack explicit values) */}
        {factors.map((factor, idx) => (
          <MetricCard
            key={`factor-${idx}`}
            name={factor}
            status="provided"
            description="Mentioned as a relevant factor, but no specific value was provided."
          />
        ))}
      </div>
    </div>
  );
}
