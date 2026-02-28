# Trout Stream Proximity Tool - Unknowns

Last Updated: February 25, 2026

---

## 🔴 Must Decide Before Coding (Phase 1 Research - 4 hours)

These are blockers. Must research and decide in Week 1.

### Technology Decisions (60 min total)

- [x] **GIS Library Choice** (30 min)
  - GeoPandas vs PostGIS vs ArcPy
  - Research budget: 30 minutes
  - Decision criteria: Ease of learning, AI agent support, documentation
  - **Status:** Complete
  - **Decision:** GeoPandas
  - **Rationale:**
    - leverages pandas, which is common package
    - free to use
    - no database (PostGIS has PostgreSQL back end - possible fo V2)
    - well documented
    - other users can use app without licensing

- [ ] **Geocoding Service** (15 min)
  - Census Bureau Geocoder vs Google Maps API
  - Research budget: 15 minutes
  - Decision criteria: Free tier limits, accuracy, ease of use
  - **Status:** Not started
  - **Decision:** [To be filled in Phase 1]

- [ ] **Map Visualization Library** (15 min)
  - Folium vs Plotly vs Leaflet.js
  - Research budget: 15 minutes
  - Decision criteria: Integration with GeoPandas, ease of use
  - **Status:** Not started
  - **Decision:** [To be filled in Phase 1]

---

## 🟡 Validate in Spike Phase (Phase 1 - Session 4)

These need proof-of-concept before committing to approach.

### Data Source Validation (90 min spike)

- [x] **PA Fish & Boat Class A Data Accessibility**
  - Question: Can we programmatically access Class A Wild Trout data?
  - Where to look: <https://gis.pfbc.pa.gov/>
  - Validation: Download or fetch sample data
  - **Status:** Found
  - **Result:**
    - **REST API for PA trout waters**
    - URL: <https://mapservices.pasda.psu.edu/server/rest/services/pasda/PAFishBoat/MapServer>
    - Contains all layers of trout streams
    - Contains layers for confirmed public or semi-public access

- [x] **Public Access Point Data Existence**
  - Question: Does PA Fish & Boat publish public access GIS data?
  - Fallback: State Game Lands boundaries from PA Game Commission
  - Fallback 2: State Forest boundaries from DCNR
  - **Status:** Found
  - **Result:**
    - See REST API for PA trout waters in previous section

- [ ] **County Data Availability**
  - Question: Is data available for Centre, Clinton, Lycoming counties?
  - Validation: Confirm all 3 counties covered in dataset
  - **Status:** Not started
  - **Result:** [To be filled in spike]

### Technical Validation (During spike)

- [ ] **GeoPandas Can Load PA Data**
  - Question: Can GeoPandas read PA Fish & Boat format?
  - Test: Load sample stream data
  - **Status:** Not started
  - **Result:** [To be filled in spike]

- [ ] **Distance Calculation Works**
  - Question: Can we calculate geodesic distance correctly?
  - Test: Calculate distance from known point to known stream
  - **Status:** Not started
  - **Result:** [To be filled in spike]

- [ ] **Coordinate Reference Systems**
  - Question: What CRS is PA data in?
  - Test: Load data and check CRS
  - Note: May need to reproject for distance calculations
  - **Status:** Not started
  - **Result:** [To be filled in spike]

---

## 🟢 Learn While Building (Don't Research Now)

Reference documentation as needed during development. No pre-research required.

### GeoPandas Operations

- How to filter GeoDataFrames by attribute
- How to calculate buffers around geometries
- How to find nearest geometry
- How to reproject coordinate systems
- How to export to GeoJSON

### Streamlit Specifics

- Component layout and organization
- File upload widgets
- Map display integration
- Error handling and user feedback
- Caching for performance

### Testing GIS Code

- How to test spatial operations
- Creating test fixtures with sample geometries
- Assertion approaches for GeoDataFrames
- Mocking geocoding APIs

### Map Visualization

- Folium marker customization
- Layer control (toggle streams, access points)
- Popup content formatting
- Color coding by classification
- Distance measurement display

### Error Handling

- Invalid address handling
- Out-of-bounds address (not in PA)
- No nearby streams scenario
- Missing data graceful degradation

### Performance

- Loading large shapefiles
- Spatial indexing for faster queries
- Caching frequently-used data
- Optimizing distance calculations

