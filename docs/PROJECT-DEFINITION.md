# Project: Trout Stream Proximity Tool

## One-Sentence Pitch

Trout Stream Proximity Tool helps property hunters assess proximity to Pennsylvania's Class A wild trout waters by analyzing PA Fish & Boat stream classification data and calculating distances to the nearest Class A stream.

## The Problem This Solves

When property hunting in rural PA, it's impossible to know how close a parcel is to quality wild trout fishing. Real estate listings don't include this information, and manually cross-referencing maps is tedious and error-prone. This tool automates the spatial analysis.

## Ethical Design Decision

This tool focuses on PUBLIC access points to avoid enabling trespassing on private land. It promotes ethical fishing by highlighting publicly accessible waters rather than systematically identifying private streams. A private version for personal property analysis may be built later using these learnings.

---

## v1.0 Success Criteria (DONE = SHIPPED)

**Functional Requirements:**

- [x] User can input a single property address
- [x] Tool calculates distance to nearest Class A wild trout stream
- [x] Interactive map displays property location and nearest stream
- [x] Results show straight-line distance in miles
- [x] Works for all Pennsylvania addresses against statewide Class A stream data
- [x] No crashes on valid Pennsylvania addresses

**Quality Requirements:**

- [x] README with working setup instructions
- [x] At least 3 passing tests
- [x] 2-3 ADRs documenting key decisions
- [x] Demo screenshot showing working map

**Shipping Requirements:**

- [x] Code on GitHub (public repo)
- [ ] Shared on LinkedIn
- [x] Added to resume
- [x] Tagged as v1.0 release

**Ship Date:** Friday, April 24, 2026
**Kill Date:** Friday, May 1, 2026

---

## v1.0 Features (Must-Have)

1. **Address Input**
   - Single address text input
   - Geocode to lat/lng coordinates
   - Validate address is in PA

2. **Stream Data Loading**
   - Load PA Fish & Boat Class A Wild Trout stream data
   - Parse stream geometries

3. **Distance Calculation**
   - Find nearest Class A public stream
   - Calculate geodesic distance in miles
   - Account for Earth's curvature

4. **Map Visualization**
   - Interactive map (Folium)
   - Property location marker
   - Nearest Class A stream line
   - Stream tooltip displaying stream name on hover
   - Stream popup displaying stream name, distance from address, and percent on public land on click

5. **Results Display**
   - Narrative summary: "The Class A trout stream nearest to [address] is: [stream name], which is [distance] mile(s) away."
   - Interactive map with stream and address marker

---

## v1.0 Technical Decisions

**Distance Calculation:**

- Straight-line distance ("as the crow flies")
- Geodesic calculation using GeoPandas
- Miles as display unit

**Stream Classification:**

- Class A Wild Trout ONLY
- Excludes naturally reproducing, approved, stocked

**Geographic Scope:**

- PA Statewide Class A stream data

---

## Explicitly OUT OF SCOPE for v1.0

**Features deferred to v2.0+:**

- Driving distance/turn-by-turn directions
- Multiple address batch processing
- Other stream classifications (Naturally Reproducing, Approved)
- Property boundary data integration
- Saved searches or bookmarking
- User accounts/authentication
- Mobile app version
- Performance optimization
- Real-time data updates

**Features permanently out of scope:**

- Private stream identification without public access
- Systematic listing of all stream properties
- Integration with real estate APIs
- Trespassing enablement features

**Advanced analysis (future):**

- Stream flow data
- Water quality metrics
- Elevation/topography
- Fish stocking schedules
- Seasonal access restrictions

---

## Data Sources

**Required (must verify in Phase 1):**

1. PA Fish & Boat Commission GIS Data
   - Class A Wild Trout stream classifications
   - Stream geometries (polylines)
   - Format: ArcGIS REST Service or Shapefile

2. Public Access Points
   - PA Fish & Boat public access database OR
   - State Game Lands boundaries (PGC)
   - State Forest boundaries (DCNR)
   - Format: Shapefile or GeoJSON

