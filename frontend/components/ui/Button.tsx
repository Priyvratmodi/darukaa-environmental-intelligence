import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost';
  isLoading?: boolean;
  children: React.ReactNode;
}

export function Button({
  variant = 'primary',
  isLoading = false,
  children,
  disabled,
  className = '',
  ...props
}: ButtonProps) {
  const base =
    'inline-flex items-center justify-center gap-2.5 rounded-full text-sm font-semibold transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-600 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-60';

  const variants = {
    primary:
      'bg-emerald-700 text-white hover:bg-emerald-800 hover:shadow-md active:bg-emerald-900 px-7 py-2.5 shadow-sm',
    secondary:
      'bg-stone-900 text-white hover:bg-stone-800 hover:shadow-md active:bg-stone-950 px-7 py-2.5 shadow-sm',
    ghost:
      'text-stone-600 hover:text-stone-900 hover:bg-stone-100 px-5 py-2.5',
  };

  return (
    <button
      className={`${base} ${variants[variant]} ${className}`}
      disabled={disabled ?? isLoading}
      aria-busy={isLoading}
      {...props}
    >
      {isLoading && (
        <svg
          className="h-4 w-4 animate-spin text-current"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <circle
            className="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            strokeWidth="4"
          ></circle>
          <path
            className="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          ></path>
        </svg>
      )}
      {children}
    </button>
  );
}
