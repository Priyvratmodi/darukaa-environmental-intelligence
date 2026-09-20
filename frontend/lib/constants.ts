import type { Domain } from '@/types/api';

/** Human-readable labels for each environmental domain. */
export const DOMAIN_LABELS: Record<Domain, string> = {
  soil: 'Soil',
  water: 'Water',
  biodiversity: 'Biodiversity',
  land_use: 'Land Use',
  climate: 'Climate',
  pollution: 'Pollution',
  agriculture: 'Agriculture',
  habitat: 'Habitat',
  species: 'Species',
  ecosystem: 'Ecosystem',
  unknown: 'Unknown',
};

/** Tailwind colour classes for evidence strength badges. */
export const EVIDENCE_STRENGTH_CLASSES: Record<string, string> = {
  Strong: 'bg-green-100 text-green-800 border-green-200',
  Moderate: 'bg-yellow-100 text-yellow-800 border-yellow-200',
  Weak: 'bg-red-100 text-red-800 border-red-200',
};

/** Tailwind colour classes for confidence level badges. */
export const CONFIDENCE_CLASSES: Record<string, string> = {
  High: 'bg-green-100 text-green-800 border-green-200',
  Medium: 'bg-yellow-100 text-yellow-800 border-yellow-200',
  Low: 'bg-red-100 text-red-800 border-red-200',
};
