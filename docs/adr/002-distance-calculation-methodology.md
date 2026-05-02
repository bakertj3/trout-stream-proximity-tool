# ADR-002: Distance Calculation Method

## Status

Accepted

## Context

The Trout Stream Proximity Tool needs to return a calculated value to the user that defines the distance between the input address and the nearest Class A Trout Stream

Options considered:

- Straight line distance
- Driving distance

## Decision

Straight line distance was chosen as the method for stream proximity distance.

## Rationale

Straight line distance was chosen for several reasons:

- Driving distance would involve another API to calculate driving distance
- Aiming for 'minimum viable product' scope led to choosing straight line distance method for simplicity

UTM reprojection was implemented in order to ensure accuracy of distance calculations.  Local UTM zones ensure that map distortion is minimized for the locality by projecting a smaller area of the earth to a flat plane for calculating distances.  UTM uses meters as units, which are highly accurate for this purpose.

## Consequences

Users could be displayed a stream that is not the closest considering driving distance. Users could also be displayed a stream that does not have useful access points because distance is as-the-crow-flies.
