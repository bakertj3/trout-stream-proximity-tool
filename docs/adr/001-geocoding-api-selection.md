# ADR-001: Geocoding API Selection

## Status

Accepted

## Context

The Trout Stream Proximity Tool needs to convert an address to a geocoded Lat/Lng position to evaluate proximity to PA Fish & Boat geojson stream data.

Evaluated options:

- Google Maps Geocoding API
- US Census Address API

## Decision

Google Maps Geocoding API was chosen as the geocoding platform

## Rationale

Google Maps Geocoding API was chosen based on these factors:

    - The Google Maps Geocoding API is more accurate than the US Census API for rural addresses
    - The Developer already had a Google developer account
    - The cost for using the geocoding API would be low for this project's consumption
    - Google products are generally well-documented and easy to use

## Consequences

Users of this app must have a Google Developer account with a payment method on file and a valid Geocoding API key. The API key must be stored in a `.env` file in the project root.
