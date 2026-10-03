# OneAquaHealth: Data, Dashboard & Demo Video

**Author:** Laksh Panthi  
**Role:** Data Engineering, Dashboard Architecture & Demo Video Lead  
**Initiative:** OneAquaHealth (Horizon Europe Project No. 101086521) / IEEE Global Hackathon 2026  
**Pilot Study Cities:** Coimbra (Portugal), Benevento (Italy), Ghent (Belgium), Oslo (Norway), Toulouse (France)  

---

## 🌊 Executive Project Overview

Under the **"One Health"** paradigm (linking aquatic ecosystem well-being directly with human physical and mental health), this platform provides an operational citizen science surveillance dashboard. It connects grassroots volunteer field monitoring with municipal environmental decision-support across 5 European pilot river basins.

### Key Milestones Delivered:
1. **Today:** Installed official Citizen Science mobile app, reviewed Session 5 Hub tools, and produced an executive assessment on open data availability (`docs/open-data-assessment.md`).
2. **Thu by Noon:** Curated and validated the 15-site baseline dataset across all 5 pilot cities (`data/sites-15.json`).
3. **Thu / Fri:** Expanded to an exhaustive registry of **100 monitoring sites** (exactly 20 per pilot city) with authentic hydrologic names, geo-coordinates, and clearly labeled with `"source": "synthetic"` (`data/sites.json`).
4. **Seed Observations:** Added **130 historical citizen observation checks** (`data/seed-observations.json`) spanning water temperature, pH, dissolved oxygen, turbidity, biological health scores, and human well-being ratings.
5. **Surveillance Dashboard (`src/features/dashboard/`):**
   - **3 Core Stat Cards:** Coverage Rate (72.0%), Never-Checked Sites (28 sites / 28.0%), and Average Days Since Check (11.4 days).
   - **Recharts City Bar Chart:** Grouped and stacked visualization of monitored vs. never-checked sites across all 5 basins.
   - **Community Challenge Progress Bar:** Sprint goal tracking 130 / 200 checks (65%), milestone tiers, and motivational badges.
   - **Priority Queue & Site Registry:** Filterable alerts for unmonitored stream reaches.
   - **Live Feed:** Stream observations with chemical and perceptual metrics.
6. **Sat Video Production Guide (`docs/demo-video-guide.md`):** Complete 3–5 min video script, storyboard, recording setup, DaVinci/CapCut checklist, screenshot plan, and YouTube publishing metadata.
7. **2-Hour Learning Guide (`docs/learning-guide-json-fetch-recharts.md`):** Practical curriculum on JSON modeling, `fetch()` with async/await, and Recharts bar chart implementations.

---

## 📁 Repository Structure

```
oneaquahealth-dashboard/
├── data/
│   ├── sites-15.json              # 15-site starter benchmark (3 sites per pilot city)
│   ├── sites.json                 # 100 pilot sites (20 per city, source: "synthetic")
│   └── seed-observations.json     # 130 realistic citizen field checks (past 45 days)
├── docs/
│   ├── open-data-assessment.md    # Session 5 review & half-page note on open data
│   ├── demo-video-guide.md        # 3-5 min video script, storyboard & YouTube metadata
│   └── learning-guide-json-fetch-recharts.md # 2-hour practical study curriculum
├── src/
│   └── features/
│       └── dashboard/
│           ├── CityBarChart.jsx           # Recharts 5-city comparative bar chart
│           ├── CommunityChallenge.jsx     # Community goal progress bar & tiers
│           ├── Dashboard.jsx              # Composite React master dashboard
│           ├── dashboardDataService.js    # Data aggregation & metrics calculation
│           ├── index.js                   # Feature barrel exports
│           ├── ObservationsFeed.jsx       # Real-time observation feed
│           ├── SiteListTable.jsx          # Filterable sites & priority alerts table
│           └── StatCard.jsx               # Reusable stat card widget
├── index.html                     # Standalone, interactive browser-ready dashboard
├── package.json                   # React 18, Vite, Recharts & Tailwind configuration
├── generate_data.py               # Dataset generation & validation script
├── serve.py                       # Python local web server launcher
├── start_dashboard.bat            # Windows 1-click launch batch script
└── README.md                      # This comprehensive documentation
```

---

## 🚀 Quickstart: Launching the Dashboard

### Option 1: 1-Click Launch (Windows / Python) — Recommended
Double-click `start_dashboard.bat` or run:
```powershell
python serve.py
```
This serves the dashboard locally and automatically opens `http://localhost:8000` in your default browser.

### Option 2: Direct File Open
Open `index.html` directly in any modern web browser (Google Chrome, Microsoft Edge, Brave, Firefox). Built-in offline fallback ensures complete functionality even without a local web server.

### Option 3: Modern React + Vite Dev Server
When Node.js is installed:
```bash
npm install
npm run dev
```

---

## 📊 Core Surveillance Metrics (The 3 Stat Cards)

1. **Coverage Rate (72.0%):**
   $$\text{Coverage Rate} = \frac{\text{Checked Sites (72)}}{\text{Total Sites (100)}} \times 100 = 72.0\%$$
   Indicates proportion of pilot aquatic zones under active citizen surveillance.
2. **Never-Checked Sites (28 Sites / 28.0%):**
   Highlights unmonitored river reaches (e.g. urban culverts, agricultural drains) that require volunteer mobilization.
3. **Average Days Since Check (11.4 Days):**
   Calculates the average elapsed days since the latest observation across active sites, ensuring environmental data freshness below the 14-day threshold.

---

## 🎥 Saturday Video Recording & YouTube Submission Checklist

Refer to [`docs/demo-video-guide.md`](docs/demo-video-guide.md) for full details:
- **Duration:** 3:45 (strictly within the 3–5 min hackathon guideline).
- **Segments:** Hook (0:00–0:35) $\rightarrow$ Data Strategy (0:35–1:15) $\rightarrow$ 3 Stat Cards (1:15–2:05) $\rightarrow$ Recharts Bar Chart (2:05–2:50) $\rightarrow$ Community Challenge (2:50–3:30) $\rightarrow$ Conclusion (3:30–3:50).
- **Screenshots:** Capture the 5 specified PNGs at 1920x1080 for presentation slides and repository header.
- **YouTube Metadata:** Optimized title, description, chapter timestamps, and tags included ready for copy-paste.
