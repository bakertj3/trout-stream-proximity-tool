# Trout Stream Proximity Tool - 5-Week Execution Plan

**Start Date:** February 21, 2026 (Friday)
**Ship Date:** April 24, 2026 (Friday)
**Kill Date:** May 1, 2026 (Friday)

**Note:** Week-by-week plan below will be revised iteratively during Sunday reviews based on learning pace and areas needing deeper exploration.

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

### Wednesday, Feb 25 - Session 2 (30 min) - COMPLETE

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

### Friday, Feb 27 - Session 3 (90 min) - COMPLETE

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

- [x] GeoPandas installed
- [x] Hello world code committed
- [x] First test passing

**If stuck >90 min:** Ask me for help immediately

---

### Saturday/Sunday, Feb 28/Mar 1 - Session 4 (90 min) - COMPLETE

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

- [x] PA stream data loaded successfully
- [x] Can filter by county
- [x] Can calculate basic distance
- [x] Go/No-Go decision made

**If this doesn't work in 90 min:** STOP. Ask me for help before proceeding.

---

### Sunday, Mar 1 - Weekly Review (30 min) - COMPLETE

**Review questions:**

1. Did I complete Phase 1 research in 4 hours?
2. Can I load PA stream data?
3. Does GeoPandas work?
4. Am I ready to start development?

**Decision:**

- [x] GO: Proceed to Week 2 development
  - ***Post Week 1 sessions will be planned week-by-week during Sunday reviews based on learning progress***
- [ ] PIVOT: Adjust approach (simpler tool?)
- [ ] KILL: Document learnings, move on

### Update PROJECT-DEFINITION.md if scope changed

#### Share dev log in our chat

---

## Week 2 Plan (March 3-8)

### Tuesday, March 3 - Session 5 (90 min)

**Focus:** Pandas Fundamentals

**Structure:**

- Part 1 (45 min): Structured exercises with coaching
  - DataFrame basics (load, inspect, access columns)
  - Filtering & boolean indexing
  - Common operations (count, group, sort)
- Part 2 (45 min): Exploratory work with real PA stream data
  - Trevor tries exercises for 5-10 min each
  - Then coaching begins with hints/questions
  - Build personal cheat sheet as he goes

**Deliverable:** Pandas cheat sheet in Trevor's own words

### Wednesday, March 4 - Session 6 (90 min)

**Focus:** Workflow Mapping & Development Roadmap

**Goals:**

- Map complete end-to-end workflow (address → distance calculation)
- Break into logical, testable chunks
- Identify what Pandas/GeoPandas knowledge each chunk needs
- Create roadmap for development
- Understand "next smallest test" strategy for each piece

**Deliverable:** Visual workflow map + development roadmap document

### Friday, March 6 - Session 7 (90 min)

**Focus:** TDD work on first workflow piece

- With roadmap in hand, choose first piece to implement
- Trevor writes tests with coaching guidance
- Practice "next smallest test" methodology
- Focus on test structure/formatting

### Saturday/Sunday, March 7-8 - Session 8 (2 hours)

**Focus:** Continue TDD development

- Build on Friday's work
- Practice test-first development with real project code
- Refine understanding of when to write next test

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
