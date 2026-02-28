# Trout Stream Proximity Tool - 5-Week Execution Plan

**Start Date:** February 21, 2026 (Friday)
**Ship Date:** March 28, 2026 (Friday)
**Kill Date:** April 4, 2026 (Friday)

---

## Your Weekly Schedule

**Monday, Wednesday, Friday:** 90-minute dev sessions (6:30-8pm? Your choice)
**Saturday OR Sunday:** 2-hour focused session
**Sunday Evening:** 30-minute weekly review

**Total:** 8-10 hours per week

---

## Week 1: Feb 23-Mar 1 (Research & Setup)

***Phase 1: Time-Boxed Research (4 hours MAX)***

### Tuesday, Feb 24 - Session 1 (30 min)

**Goal:** Decide on GIS library

**Tasks:**

1. Set 30-minute timer
2. Google: "python gis analysis comparison"
3. Read: GeoPandas overview page
4. Ask me: "Compare GeoPandas vs PostGIS for Python GIS beginner"
5. Fill out decision table in UNKNOWNS.md
6. **Make decision when timer ends**

**Output:**

- [x] Decision documented in UNKNOWNS.md
- [x] Ready to install chosen library

---

### Wednesday, Feb 25 - Session 2 (30 min)

**Goal:** Verify PA data exists and is accessible

**Tasks:**

1. Set 30-minute timer
2. Go to: <https://gis.pfbc.pa.gov/>
3. Find Class A Wild Trout layer
4. Check if you can export/access data
5. Search for public access point data
6. Document findings in UNKNOWNS.md
7. **When timer ends, move forward with what you found**

**Output:**

- [x] Data source URLs documented
  - <https://mapservices.pasda.psu.edu/server/rest/services/pasda/PAFishBoat/MapServer>
- [x] Know whether public access data exists
- [x] Identified fallback if needed

---

### Friday, Feb 27 - Session 3 (90 min)

**Goal:** Get GeoPandas working with hello world

**Tasks:**

1. Set 90-minute timer
2. Install GeoPandas: `pip install geopandas`
3. Follow official quickstart tutorial
4. Load built-in world dataset
5. Print basic info about it
6. Write one test that it loads
7. Commit code

**Code to try:**

```python
import geopandas as gpd
from geodatasets import get_path

# Load example data
world = gpd.read_file(get_path("nybb")

# Print info
print(f"Loaded {len(world)} boroughs")
print(world.head())

# Success!
```

**Output:**

- [ ] GeoPandas installed
- [ ] Hello world code committed
- [ ] First test passing

**If stuck >90 min:** Ask me for help immediately

---

### Saturday/Sunday, Feb 28/Mar 1 - Session 4 (90 min)

**Goal:** Prove you can load PA stream data

**Tasks:**

1. Set 90-minute timer
2. Download/access PA Class A stream data
3. Load it with GeoPandas
4. Filter to Centre County
5. Calculate distance from a test point to nearest stream
6. Document what worked/didn't in UNKNOWNS.md

**Test point to use:**

- State College, PA: 40.7934° N, 77.8600° W

**Output:**

- [ ] PA stream data loaded successfully
- [ ] Can filter by county
- [ ] Can calculate basic distance
- [ ] Go/No-Go decision made

**If this doesn't work in 90 min:** STOP. Ask me for help before proceeding.

---

### Sunday, Mar 1 - Weekly Review (30 min)

**Review questions:**

1. Did I complete Phase 1 research in 4 hours?
2. Can I load PA stream data?
3. Does GeoPandas work?
4. Am I ready to start development?

**Decision:**

- [ ] GO: Proceed to Week 2 development
- [ ] PIVOT: Adjust approach (simpler tool?)
- [ ] KILL: Document learnings, move on

### Update PROJECT-DEFINITION.md if scope changed

#### Share dev log in our chat

---

## Week 2: Mar 3-8 (Core Development Begins)

### Phase 2: TDD Development

### Tuesday, Mar 3 - Session 5 (90 min)

**Goal:** First real test - load stream data

**Write this test:**

```python
def test_can_load_class_a_streams():
    """Can we load PA Class A stream data?"""
    streams = load_class_a_streams()
    assert streams is not None
    assert len(streams) > 0
    assert 'geometry' in streams.columns
```

**Make it pass:**

- Implement `load_class_a_streams()` function
- Load PA data
- Return GeoDataFrame

