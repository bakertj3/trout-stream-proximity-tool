# ADR-003: Geographic Scope

## Status

Accepted

## Context

Original planned scope for app was to limit geographic distance calculations to 3 Pennsylvania counties with high quality Class A trout streams - Centre, Clinton, and Lycoming.

Options evaluated:

- limit Class A stream geojson dataset to only records in Centre, Clinton, and Lycoming counties, then calculate distance to closest stream
- calculate stream proximity across the entire PA geojson dataset rather than filtering first

## Decision

Decision made to calculate stream proximity across entire PA geojson dataset without county filtering

## Rationale

Calculating stream proximity across the entire state was preferred based on the following factors:

- The statewide GeoJSON dataset was already available and complete, requiring no additional filtering logic to subset by county.
- Calculating distance across the entire dataset was simpler and more accurate than filtering by county first.
- If limiting to a subset of PA counties, it would be possible for the nearest stream to actually be located in a neighboring county, which would be masked due to the county filtering.

## Consequences

- Users do not get results filtered to the county the address is located in.  
- Users are shown the actual closest stream even if it is not in the same county as the input address.
