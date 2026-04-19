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

## 3/7/2026 - 3/8/2026 - Session 7

### What happened

- researched geocoding platform options - Census vs Google
- decided to use Google Maps Geocoding API
  - already have free developer account
  - Google's geocoding API is more accruate for rural addresses - relevant to class A trout streams
- wrote first test for invalid addresses, passes
- created .env file to store API key
- deleted existing google API key that was committed to GitHub in the open
- recreated a new API key, stored in .env

### What I learned

- I refreshed knowledge on how to store secrets in .env vars in python
- Learned what the output of Google's Geocoding API looks like
- Navigating nested JSON structures from API sources
- Learned how to assert raised exceptions for in python functions with pytest

### What's next

- Write next failing test for successful address geocode

## 3/8/2026 - Week 2 Review

### What happened

- Reviewed week wins and accomplishments
  - Focused learning on the Pandas framework
  - Workflow outline and planning
  - Compared geocoding APIs and decided on Google
  - Wrote first test for geocoding functionality
- Planned out Week 3 sessions & goals

### What I learned

- I jump to contingencies, edge cases, and user experience. Focusing on MVP is more difficult.
- I need to continue to ask "what is good enough for v1"
- Learned Pandas functionality and some simpler ways to calculate common data values
- Learned about Pros/Cons of Google & Census Bureau geocoding APIs

### What's next

- Week 3 (March 10-15) plan outline
  - Complete Geocoding (1-2 more tests)
  - Integration address -> lat/lng -> nearest stream distance
  - Start Folium map visualization

## 3/10/2026 - Session 8

### What happened

- wrote failing TDD tests for address_geocode
- made tests pass
- evaluated merits of binding geocoding to Pennsylvania only
- refactored address_geocode to load the API_Key only when module is loaded
- evaluated where the orchestration layer should reside
- decided that orchestration will reside in `src/proximity_analyzer.py` with main function `return_closest_stream()`

### What I learned

- learned about python design for orchestration layers and app vs main module focus
- discovered that python can assert inequalities in this format `assert 39 <= result["lat"] <= 43`
- furthered depth of TDD reasoning within python tests

### What's next

- write failing tests for `proximity_analyzer.py` module & `return_closest_stream()` function

## 3/12/2026 - 3/13/2026 - Session 9

### What happened

- worked through TDD incremental steps to implement functionality in `proximity_analyzer.py`
- wrestled with what to return for `return_closest_stream()` output
- couldn't figure out how to get the stream geometry into a dictionary format from the geometry series in the DataSeries

### What I learned

- continued to reinforce incremental TDD thinking through writing tests to get to code implementation

### What's next

- write next test for verifying stream geometry from nearest_stream object

## 3/14/2026 - Session 10

### What happened

- tried to verify type of stream geometry in a learning module `learning/geopandas_exercise_stream_data.py`
- struggled with importing directories in python project, found solution, adding to "What I learned" section
- Learned that stream line definitions in a GeoPandas series is an instance of t a Shapely object
- wrote final test for asserting geometry is a shapely BaseGeometry type
- Integration tests & implementation for orchestration layer complete
  
### What I learned

- add `[tools.setuptools] packages = ["src"]` to `pyproject.toml` to reference `src/` module from anywhere in project
  - run `uv pip install -e .` to install in editable mode for the project
  - NOTE: Editable install `-e .` tells python to treat project directory as an importable package without copying files
- Online docs are generally quickest for determining library/module class hierarchies

### What's next

- Explore Folium in `learning/` directory
- Determine what I need to convert Shapely stream geometry to Folium format
- write tests for the mapping

## 3/14/2026 - 3/15/2026 - Session 11

### What happened

- explored mapping in Folium using `learning/folium_map_basics.py`
- explored shapely datatypes, properties and functions
- discovered that geojson coordinates list [lng, lat] - folium needs [lat, lng]
- learned mapping lines and polygons in Folium

### What I learned

- Folium needs lat/lng coords in order [Lat, Lng]
- GeoJson files order the coordinates [Lng, Lat], so conversion will need to be done before mapping
- Shapely has functions to determine if shapes intersect, overlap, etc

### What's next

- begin writing tests for the mapping layer
  - need to ensure mapping uses folium's fit_bounds, but need to ensure that bounds are calulated encapsulating address and stream bounds
- use TDD for incremental development of mapping layer implementation

## 3/15/2026 - Week 3 review

### What happened

- Finished geocoding TDD
- Built orchestration layer (`proximity_analyzer.py`)
- Explored Folium/Shapely in `learning/`

### What I learned

- Python app architecture (orchestration layers)
- Inequality assertion syntax
- Editable install (`pip install -e .`)
- GeoJSON coordinate order (lng, lat)
- Shapely geometry types
- API doc navigation

### What's next

- Mapping layer tests (MultiLineString, bounds/zoom)
- Streamlit exploration if time allows
- Add session time tracking

## 3/18/2026, 3/21/2026, 3/22/2026 - Session 12

### Time tracking

- Sesion A: 3/18/2026 - 9:21p - 9:28p
- Session B: 3/18/2026 - 10:35p - 10:50p
- Session C: 3/21/2026 - 9:30a - 10:50a
- Session D: 3/21/2026 - 11:30a - 11:50a
- Session E: 3/22/2026 - 12p - 12:15p
- Session F: 3/22/2026 - 2:30p - 5:00p