3. Address Geocoding
   - Census Bureau Geocoder (free, unlimited) OR
   - Google Maps Geocoding API (free tier: 40k/month)

**URLs to find in Phase 1:**

- PA Fish & Boat ArcGIS: <https://gis.pfbc.pa.gov/>
- PA Game Commission GIS: [Find in research]
- PA DCNR GIS: [Find in research]

---

## Technical Stack (Decided in Phase 1)

**Backend/Analysis:**

- Python 3.x
- GeoPandas (spatial analysis)
- Shapely (geometry operations)
- Pandas (data manipulation)

**Frontend/UI:**

- Streamlit (web interface)
- Folium (interactive maps)

**Data Storage:**

- Local files (GeoJSON/Shapefiles)
- No database required for MVP

**Testing:**

- pytest
- pytest-cov (coverage)

---

## Timeline & Commitment

**Start Date:** February 21, 2026 (Friday)
**Ship Date:** April 24, 2026 (Friday) - 9 weeks
**Kill Date:** May 1, 2026 (Friday) - 10 weeks

**Time Commitment:** 8-10 hours/week

- Three 90-minute evening sessions (4.5 hours)
- One 2-hour weekend session (2 hours)
- One 30-minute Sunday review (0.5 hours)
- Total: 7 hours/week minimum

**If not shipped by kill date:**

- Document learnings in LESSONS_LEARNED.md
- Commit all code to GitHub
- Write brief post-mortem
- Move on without guilt
- Apply learnings to next project

---

## Weekly Schedule

**Monday, Wednesday, Friday:** 90-minute dev sessions

- Focus on TDD (one test at a time)
- Reference docs only when stuck
- Park ideas in FUTURE.md
- Commit progress

**Saturday or Sunday:** 2-hour focused session

- Bigger feature work
- Integration testing
- Catch up if behind

**Sunday Evening:** 30-minute weekly review

- Check progress against timeline
- Update this document if scope changes
- Decide: continue, pivot, or kill
- Plan next week's focus

---

## Phase Breakdown

### Week 1 (Feb 21-27): Research & Setup

#### Phase 1: Time-Boxed Research (4 hours)

- GeoPandas landscape survey
- Technology decisions
- Hello world
- Data source spike

**Deliverables:**

- [x] GeoPandas installed and working
- [x] PA stream data loaded in test script
- [x] First test passing
- [x] UNKNOWNS.md updated with findings

### Post week 1 notes

- made decision to pivot to an iterative week-by-week learning plan
- placing more emphasis on learning the core Pandas framework workflows
- shifting to leverage AI as coaching-focused learning model rather than a copy-paste model

---

## Accountability Plan

**Daily Dev Log:**

- Track in `daily-log.md`
- 5-minute end-of-session notes
- What worked, what blocked, what's next

**Weekly Check-Ins:**

- Share dev log in project chat
- Review progress against timeline
- Celebrate wins, diagnose blocks
- Adjust scope if needed

**Public Commitment:**

- LinkedIn post when shipped
- GitHub activity visible
- Resume updated with project

---

## Research Budget: 4 Hours MAX

### Session 1 (30 min): Landscape Survey

- Python GIS options comparison
- GeoPandas vs PostGIS vs alternatives
- Decision: Which library?

### Session 2 (30 min): Data Source Verification

- Find PA Fish & Boat ArcGIS URL
- Verify Class A data exists and is accessible
- Find public access point data
- Decision: Can we get the data we need?

### Session 3 (90 min): GeoPandas Hello World

- Install GeoPandas and dependencies
- Load sample shapefile
- Basic operations (filter, buffer, distance)
- Write first test

### Session 4 (90 min): PA Data Spike

- Download/access PA stream data
- Load it with GeoPandas
- Filter to Class A streams
- Calculate sample distance
- Decision: Is this buildable?

#### After 4 hours: Go/No-Go decision

---

## Success Metrics

**Week 1:**

- [ ] Research complete (4 hours, no more)
- [ ] Can load PA stream data
- [ ] First test passing
- [ ] Clear understanding of approach

**Week 2:**

- [ ] Geocoding works
- [ ] Distance calculation works
- [ ] 3+ tests passing

