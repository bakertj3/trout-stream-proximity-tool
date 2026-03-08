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
55955c69489199f3465f9b7404d1ee5eab6863bd

## 3/1/2026 (Sunday) - Week 1 Review

### what happened

- started week one proof-of-concept setup with GeoPandas, PA Stream GIS Data
- wrote Hello World test for GeoPandas using the nybb dataset
- wrote a basic proximity/distance calculation using a lat/lng point to the nearest Class A trout stream in Centre county

### what I learned

- I want to own more of the code and not copy/paste from Claude
- Pandas/GeoPandas is a powerful framework tool that might have application for my professional work, but there is a learning curve to traverse in getting to a useful working knowledge of the tools.  I want to understand how to do common operations so I'm not relying on Claude to provide the code needed for each development step.
- The timeline needs to be adjusted in order to dig in to learning a bit more than originally expected.  Extending timeline by 3-4 weeks accordingly.

### what's next

- Next session I will dig into Pandas and take a dive into concepts, functionality, and application of the tool.
- Each week, I will complete my Sunday weekly review and choose what the next week's plan is based on where the learning/work for the week landed.

## 3/3/2026 - 3/6/26 - Session 5

### Plan

- pivoted timeline plan based on desire to own the decisions and code instead of leveraging AI for code
- learn the Pandas framework basics
- document knowledge learned in docs/PANDAS-CHEATSHEET.md

### What happened

- created fake stream DataFrame to learn complete Pandas orientation
  - topics:
    - DataFrame properties
    - basic DataFrame filtering
    - sorting and aggregation to return desired data
- used Class A Trout Streams.geojson to further learning on real dataset
  - topics:
    - dataset characteristics
    - returning stream information (names, lengths, etc)
    - filtering & returning data (longest stream name, streams with "creek" in the name, county with most streams)

### What I learned

- Better familiarity with pandas syntax
- Found that I was overcomplicating a lot of the querying
- learned about the pd.json_normalize function for flattening nested dictionary data (useful for streams dataset!)

### What's next

- next session: workflow mapping

## 3/7/26 - Session 6

### Plan

- map workflow to understand all the big picture of the MVP app fucntionality
- quantify steps in the app flow for better understanding of functionality needed for TDD development

### What happened

- Leveraged Claude as coach to help guide me through working out the basic framework of what the app does
- Decided to use Folium for map display because it works seamlessly with GeoPandas and has minimal features (good for v1.0)
- Decided to leverage stream data local to the app for speed & simplicity over API calls
- Worked out overall flow of app

### What I learned

- Pros/cons of Folium, Plotly & Leaflet.js for Map display
- full flow of app
  1. User inputs address
  2. Geocode address → lat/lng
  3. Load local Class A stream data
  4. Calculate distance from lat/lng to each stream
  5. Return nearest stream(s)
  6. Display results + Folium map showing location and stream

### What's next

- Research geocoding options (Census bureau vs Google API)
- Pick a geocoding option
- write first test for geocoding