**Output:**

- [ ] Test passing
- [ ] Code committed
- [ ] Daily log updated

---

### Wednesday, Mar 4 - Session 6 (90 min)

**Goal:** Filter streams by county

**Write this test:**

```python
def test_filter_streams_by_county():
    """Can we filter streams to specific counties?"""
    streams = load_class_a_streams()
    centre_streams = filter_by_counties(streams, ['Centre'])
    assert len(centre_streams) > 0
    # All streams should be in Centre County
```

**Make it pass:**

- Implement county filtering
- Test with Centre, Clinton, Lycoming

**Output:**

- [ ] Test passing
- [ ] County filtering works
- [ ] Committed

---

### Friday, Mar 6 - Session 7 (90 min)

**Goal:** Geocoding - address to coordinates

**Write this test:**

```python
def test_geocode_pa_address():
    """Can we convert PA address to lat/lng?"""
    lat, lng = geocode_address("123 Main St, State College, PA")
    assert lat is not None
    assert lng is not None
    assert 39 < lat < 43  # Roughly PA latitude range
    assert -81 < lng < -74  # Roughly PA longitude range
```

**Make it pass:**

- Choose geocoding service (Census or Google)
- Implement `geocode_address()` function
- Handle errors

**Output:**

- [ ] Geocoding works
- [ ] Test passing
- [ ] Committed

---

### Saturday/Sunday, Mar 7-8 - Session 8 (2 hours)

**Goal:** Distance calculation

**Write this test:**

```python
def test_find_nearest_stream():
    """Can we find nearest stream to a point?"""
    streams = load_class_a_streams()
    lat, lng = 40.7934, -77.8600  # State College
    
    nearest_stream, distance_miles = find_nearest_stream(streams, lat, lng)
    
    assert nearest_stream is not None
    assert distance_miles > 0
    assert distance_miles < 50  # Sanity check
```

**Make it pass:**

- Calculate geodesic distance
- Find minimum distance
- Return stream info and distance

**Output:**

- [ ] Distance calculation works
- [ ] Test passing
- [ ] Committed

---

### Sunday, Mar 8 - Weekly Review (30 min)

**Progress check:**

- [ ] 4+ tests passing
- [ ] Core functions working
- [ ] On track for Week 3 goals

**If behind:** Cut scope, reduce features

- [ ] **Share dev log in our chat**

---

## Week 3: Mar 9-15 (Integration)

### Tuesday, Mar 10 - Session 9 (90 min)

**Goal:** Public access point identification

**Tasks:**

- Load public access data (or State Game Lands)
- Filter to public-accessible stream segments
- Test finding nearest PUBLIC access

---

### Wednesday, Mar 11 - Session 10 (90 min)

**Goal:** End-to-end integration test

**Write this test:**

```python
def test_full_workflow():
    """Complete workflow: address → analysis → results"""
    result = analyze_property("456 Oak St, Bellefonte, PA")
    
    assert result['nearest_class_a_miles'] is not None
    assert result['property_coords'] is not None
    assert result['stream_name'] is not None
```

**Make it pass:**

- Integrate all functions
- Return structured result

---

### Friday, Mar 13 - Session 11 (90 min)

**Goal:** Error handling

**Write tests for:**

- Invalid address
- Address outside PA
- No streams nearby

- **Make robust**

---

### Saturday/Sunday, Mar 14-15 - Session 12 (2 hours)

**Goal:** Map visualization prototype

**Tasks:**

- Create basic Folium map
- Add property marker
- Add stream lines
- Display in notebook/script first

---

### Sunday, Mar 15 - Weekly Review (30 min)

**Progress check:**

- [ ] Integration working
- [ ] Error handling added
- [ ] Map displays
- [ ] Ready for UI

- [ ] **Share dev log**

---

## Week 4: Mar 16-22 (UI & Polish)

### Tuesday, Mar 17 - Session 13 (90 min)

**Goal:** Streamlit app skeleton

**Create:**

- Text input for address
- Button to analyze
- Display results area

---

### Wednesday, Mar 18 - Session 14 (90 min)

**Goal:** Integrate map into Streamlit

**Tasks:**

- Display Folium map in Streamlit
- Show results text
- Handle loading states

---

### Friday, Mar 20 - Session 15 (90 min)

**Goal:** Polish UI

