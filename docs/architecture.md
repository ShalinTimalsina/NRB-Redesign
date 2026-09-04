# NRB Redesign Architecture

## Canonical structure

- `nrb.html` — canonical desktop homepage prototype
- `pages/home/index.html` — route alias for the homepage during transition
- `pages/<section>/index.html` — section landing pages and content templates
- `components/header.html` — reusable header/navigation markup reference
- `components/footer.html` — reusable footer markup reference
- `assets/css/nrb-core.css` — shared design tokens, base styles, and reusable layout utilities

## Homepage anatomy

The homepage is structured as a digital headquarters for Nepal Rastra Bank, not as a marketing landing page.

### Header layers

- Utility bar: language, accessibility, sitemap, contact, consumer protection portal
- Main header: logo, institutional identity, search, and primary navigation

### Homepage sections

1. Hero banner with institutional statement and economic snapshot
2. Popular Services
3. Economic Overview
4. Foreign Exchange Snapshot
5. Featured Publications
6. Latest Notices & Circulars
7. Media Centre
8. Consumer Services
9. NRB Institutional Network
10. Premium enterprise footer

## Page families

### Homepage
Used for the executive summary of the NRB ecosystem.

### Overview pages
Used for:
- About NRB
- Contact
- Careers
- Monetary Policy & Operations

### Dashboard pages
Used for:
- Statistics & Data
- Foreign Exchange

### Library pages
Used for:
- Publications
- Notices & Media
- Procurement

### Directory pages
Used for:
- Board of Directors
- Principal Officers
- Departments
- Provincial Offices

## Shared styling rules

- Desktop-first only
- 1440px page canvas
- 12-column layout behavior
- 8-point spacing system
- Inter as the primary font
- IBM Plex Sans for headings on pages that load the font
- Primary color `#25295B`
- Accent color `#138496`
- Subtle premium accent `#C59D5F`

## File organization intent

The codebase is organized so the structure mirrors the information architecture:

1. Global homepage entry
2. Section landing pages
3. Reusable component references
4. Shared visual system in one stylesheet
5. Future expansion into more detailed page templates without redesigning the foundation

## Design intent

- Institutional, executive, and research-focused
- Editorial content blocks instead of startup-style cards
- Data presented with hierarchy and restraint
- Clear routes to services, publications, and notices
