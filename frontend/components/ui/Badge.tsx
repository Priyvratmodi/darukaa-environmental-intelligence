import React from 'react';

interface BadgeProps {
  children: React.ReactNode;
  className?: string;
}

/**
 * Small inline badge / pill component for status labels,
 * evidence strength, confidence levels, and domain tags.
 */
export function Badge({ children, className = '' }: BadgeProps) {
  return (
    <span
      className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium ${className}`}
    >
      {children}
    </span>
  );
}
