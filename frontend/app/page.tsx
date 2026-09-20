import { Header } from '@/components/layout/Header';
import { HeroSection } from '@/components/layout/HeroSection';
import { AnalysisSection } from '@/components/analysis/AnalysisSection';

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <Header />

      <main className="flex-1">
        <HeroSection />
        <AnalysisSection />
      </main>

      <footer className="border-t border-gray-100 px-6 py-6">
        <div className="mx-auto flex max-w-5xl items-center justify-between">
          <p className="text-xs text-gray-400">
            Darukaa Environmental Intelligence &mdash; evidence-based causal reasoning
          </p>
          <p className="text-xs text-gray-300 font-mono">v0.1.0</p>
        </div>
      </footer>
    </div>
  );
}