**Tasks:**

- Better layout
- Error messages
- Loading indicators
- Instructions

---

### Saturday/Sunday, Mar 21-22 - Session 16 (2 hours)

**Goal:** Code cleanup

**Tasks:**

- Remove debug prints
- Add docstrings
- Clean git history
- One cleanup pass

---

### Sunday, Mar 22 - Weekly Review (30 min)

**Progress check:**

- [ ] App works end-to-end
- [ ] Ready for documentation
- [ ] On track to ship Friday

- [ ] **Share dev log**

---

## Week 5: Mar 23-29 (Documentation & Ship)

### Tuesday, Mar 24 - Session 17 (90 min)

**Goal:** README.md

**Create:**

- Problem statement
- Setup instructions
- Usage examples
- Screenshots

**Test:** Have someone follow your README

---

### Wednesday, Mar 25 - Session 18 (90 min)

**Goal:** Write ADRs

**Create 2-3 ADRs:**

1. `001-tech-stack-selection.md`
2. `002-distance-calculation-approach.md`
3. `003-public-access-methodology.md`

Use ADR template

---

### Friday, Mar 27 - Session 19 (2 hours)

#### SHIP DAY

**Tasks:**

1. Final testing
2. Tag v1.0 release
3. Push to GitHub
4. Take screenshots
5. Write LinkedIn post
6. Share it!

**LinkedIn post template:**

```text
I just shipped Trout Stream Proximity Tool! 🎣

This tool helps property hunters in Pennsylvania assess proximity to Class A wild trout waters using GIS analysis.

Built with Python, GeoPandas, and Streamlit, this was my first project using spatial data analysis. Key technical challenge: integrating PA Fish & Boat Commission GIS data with geocoding to calculate distances to public fishing access.

I designed it with ethical considerations in mind - focusing on public access points to promote responsible fishing rather than enabling trespassing.

Check it out: [GitHub link]

#Python #GIS #SoftwareDevelopment #OpenSource
```

---

### Sunday, Mar 29 - Final Review (30 min)

**Reflection:**

- Write LESSONS_LEARNED.md
- Update resume
- Plan next project (or celebrate!)

- [ ] **Share final dev log**

---

## Emergency Procedures

### If You Get Stuck (>4 hours on same problem)

**STOP. Do this:**

1. Ask me for help with specific error
2. Search Stack Overflow
3. Try simpler approach
4. Skip feature if possible

***Don't stay stuck more than half a day***

---

### If You Fall Behind

**Week 2 behind?**

- Cut public access point feature
- Just distance to nearest stream
- Reduce scope

**Week 3 behind?**

- Skip fancy map features
- Basic map is fine
- Cut error handling niceties

**Week 4 behind?**

- Minimal Streamlit UI
- Command-line version OK
- Focus on shipping something

---

### If You Lose Motivation

**Check these:**

1. Is scope too big? → Cut features
2. Is it too hard? → Simplify approach  
3. Still care? → Yes: continue, No: kill it
4. New idea distracting? → Park it, finish this first

---

## Success Criteria

**You'll know you're succeeding when:**

**Week 1:**

- Research done in 4 hours
- First test passing
- Data loads successfully

**Week 2:**

- Multiple tests passing
- Core functions work
- Making steady progress

**Week 3:**

- Integration working
- Map displays
- Most features complete

**Week 4:**

- UI functional
- End-to-end demo works
- Almost shippable

**Week 5:**

- Documentation done
- SHIPPED on GitHub
- Shared publicly
- Celebrating!

---

## Daily Log Template

Copy this for each session:

```markdown
## [Date] - Session [N]

### Plan
**Goal:** [What you're trying to accomplish]
**Time:** 90 min

### What I Did
- 
- 
- 

### What Worked
- 

### What Blocked Me
- 

### Parked Ideas
- 

### Next Session
**Focus:** [Next test to write]

### Commit
[commit hash or "no commit today"]
```

---

## The Commitment

**I commit to:**

- Following this plan
- 8-10 hours per week
- Weekly check-ins
- Shipping by March 28
- Killing by April 4 if not shipped
- No exceptions

**Let's do this.**

---

**Next Action:** Start Tuesday, Feb 24 with Session 1 (30 minutes - GIS library decision)

**Before then:**

- Save all framework documents
- Create project directory
- Set up git repo
- Review this plan once more
