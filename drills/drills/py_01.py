report = {"serious": "1"}

report["serious"]
report.get("occurcountry")

patient = report.get("patient") or {}
reactions = patient.get("reaction") or []

terms = [r["reactionmeddrapt"] for r in reactions if "reactionmeddrapt" in r]
unique = set(terms)
"NAUSEA" in unique

if not reactions:
    print("Geen reacties")

print(terms)
print(unique)
print("NAUSEA" in unique)