**Note:** If stuck on any of these >2 hours, ask for help. Don't research upfront.

---

## 🟠 Nice-to-Know (Future Versions)

Explicitly NOT researching for v1.0. Park for later.

### v2.0 Considerations

- Google Maps Directions API for driving distance
- Property parcel boundary integration
- Additional stream classifications
- Batch processing multiple addresses
- Database for caching/performance

### Advanced Features

- Stream flow data integration
- Water quality metrics
- Seasonal access restrictions
- Fishing regulations by segment

### Infrastructure

- Deployment to Streamlit Cloud
- CI/CD pipeline setup
- Automated testing on commit

---

## Decision Log

As decisions are made during Phase 1, document them here:

### Technology Decisions

**GIS Library:**

- Decision: [TBD]
- Date: [TBD]
- Reasoning: [TBD]
- ADR: docs/adr/001-tech-stack.md

**Geocoding Service:**

- Decision: [TBD]
- Date: [TBD]
- Reasoning: [TBD]

**Map Visualization:**

- Decision: [TBD]
- Date: [TBD]
- Reasoning: [TBD]

### Data Source Decisions

**Public Access Data:**

- Decision: [TBD]
- Date: [TBD]
- Source: [TBD]
- Fallback used: [Yes/No]

### Approach Decisions

**Distance Calculation Method:**

- Decision: Geodesic (straight-line accounting for Earth curvature)
- Date: Feb 21, 2026
- Reasoning: Simpler than driving distance, good enough for property screening
- Future: May add driving distance in v2.0

**Stream Classifications:**

- Decision: Class A Wild Trout only
- Date: Feb 21, 2026
- Reasoning: Highest quality waters, simplest dataset, easy to expand later

**Geographic Scope:**

- Decision: Centre, Clinton, Lycoming counties
- Date: Feb 21, 2026
- Reasoning: Good data quality, familiar areas, quality streams, manageable scope

---

## Research Session Plan (Phase 1 - Week 1)

### Session 1: Monday Evening (30 min)

**Goal:** Decide on GIS library

- Google: "python gis analysis", "geopandas vs alternatives"
- Read: GeoPandas docs overview
- Ask Claude: "Compare GeoPandas vs PostGIS for Python GIS beginner"
- **Decision by end of session**
- Document in UNKNOWNS.md

### Session 2: Wednesday Evening (30 min)

**Goal:** Verify PA data accessibility

- Find PA Fish & Boat ArcGIS portal
- Explore available services
- Check for Class A Wild Trout layer
- Identify public access data (or fallbacks)
- **Validate data exists**
- Document findings in UNKNOWNS.md

### Session 3: Friday Evening (90 min)

**Goal:** GeoPandas hello world

- Install GeoPandas
- Follow official quickstart
- Load sample world dataset
- Calculate simple distance
- Write first test
- **Commit working code**

### Session 4: Saturday/Sunday (90 min)

**Goal:** PA data spike

- Download/access PA stream data
- Load with GeoPandas
- Filter to Class A streams
- Calculate distance from test point
- **Prove concept works**
- Document in UNKNOWNS.md

### After Session 4: Go/No-Go Decision

- If all 🟡 items validated → Proceed to development
- If blockers found → Pivot approach or kill project

---

## Questions for Future Investigation

Non-blocking questions to explore if time permits:

- How accurate is straight-line vs driving distance for rural PA?
- What percentage of Class A streams have public access?
- Could we estimate stream quality from surrounding land use?
- Are there seasonal access restrictions we should note?
- How frequently is PA Fish & Boat data updated?

**Note:** Don't research these now. Maybe never. Focus on v1.0.

---

## Status Summary

**🔴 Red Unknowns:** 3 total (all in Phase 1)
**🟡 Yellow Unknowns:** 6 total (all in spike)
**🟢 Green Unknowns:** Many (reference docs as needed)
**🟠 Orange Unknowns:** Intentionally ignored for v1.0

**Phase 1 Research Budget:** 4 hours (240 minutes)

- Session 1: 30 min
- Session 2: 30 min
- Session 3: 90 min
- Session 4: 90 min
**Total: 240 minutes (4 hours exactly)**

**Next Update:** After Phase 1 complete (by Feb 27)
