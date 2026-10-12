#Adverse Event Triage

Can the seriousness classification of an FDA adverse event report be predicted from the report's own conetent -- and what does ti mean if it can?

built to learn data science end to end on real pharmacovigilance data: ingestion, flattening, honest evaluation, calibration, and a comparison against the disproportionality methods (PRR, ROR) that pharmacovigilance has used for decades.

Data
openFDA druge/event (FAERS). Public, unvalidated, spontaneous reports. 

Stack
Python, httpx, polars, DuckDB, scikit-leanr, matplotlib, uv.

Status
week 1 of 12