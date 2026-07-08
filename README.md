<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="auto">
  <defs>
    <!-- Disco gradient – moves around -->
    <linearGradient id="disco" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff0055"/>
      <stop offset="25%" stop-color="#ff6600"/>
      <stop offset="50%" stop-color="#ffcc00"/>
      <stop offset="75%" stop-color="#00ff88"/>
      <stop offset="100%" stop-color="#0088ff"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="y1" values="0%;100%;0%" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="100%;0%;100%" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="100%;0%;100%" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    <!-- Glow filter for text (aura) -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <!-- Aura blur for the disco border glow -->
    <filter id="auraBlur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10"/>
    </filter>
  </defs>

  <!-- Solid black background -->
  <rect x="0" y="0" width="800" height="400" fill="#000000"/>

  <!-- Disco‑light border (animated + pulsing) -->
  <rect x="10" y="10" width="780" height="380" rx="20" ry="20" fill="none" stroke="url(#disco)" stroke-width="8" opacity="0.95">
    <animate attributeName="stroke-width" values="8;14;8" dur="2s" repeatCount="indefinite"/>
  </rect>
  <!-- Outer blurred glow border (extra aura) -->
  <rect x="5" y="5" width="790" height="390" rx="25" ry="25" fill="none" stroke="url(#disco)" stroke-width="4" opacity="0.5" filter="url(#auraBlur)">
    <animate attributeName="stroke-width" values="4;8;4" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- Ambient floating aura orbs (for extra glow) -->
  <circle cx="200" cy="100" r="120" fill="#ff66aa" opacity="0.12" filter="url(#auraBlur)">
    <animate attributeName="opacity" values="0.06;0.15;0.06" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="600" cy="300" r="150" fill="#66ccff" opacity="0.10" filter="url(#auraBlur)">
    <animate attributeName="opacity" values="0.04;0.12;0.04" dur="6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="400" cy="200" r="180" fill="#ffcc00" opacity="0.08" filter="url(#auraBlur)">
    <animate attributeName="opacity" values="0.05;0.12;0.05" dur="7s" repeatCount="indefinite"/>
  </circle>

  <!-- Jumping words with different colours and staggered delays -->
  <g font-family="'Segoe UI', 'Poppins', sans-serif" font-weight="800" font-size="60" text-anchor="middle" filter="url(#glow)">
    <!-- Summer (orange) -->
    <text x="160" y="240" fill="#ff6b35">
      Summer
      <animateTransform attributeName="transform" type="translate" values="0,0; 0,-40; 0,-20; 0,-50; 0,0" dur="1.8s" repeatCount="indefinite"/>
    </text>
    <!-- PEP (gold) -->
    <text x="320" y="240" fill="#ffcc00">
      PEP
      <animateTransform attributeName="transform" type="translate" values="0,0; 0,-45; 0,-25; 0,-55; 0,0" dur="1.8s" repeatCount="indefinite" begin="0.15s"/>
    </text>
    <!-- Daily (green) -->
    <text x="480" y="240" fill="#00ff88">
      Daily
      <animateTransform attributeName="transform" type="translate" values="0,0; 0,-35; 0,-15; 0,-45; 0,0" dur="1.8s" repeatCount="indefinite" begin="0.30s"/>
    </text>
    <!-- Work (blue) -->
    <text x="640" y="240" fill="#66ccff">
      Work
      <animateTransform attributeName="transform" type="translate" values="0,0; 0,-50; 0,-30; 0,-60; 0,0" dur="1.8s" repeatCount="indefinite" begin="0.45s"/>
    </text>
  </g>

  <!-- Extra glow layer behind text for stronger aura (semi‑transparent) -->
  <g font-family="'Segoe UI', 'Poppins', sans-serif" font-weight="800" font-size="60" text-anchor="middle" opacity="0.2" filter="url(#glow)">
    <text x="160" y="240" fill="#ff6b35">Summer</text>
    <text x="320" y="240" fill="#ffcc00">PEP</text>
    <text x="480" y="240" fill="#00ff88">Daily</text>
    <text x="640" y="240" fill="#66ccff">Work</text>
  </g>
</svg>
