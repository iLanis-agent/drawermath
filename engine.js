(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function slidePlan(openingMm, setBackMm) {
    if (!(openingMm > 0)) return { error: "the opening depth must be positive" };
    if (!(setBackMm >= 0)) return { error: "the set-back cannot be negative" };
    var usable = round1(openingMm - setBackMm);
    if (!(usable > 0)) return { error: "the set-back takes the whole opening" };
    var verdict;
    if (usable < 300) verdict = "a shallow drawer";
    else if (usable < 500) verdict = "a standard drawer";
    else verdict = "a deep drawer";
    return { usable: usable, verdict: verdict };
  }

  function frontPlan(widthMm, heightMm, gapMm) {
    if (!(widthMm > 0) || !(heightMm > 0)) return { error: "the opening width and height must be positive" };
    if (!(gapMm >= 0)) return { error: "the gap cannot be negative" };
    var frontW = round1(widthMm - 2 * gapMm);
    var frontH = round1(heightMm - 2 * gapMm);
    if (!(frontW > 0) || !(frontH > 0)) return { error: "the gaps take the whole opening" };
    var verdict;
    if (frontW < 300) verdict = "a narrow front";
    else if (frontW < 600) verdict = "a standard front";
    else verdict = "a wide front";
    return { frontW: frontW, frontH: frontH, verdict: verdict };
  }

  function stackPlan(cabinetMm, drawers, gapMm) {
    if (!(cabinetMm > 0)) return { error: "the cabinet height must be positive" };
    if (!(drawers >= 1) || Math.floor(drawers) !== drawers) return { error: "the drawer count must be a whole number, one or more" };
    if (!(gapMm >= 0)) return { error: "the gap cannot be negative" };
    var frontH = round1((cabinetMm - (drawers + 1) * gapMm) / drawers);
    if (!(frontH > 0)) return { error: "the gaps take the whole cabinet" };
    var verdict;
    if (frontH < 150) verdict = "shallow fronts, good for cutlery and linens";
    else if (frontH < 300) verdict = "standard fronts, good for clothes";
    else verdict = "deep fronts, good for pots and bulk";
    return { frontH: frontH, verdict: verdict };
  }

  function renderSlide(r, openingMm, setBackMm) {
    return "An opening " + openingMm + " mm deep with a labeled " + setBackMm + " mm set-back leaves " + r.usable + " mm for the box and slides - " + r.verdict + ".";
  }

  function renderFront(r, widthMm, heightMm, gapMm) {
    return "An opening " + widthMm + " mm x " + heightMm + " mm with a labeled " + gapMm + " mm gap each side takes a front " + r.frontW + " mm x " + r.frontH + " mm - " + r.verdict + ".";
  }

  function renderStack(r, cabinetMm, drawers, gapMm) {
    return "A cabinet " + cabinetMm + " mm tall with a labeled " + gapMm + " mm gap around " + plural(drawers, "drawer") + " leaves fronts " + r.frontH + " mm tall - " + r.verdict + ".";
  }

  var api = { slidePlan: slidePlan, frontPlan: frontPlan, stackPlan: stackPlan, renderSlide: renderSlide, renderFront: renderFront, renderStack: renderStack };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.DrawerMath = api;
})(this);