**Week 3:**

- [ ] Map displays
- [ ] Integration working
- [ ] 5+ tests passing

**Week 4:**

- [ ] Streamlit interface functional
- [ ] End-to-end demo works
- [ ] Error handling added

**Week 5:**

- [ ] Documentation complete
- [ ] Demo ready
- [ ] SHIPPED on GitHub
- [ ] Shared on LinkedIn

---

## Risk Mitigation

### Risk: Public access data doesn't exist

- Mitigation: Use State Game Lands/Forest boundaries
- Fallback: Distance to any Class A stream segment

### Risk: GeoPandas too complex

- Mitigation: Spike in Week 1, pivot to simpler tool if needed
- Fallback: Basic lat/lng distance calculation without GIS

### Risk: Getting stuck for multiple days

- Mitigation: Ask for help after 4 hours stuck
- Fallback: Skip feature, reduce scope

### Risk: Scope creep

- Mitigation: FUTURE.md for all new ideas
- Fallback: Weekly review cuts features if behind

### Risk: Losing motivation

- Mitigation: Weekly check-ins
- Fallback: Kill project by Week 6, document learnings

---

## Notes

**Why Class A Only for v1.0:**

- Simplest dataset to work with
- Highest quality waters (most interesting)
- Easy to add other classifications in v2.0
- Keeps scope manageable for learning GIS

**Why statewide geographic scope:**

- The statewide GeoJSON dataset was already available and complete, requiring no additional filtering logic to subset by county.
- Calculating distance across the entire dataset was simpler and more accurate than filtering by county first.
- If limiting to a subset of PA counties, it would be possible for the nearest stream to actually be located in a neighboring county, which would be masked due to the county filtering.

**Why Straight-Line Distance:**

- Simpler calculation (no API costs)
- Good enough for initial property screening
- Driving distance can be v2.0 feature
- Keeps MVP focused on GIS learning

---

## Future Enhancements (v2.0+)

**After v1.0 ships, consider:**

1. Driving distance via Google Maps API
2. Additional stream classifications
3. Batch address processing
4. Property boundary integration
5. Saved searches
6. Mobile-responsive UI
7. Performance optimization

**Separate private tool (future project):**

- Properties containing streams (not just access)
- Private repo for personal use
- Built using learnings from this project
- Ethical considerations documented

---

## Project Repository Structure

```markdown
trout-stream-proximity-tool/
├── data
│   └── Class A Trout Streams.geojson
├── docs
│   ├── adr
│   │   ├── 001-geocoding-api-selection.md
│   │   ├── 002-distance-calculation-methodology.md
│   │   └── 003-geographic-scope.md
│   ├── daily-log.md
│   ├── EXECUTION-PLAN.md
│   ├── FUTURE.md
│   ├── images
│   │   └── screenshot.png
│   ├── PANDAS-CHEATSHEET.md
│   ├── PROJECT-DEFINITION.md
│   ├── PYTHON-CHEATSHEET.md
│   └── UNKNOWNS.md
├── learning
│   ├── folium_map_basics.py
│   ├── folium_map_properties.py
│   ├── geopandas_exercise_stream_data.py
│   ├── google_geocode_api_basics.py
│   ├── pandas_basics.py
│   └── pandas_exercise_stream_data.py
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── src
│   ├── __init__.py
│   ├── address_geocode.py
│   ├── app.py
│   ├── proximity_analyzer.py
│   ├── proximity_map.py
│   └── stream_data.py
└── tests
    ├── __init__.py
    ├── test_address_geocode.py
    ├── test_app.py
    ├── test_proximity_analyzer.py
    ├── test_proximity_map.py
    └── test_stream_data.py
```

---

## Commitment Statement

I commit to:

- Following the project kickoff framework
- Time-boxing research to 4 hours
- Working 8-10 hours per week
- Weekly check-ins and progress sharing
- Shipping by April 24 or killing by May 1
- No exceptions, no extensions beyond kill date

Signed: Trevor Baker
Date: February 21, 2026

---

## **Status: v1.0 SHIPPED**
