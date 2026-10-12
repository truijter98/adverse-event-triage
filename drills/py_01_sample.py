import json
import pathlib

reports = json.loads(pathlib.Path("drills/sample.json").read_text())
print(len(reports), "meldingen")

#1 Hoeveel meldingen zijn ernstig?
serious = 0
for report in reports:
    if report.get("serious") == "1":
        serious += 1

print(serious, "ernstig")

#2 Alle unieke reactietermen over alle vijf, in een set
unique = set()
for report in reports:
    patient = report.get("patient") or {}
    reactions = patient.get("reaction") or []
    for r in reactions:
        term = r.get("reactionmeddrapt")
        if term:
            unique.add(term)
print(len(unique), "Unieke termen")
print(unique)


#3 De melding met de meeste reacties (max met key=)
def n_reactions(report):
    patient = report.get("patient") or {}
    return len(patient.get("reaction") or [])

biggest = max(reports, key=n_reactions)
print("meeste reacties:", n_reactions(biggest), "in melding", biggest.get("safetyreportid"))
