import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def slide_plan(openingMm, setBackMm):
    if not (openingMm > 0):
        return {"error": "the opening depth must be positive"}
    if not (setBackMm >= 0):
        return {"error": "the set-back cannot be negative"}
    usable = round1(openingMm - setBackMm)
    if not (usable > 0):
        return {"error": "the set-back takes the whole opening"}
    if usable < 300: verdict = "a shallow drawer"
    elif usable < 500: verdict = "a standard drawer"
    else: verdict = "a deep drawer"
    return {"usable": usable, "verdict": verdict}

def front_plan(widthMm, heightMm, gapMm):
    if not (widthMm > 0) or not (heightMm > 0):
        return {"error": "the opening width and height must be positive"}
    if not (gapMm >= 0):
        return {"error": "the gap cannot be negative"}
    frontW = round1(widthMm - 2 * gapMm)
    frontH = round1(heightMm - 2 * gapMm)
    if not (frontW > 0) or not (frontH > 0):
        return {"error": "the gaps take the whole opening"}
    if frontW < 300: verdict = "a narrow front"
    elif frontW < 600: verdict = "a standard front"
    else: verdict = "a wide front"
    return {"frontW": frontW, "frontH": frontH, "verdict": verdict}

def stack_plan(cabinetMm, drawers, gapMm):
    if not (cabinetMm > 0):
        return {"error": "the cabinet height must be positive"}
    if not (drawers >= 1) or math.floor(drawers) != drawers:
        return {"error": "the drawer count must be a whole number, one or more"}
    if not (gapMm >= 0):
        return {"error": "the gap cannot be negative"}
    frontH = round1((cabinetMm - (drawers + 1) * gapMm) / drawers)
    if not (frontH > 0):
        return {"error": "the gaps take the whole cabinet"}
    if frontH < 150: verdict = "shallow fronts, good for cutlery and linens"
    elif frontH < 300: verdict = "standard fronts, good for clothes"
    else: verdict = "deep fronts, good for pots and bulk"
    return {"frontH": frontH, "verdict": verdict}

def render_slide(r, openingMm, setBackMm):
    return ("An opening " + fmt(openingMm) + " mm deep with a labeled " + fmt(setBackMm) + " mm set-back leaves "
            + fmt(r["usable"]) + " mm for the box and slides - " + r["verdict"] + ".")

def render_front(r, widthMm, heightMm, gapMm):
    return ("An opening " + fmt(widthMm) + " mm x " + fmt(heightMm) + " mm with a labeled " + fmt(gapMm)
            + " mm gap each side takes a front " + fmt(r["frontW"]) + " mm x " + fmt(r["frontH"]) + " mm - " + r["verdict"] + ".")

def render_stack(r, cabinetMm, drawers, gapMm):
    return ("A cabinet " + fmt(cabinetMm) + " mm tall with a labeled " + fmt(gapMm) + " mm gap around "
            + plural(drawers, "drawer") + " leaves fronts " + fmt(r["frontH"]) + " mm tall - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[500,25],[400,25],[600,25],[250,25],[525.5,25],[0,25],[500,-5],[20,25],[500,0],[299,25]]:
    add("slidePlan", slide_plan, render_slide, a)
for a in [[400,300,3],[600,200,3],[250,150,3],[800,250,2],[305.5,200.5,3],[0,300,3],[400,0,3],[400,300,-1],[5,5,3],[596,300,3]]:
    add("frontPlan", front_plan, render_front, a)
for a in [[720,3,3],[500,4,3],[900,3,3],[600,2,3],[720,1,3],[0,3,3],[720,0,3],[720,2.5,3],[720,3,-1],[9,3,3],[600,5,3],[450.5,3,3]]:
    add("stackPlan", stack_plan, render_stack, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
