# Drawer math

Drawer math plans the drawer before the build: the opening depth minus a
labeled set-back becomes the room for the box and slides, the opening size
minus a labeled gap each side becomes the front size, and the cabinet height
minus labeled gaps, shared by the drawer count, becomes equal front heights.

Live site: https://ilanis-agent.github.io/drawermath/

## The three tools

- **Slide plan** - `opening depth - labeled set-back (25 mm)`, the usable
  depth for box and slides, with a shallow / standard / deep verdict.
- **Front plan** - `opening - 2 x labeled gap (3 mm)` in each dimension, the
  front size, with a narrow / standard / wide verdict.
- **Stack plan** - `(cabinet - (drawers + 1) x labeled gap) / drawers`, equal
  front heights, with a use-band verdict.

## Limits

Every default is labeled and illustrative. Openings are never perfectly
square and hardware makers rate their own slides. This is planning
arithmetic, not joinery instruction: measure the real opening and check the
slide maker's sheet.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (32 cases, 130 checks)

Run the tests: `python3 oracle.py && node test.js`
