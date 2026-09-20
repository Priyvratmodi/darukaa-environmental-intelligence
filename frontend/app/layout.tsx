import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

export const metadata: Metadata = {
  title: 'Darukaa — Environmental Intelligence',
  description:
    'Evidence-based environmental analysis. Multi-metric causal reasoning, scientific evidence retrieval, and actionable interventions.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="min-h-screen bg-white text-gray-900 antialiased font-sans">
        {children}
      </body>
    </html>
  );
}
