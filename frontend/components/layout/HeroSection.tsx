export function HeroSection() {
  return (
    <section className="relative overflow-hidden border-b border-stone-200/50 bg-stone-50/30 px-6 py-20 sm:py-28">
      {/* Decorative background element */}
      <div className="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-emerald-100/40 via-transparent to-transparent opacity-60" />

      <div className="mx-auto max-w-5xl">
        {/* Eyebrow label */}
        <p className="mb-6 flex items-center gap-3 text-xs font-bold uppercase tracking-[0.2em] text-emerald-700">
          <span className="block h-px w-8 bg-emerald-700/50" aria-hidden="true" />
          Evidence-Based Analysis
        </p>

        {/* Primary headline */}
        <h1 className="max-w-3xl text-4xl font-extrabold leading-[1.15] tracking-tight text-stone-900 sm:text-5xl lg:text-6xl">
          Understand what is changing
          <br />
          <span className="text-stone-400 font-medium">in your ecosystem.</span>
        </h1>

        {/* Subtitle */}
        <p className="mt-6 max-w-2xl text-lg leading-relaxed text-stone-600 sm:text-xl">
          Describe environmental changes and let Darukaa connect the evidence
          across soil, climate, land use and biodiversity — producing
          causal reasoning grounded in scientific literature.
        </p>

        {/* Domain tags */}
        <div className="mt-10 flex flex-wrap items-center gap-2.5" aria-label="Supported environmental domains">
          {[
            'Soil Health',
            'Hydrology',
            'Biodiversity',
            'Land Use',
            'Climate Dynamics',
            'Pollutants',
            'Agroecology',
            'Habitats',
          ].map((domain) => (
            <span
              key={domain}
              className="rounded-full border border-stone-200/80 bg-white/60 px-4 py-1.5 text-[13px] font-medium text-stone-600 backdrop-blur-sm shadow-sm transition-colors hover:bg-white hover:text-emerald-800"
            >
              {domain}
            </span>
          ))}
        </div>
      </div>
    </section>
  );
}
