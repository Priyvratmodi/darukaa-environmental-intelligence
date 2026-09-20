import React from 'react';

interface SpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  label?: string;
}

const SIZE_CLASSES = {
  sm: 'h-4 w-4 border-2',
  md: 'h-8 w-8 border-2',
  lg: 'h-12 w-12 border-4',
};

/**
 * Animated loading spinner used while API requests are in-flight.
 */
export function Spinner({ size = 'md', label = 'Loading…' }: SpinnerProps) {
  return (
    <div className="flex flex-col items-center justify-center gap-3" role="status" aria-label={label}>
      <div
        className={`rounded-full border-gray-200 border-t-green-600 animate-spin ${SIZE_CLASSES[size]}`}
      />
      {label && (
        <span className="text-sm text-gray-500">{label}</span>
      )}
    </div>
  );
}
