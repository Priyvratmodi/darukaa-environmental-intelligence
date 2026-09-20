import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  async rewrites() {
    // Read the backend URL from environment variables, defaulting to localhost:8000
    const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
    
    return [
      {
        source: '/api/:path*',
        destination: `${API_URL}/:path*`,
      },
    ];
  },
};

export default nextConfig;
