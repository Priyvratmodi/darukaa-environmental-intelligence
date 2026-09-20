import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
  title?: string;
}

/**
 * Modern card wrapper with a scientific, crisp aesthetic.
 */
export function Card({ children, className = '', title }: CardProps) {
  return (
    <div
      className={`rounded-2xl border border-stone-200/80 bg-white shadow-sm transition-shadow hover:shadow-md ${className}`}
    >
      {title && (
        <div className="border-b border-stone-100 bg-stone-50/50 px-6 py-4 rounded-t-2xl">
          <h3 className="text-[13px] font-bold text-stone-700 uppercase tracking-widest">
            {title}
          </h3>
        </div>
      )}
      <div className="p-6">{children}</div>
    </div>
  );
}