### What happened

- established what a TDD test looks like for a framework like Folium
- looked up encoding a string into json string with json.JSONEncoder.encode()
  - didn't end up needing for test data arrangement
- wrote 3 tests with passing implementation
- discovered how to locate undocumented attributes of python libraries
- wrote 3 more tests with passing implementation, including mutlilinestring handling

### What I learned

- Classes in python follow PEP 8 naming conventions - classes => PascalCase (e.g., "ClassName")
- How to discover unpublished attributes of python frameworks/libraries:
  - use `dir(object)` to get a list of all attributes, public and private
  - Read library source code on GitHub or public repo
  - Search stack overflow for testing example code
  - Check library's own test files
- Learned similarities and differences in shapely's LineString and MultiLineString

### What's next

- write tests to cover map bounds and zoom for folium map object
- write tests to ensure there is stream information displayed on map object

## 3/22/2026 - Week 4 review

### What happened

- completed session 12 across 6 small timeblocks during the week
- Folium mapping layer TDD - 6 tests written & passing
- Practiced problem solving by referencing library documentation before asking Claude

### What I learned

- using dir(object) for inspecting a library's internals that may not be documented with the API
- Handling Linestring vs Multilinestring geometries
- PEP 8 Naming conventions (Pascal Case for classes)

### What's next

- Complete final tests for mapping layer (bounds/zoom, labeling)
- Verify end-to-end test with saved HTML map
- Start Streamlit UI exploration if time allows

## 3/24/2026 - Session 13

### Time tracking

- Sesion A: 3/24/2026 - 5:40p - 6:10p
- Session B: 3/24/2026 - 7:30p - 8:15p
- Session C: 3/26/2026 - 9:45p - 10:30p
- Session D: 3/27/2026 - 7:15a - 8:15a
- Session E: 3/28/2026 - 8:30a - 9:15a
- Session F: 3/28/2026 - 7:40p - 8:10
- Session G: 3/28/2026 - 9:20p - 10:20p
- Session H: 3/29/2026 - 1:10p - 2:10p

### What happened

- struggled through verifying that folium map bounds encompass objects added to the map
- discovered that folium automatically handles fitting map bounds tochild objects
- removed 2 tests written to verify that the map encompassed the address and the stream bounds
- wrote tests for verifying stream name is in tooltip and stream info is in popup of stream line
- added `Percent_PublicLand` variable to the output of `return_closest_stream()` in `proximity_analyzer.py` using a TDD approach

### What I learned

- Sometimes 3rd party platforms handle functionality that developer expects to have to implement in code.
- When documentation is not complete, learning what functionality exists in a library is only learned through discovery
- branca.element.Element - requires render() method to get actual html output to assert against
- learned how to limit decimal displays for float's f-strings - `{float:.3f}`

### What's next

- Explore Streamlit UI framework

## 3/29/2026 - Week 5 review

### What happened

- Completed mapping layer with information in tooltips and popups
- Ensured proper multiline handling in all of the test development
- Wrote tests to verify functionality that folium already covers by default
- Deleted tests that covered folium functionality because they didn't add anything to this project's code

### What I learned

- Test application code, not the framework code
- Discover python library functionality using dir() and reading source code
- `branca` rendering
- f-string float formatting

### What's next

- Streamlit UI exploration, tests, implementation

## 4/1/2026 - Session 14

### Time Tracking

- Session A: 4/5/2026 - 9:25a - 9:40a
- Session B: 4/5/2026 - 11:00a - 11:15a
- Session C: 4/5/2026 - 12:00p - 12:15p

### What Happened

- Installed streamlit in project
- Investigated built in app testing in Streamlit

### What I learned

- Streamlit has its own test framework

### What's next

## 4/11/2026, 4/12/2026 - Session 15

### Time Tracking

- 4/11/2026 - 9:45a - 10:30a
- 4/12/2026 - 2:20p - 2:50p
- 4/12/2026 - 6:00p - 6:15p
- 4/13/2026 - 9:30a - 10:45a
- 4/14/2026 - 9:45p - 10:15p

### What happened

- Wrote 4 tests for the streamlit app
- all 4 tests passing

### What I learned

- Learned about how to mock with unittest.mock, specifically `patch()` as a decorator for the test methods
- Learned that Folium display in streamlit is helped by using the streamlit-folium library

### What's next

- write several more tests for the streamlit app to verify functionality of map display

## 4/19/2026 - Week 6-8 Review

### Time tracking

- 4/19/2026 - 9:15a - 11:15a
  
### What happened

- started project review of past 2-3 weeks to establish plan to meet launch deadline
- ran app in streamlit to evaluate current state
- fix streamlit map rendering issues
- removed 1 test that was essentially testing the streamlit framework, not my code

### What I learned

- map rendering is good enough
- some javascript blocking caused the streamlit app to not render address markers from CDN
- streamlit `on_click` callback should reference the function name.  if method defined as `on_click="Function_Name()"` the function will be called whent the app renders

### What's next

- get stream distance to display on app in text only    
- update README.md with actual install instructions
- update PROJECT-DEFINITIONS.md with pivots made during development
- tag release on GitHub
