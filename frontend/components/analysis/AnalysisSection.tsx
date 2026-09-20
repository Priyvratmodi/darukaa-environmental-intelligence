'use client';

import { useState, useRef, useEffect } from 'react';
import { Button } from '@/components/ui/Button';
import { ResultsPanel } from '@/components/analysis/ResultsPanel';
import { runAnalysis, ApiError } from '@/lib/api';
import type { AnalysisResponse } from '@/types/api';
import { getOrCreateSessionId, resetSession } from '@/lib/session';

const DEFAULT_PLACEHOLDER =
  'Biodiversity on my farmland has declined. Soil organic carbon is 0.5%, soil moisture is low, rainfall has decreased, and native vegetation cover has decreased by 30%.';
const FOLLOWUP_PLACEHOLDER =
  'Provide the requested metrics here (e.g. "soil moisture is 15%"). You don\'t need to provide all of them if you don\'t have the data.';

const MAX_CHARS = 2000;

export function AnalysisSection() {
  const [query, setQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [sessionId, setSessionId] = useState<string>('');
  
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    // Initialize session ID on the client
    setSessionId(getOrCreateSessionId());
  }, []);

  const charCount = query.length;
  const isOverLimit = charCount > MAX_CHARS;
  const isEmpty = query.trim().length === 0;
  
  const isRequiresInfo = result?.status === 'requires_more_info';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (isEmpty || isLoading || isOverLimit) return;

    setIsLoading(true);
    setError(null);

    try {
      const response = await runAnalysis({
        session_id: sessionId,
        query: query.trim(),
      });
      setResult(response);
      
      // Clear the query field after a successful "requires_more_info" turn
      // so the user can easily type just the missing metrics.
      if (response.status === 'requires_more_info') {
        setQuery('');
      }
    } catch (err: unknown) {
      if (err instanceof ApiError) {
        setError(err.message);
      } else {
        setError('An unexpected error occurred while connecting to the backend.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setQuery('');
    setResult(null);
    setError(null);
    setSessionId(resetSession());
    textareaRef.current?.focus();
  };

  return (
    <section className="px-6 py-12 md:py-20">
      <div className="mx-auto max-w-4xl space-y-10">
        
        {/* ── Results area (moved above input so users see missing metrics first) ── */}
        {result && <ResultsPanel result={result} />}

        {/* ── Input form ─────────────────────────────────────── */}
        <form onSubmit={handleSubmit} noValidate className={result?.status === 'complete' ? 'hidden' : 'block'}>
          <div className="space-y-4">
            {/* Label */}
            <div className="flex items-baseline justify-between">
              <label
                htmlFor="analysis-query"
                className="block text-sm font-semibold tracking-wide text-stone-800"
              >
                {isRequiresInfo 
                  ? 'Provide Additional Information' 
                  : 'Describe your environmental observations'}
              </label>
              <span
                className={`text-xs tabular-nums font-medium ${
                  isOverLimit
                    ? 'text-red-500'
                    : 'text-stone-400'
                }`}
                aria-live="polite"
              >
                {charCount}/{MAX_CHARS}
              </span>
            </div>

            {/* Textarea */}
            <textarea
              id="analysis-query"
              ref={textareaRef}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder={isRequiresInfo ? FOLLOWUP_PLACEHOLDER : DEFAULT_PLACEHOLDER}
              rows={isRequiresInfo ? 3 : 6}
              disabled={isLoading}
              aria-describedby="query-hint"
              className={`
                w-full resize-none rounded-2xl border bg-white px-5 py-4
                text-base leading-relaxed text-stone-900 placeholder:text-stone-400
                shadow-sm transition-all duration-200
                focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500
                disabled:bg-stone-50 disabled:text-stone-500 disabled:cursor-not-allowed
                ${isOverLimit ? 'border-red-300 focus:ring-red-400/50 focus:border-red-400' : 'border-stone-200'}
                ${error ? 'border-red-300' : ''}
              `}
            />

            {/* Helper text + submit row */}
            <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between pt-1">
              <p id="query-hint" className="text-[13px] leading-relaxed text-stone-500 max-w-sm">
                {isRequiresInfo
                  ? 'The engine remembers your previous context. You do not need to restate it. Just provide what you can.'
                  : 'Include specific metrics and values where available — e.g. soil pH: 5.2, species richness: 18 per ha'}
              </p>

              <div className="flex items-center gap-4 self-end sm:self-auto">
                {isRequiresInfo && (
                  <button
                    type="button"
                    onClick={handleReset}
                    className="text-sm font-medium text-stone-400 hover:text-stone-700 transition-colors"
                  >
                    Start over
                  </button>
                )}
                <Button
                  type="submit"
                  isLoading={isLoading}
                  disabled={isEmpty || isOverLimit}
                  variant="primary"
                >
                  {isLoading ? (isRequiresInfo ? 'Updating…' : 'Analyzing…') : (isRequiresInfo ? 'Update Analysis' : 'Run Analysis')}
                </Button>
              </div>
            </div>

            {/* API error banner */}
            {error && (
              <div
                role="alert"
                className="mt-6 flex items-start gap-3 rounded-2xl border border-red-200/60 bg-red-50/80 px-5 py-4 text-sm text-red-900 shadow-sm"
              >
                <svg className="h-5 w-5 shrink-0 text-red-500" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                   <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.28 7.22a.75.75 0 00-1.06 1.06L8.94 10l-1.72 1.72a.75.75 0 101.06 1.06L10 11.06l1.72 1.72a.75.75 0 101.06-1.06L11.06 10l1.72-1.72a.75.75 0 00-1.06-1.06L10 8.94 8.28 7.22z" clipRule="evenodd" />
                </svg>
                <div>
                  <h4 className="font-semibold text-red-900">Analysis Error</h4>
                  <p className="mt-1 text-red-800/90">{error}</p>
                </div>
              </div>
            )}

            {/* Validation error */}
            {isOverLimit && (
              <p role="alert" className="text-[13px] font-medium text-red-500 flex items-center gap-1.5">
                <svg className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-5a.75.75 0 01.75.75v4.5a.75.75 0 01-1.5 0v-4.5A.75.75 0 0110 5zm0 10a1 1 0 100-2 1 1 0 000 2z" clipRule="evenodd" />
                </svg>
                Query exceeds {MAX_CHARS} character limit. Please shorten your description.
              </p>
            )}
          </div>
        </form>

        {/* If complete, we hide the form above and just show a Start Over button below the results */}
        {result?.status === 'complete' && (
           <div className="flex justify-center pt-10 border-t border-stone-200/60 mt-12">
             <Button type="button" onClick={handleReset} variant="secondary">
               Start a New Analysis
             </Button>
           </div>
        )}
      </div>
    </section>
  );
}
