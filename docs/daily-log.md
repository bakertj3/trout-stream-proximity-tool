# Daily Logs

## Session 1 - 2/24/2026 - 30min - Complete

- decided on GeoPandas as GIS tool
- installed GeoPandas in python library

---

## Session 2 - 2/25/2026 - 30 min - Complete

- found PA Fish & Boat GIS API url
- confirmed that Access data exists in same API (different layer)
- documented findings in UNKNOWNS.md

---

## 2/27/26 - Session 3

### Plan

**Goal:** GeoPandas Hello world + First Test
**Time:** 90 min

### What I Did

- attempted to follow along with GeoPandas Introduction
- troubleshooting python environments
- wrote hello_world.py
- wrote test_hello_world.py

### What Worked

- test passing
- plot displayed

### What Blocked Me

- python environment setup / venv setup

### Parked Ideas

- troubleshoot venv setup with uv

### Next Session

**Focus:** [Next test to write]

### Commit

a67e22c2c5e73240b2cea9b58d8c9afb11fc4fff

---

## 2/28/26 - Session 4 (120 min)

### Plan

**Goal:** Prove PA data loads and distance calculation works
**Time:** 90 min (+15 min extension)

### What I Did

- Fixed Python import issues (`src/__init__.py>`)
- Loaded PA Class A stream GeoJSON data
- Implemented county filtering
- Learned CRS/projection concepts
- Implemented proper geodesic distance using UTM Zone 18N
- All tests passing!

### What Worked

- Chose "Option B" - proper geodesic distance calculation
- GeoPandas .to_crs() for reprojection
- Found stream 1.17 miles from State College test point

### What I Learned

- Geographic vs Projected CRS
- UTM Zone 18N for Pennsylvania
- Why degrees don't work for distance
- GeoPandas spatial operations

### Next Session

**Focus:** Sunday review, then start Week 2 development

### Commit

e0fc9a79e6bcea91bed52b129d92f14ca0778c22
