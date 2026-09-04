# NRB multi-page structure

## Proposed page map

- `pages/home/index.html` — Home entry point
- `pages/about/index.html` — About NRB
- `pages/monetary-policy/index.html` — Monetary policy
- `pages/bank-supervision/index.html` — Bank supervision
- `pages/forex-management/index.html` — Forex management
- `pages/statistics/index.html` — Statistics and indicators
- `pages/publications/index.html` — Publications
- `pages/notices/index.html` — Notices
- `pages/media-releases/index.html` — Media releases
- `pages/consumer-services/index.html` — Consumer services
- `pages/careers/index.html` — Careers
- `pages/contact/index.html` — Contact

## Shared structure

- `components/header.html` — reusable header and navigation
- `components/footer.html` — reusable footer
- `assets/css/nrb-core.css` — shared design tokens and reusable layout utilities
- `assets/` — future static assets such as images, icons, or scripts
- `docs/architecture.md` — architecture and page-family reference

## Current transition note

The existing `nrb.html` remains the canonical homepage prototype, while `pages/home/index.html` acts as the folder-based home route during the transition.
