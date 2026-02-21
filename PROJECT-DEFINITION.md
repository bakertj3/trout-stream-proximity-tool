# Project: Trout Stream Property Evaluator

## One-Sentence Pitch

Trout Stream Property Evaluator helps property hunters and anglers assess proximity to Pennsylvania's Class A wild trout waters by analyzing PA Fish & Boat classification data and calculating distances to public access points.

## The Problem This Solves

When house hunting in rural PA, it's impossible to know how close a property is to quality public wild trout fishing. Real estate listings don't include this information, and manually cross-referencing maps is tedious and error-prone. This tool automates the spatial analysis.

## Ethical Design Decision

This tool focuses on PUBLIC access points to avoid enabling trespassing on private land. It promotes ethical fishing by highlighting publicly accessible waters rather than systematically identifying private streams. A private version for personal property analysis may be built later using these learnings.

---

## v1.0 Success Criteria (DONE = SHIPPED)

**Functional Requirements:**

- [ ] User can input a single property address
- [ ] Tool calculates distance to nearest Class A wild trout public access
- [ ] Interactive map displays property location, streams, and access points
- [ ] Results show straight-line distance in miles
- [ ] Works for Centre, Clinton, and Lycoming counties
- [ ] No crashes on valid Pennsylvania addresses

**Quality Requirements:**

- [ ] README with working setup instructions
- [ ] At least 3 passing tests
- [ ] 2-3 ADRs documenting key decisions
- [ ] Demo screenshot showing working map

**Shipping Requirements:**

- [ ] Code on GitHub (public repo)
- [ ] Shared on LinkedIn
- [ ] Added to resume
- [ ] Tagged as v1.0 release

**Ship Date:** Friday, March 28, 2026
**Kill Date:** Friday, April 4, 2026

---

## v1.0 Features (Must-Have)

1. **Address Input**
   - Single address text input
   - Geocode to lat/lng coordinates
   - Validate address is in PA

2. **Stream Data Loading**
   - Load PA Fish & Boat Class A Wild Trout stream data
   - Filter to Centre, Clinton, Lycoming counties
   - Parse stream geometries

3. **Public Access Analysis**
   - Identify public access points OR
   - Use stream segments on public lands (State Game Lands/Forests)
   - Calculate straight-line (geodesic) distance from property

4. **Distance Calculation**
   - Find nearest Class A public access point
   - Calculate geodesic distance in miles
   - Account for Earth's curvature

5. **Map Visualization**
   - Interactive map (Folium or Leaflet)
   - Show property location (marker)
   - Show Class A streams (blue lines)
   - Show public access points (green markers)
   - Display distance measurement

6. **Results Display**
   - Text summary: "Nearest Class A public access: X.X miles"
   - Map with all elements
   - Export map as HTML

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

- Centre County
- Clinton County  
- Lycoming County
- (Other PA counties in future versions)

---

## Explicitly OUT OF SCOPE for v1.0

**Features deferred to v2.0+:**

- Driving distance/turn-by-turn directions
- Multiple address batch processing
- Other stream classifications (Naturally Reproducing, Approved)
- Additional PA counties beyond the initial 3
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
**Ship Date:** March 28, 2026 (Friday) - 5 weeks
**Kill Date:** April 4, 2026 (Friday) - 6 weeks

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

- [ ] GeoPandas installed and working
- [ ] PA stream data loaded in test script
- [ ] First test passing
- [ ] UNKNOWNS.md updated with findings

### Week 2-3 (Feb 28 - Mar 13): Core Development

#### Phase 2: TDD Development

- Data loading functions
- Geocoding integration
- Distance calculation
- Public access identification

**Deliverables:**

- [ ] Address geocoding works
- [ ] Stream data loads for 3 counties
- [ ] Distance calculation tested
- [ ] 5+ tests passing

### Week 4 (Mar 14-20): Integration & Mapping

- Map visualization
- Streamlit interface
- Full workflow integration
- Error handling

**Deliverables:**

- [ ] Map displays correctly
- [ ] End-to-end workflow works
- [ ] Integration tests passing

### Week 5 (Mar 21-28): Polish & Ship

#### Phase 3: Documentation & Sharing

- Code cleanup
- README with setup instructions
- ADRs written
- Demo materials
- LinkedIn post

**Deliverables:**

- [ ] README tested by someone else
- [ ] 2-3 ADRs complete
- [ ] Demo screenshot/video
- [ ] v1.0 tagged and pushed
- [ ] Shared publicly

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

**Why These Counties:**

- Centre: Familiar area, good data quality
- Clinton: Kettle Creek (legendary waters)
- Lycoming: Pine Creek (quality streams)
- Good geographic spread for testing
- All have State Game Lands for public access

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
3. More PA counties
4. Batch address processing
5. Property boundary integration
6. Saved searches
7. Mobile-responsive UI
8. Performance optimization

**Separate private tool (future project):**

- Properties containing streams (not just access)
- Private repo for personal use
- Built using learnings from this project
- Ethical considerations documented

---

## Project Repository Structure

```markdown
trout-stream-evaluator/
├── PROJECT-DEFINITION.md (this file)
├── UNKNOWNS.md
├── FUTURE.md
├── daily-log.md
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   └── adr/
│       ├── 001-tech-stack.md
│       ├── 002-distance-calculation.md
│       └── 003-public-access-approach.md
├── src/
│   ├── geocoding.py
│   ├── stream_data.py
│   ├── distance_calc.py
│   └── app.py (Streamlit)
├── tests/
│   ├── test_geocoding.py
│   ├── test_stream_data.py
│   └── test_distance_calc.py
└── data/ (gitignored, local only)
    ├── streams/
    └── public_access/
```

---

## Commitment Statement

I commit to:

- Following the project kickoff framework
- Time-boxing research to 4 hours
- Working 8-10 hours per week
- Weekly check-ins and progress sharing
- Shipping by March 28 or killing by April 4
- No exceptions, no extensions beyond kill date

Signed: [Your name]
Date: February 21, 2026

---

**Status: READY TO BEGIN**
**Next Step: Phase 1 Research (Week of Feb 24-27)**
