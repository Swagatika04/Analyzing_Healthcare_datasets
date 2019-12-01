## **Wrangling Hospital Encounter**  **datasets**

In this exercise, I evaluated, built a cohort of patients and calculated some metrics related to that cohort.

**Part 1: Assembling the project cohort:** The goal is to identify patients seen in the emergency department with anaphylaxis or allergic reactions, determine if they had an order for epinephrine, and if they had a follow up outpatient visit after their emergency department visit.The task was to assemble the study cohort by identifying encounters that meet the following criteria: Hospital Encounter, occurred after August 1, 2014, age between 1-18 **,** and the patient received an Emergency Department diagnosis of anaphylaxis or allergic reaction, identified by certain ICD9 Codes. Also, one of the criteria was that the encounter was not at an Urgent Care department.

**Part 2: Creating Additional Fields:** With my anaphylaxis and allergic reaction cohort, I created the following indicators:

1. ANAPH\_DX\_IND: 1 if the encounter has at least one diagnosis where the text of diagnosis name contains the word &#39;anaphylaxis&#39;, 0 if it does not
2. EPI\_ORDER\_IND: 1 if the encounter had at least one medication order name (med\_ord\_nm) where the text of the medication name contains the word &#39;epinephrine&#39;, 0 if they did not
3. FOLLOW\_UP\_IND: 1 if the patient was seen for an outpatient visit within 7 days of being discharged from their anaphylaxis/allergy hospital visit, 0 if they were not seen for an outpatient visit within 7 days. A patient who is seen at any point on the 7th
 day should be flagged (e.g., a patient who presents to the ED on 2/6/2015 at 1AM who had an outpatient follow up visit on 2/13/2015 at 3PM should be flagged as having an outpatient visit within 7 days, even though this is greater than 168 hours apart).
4. FOLLOW\_UP\_DATE: The date of the first (if any) outpatient follow up that occurs within 7 days. The field should be blank if there is no follow up within 7 days.
5. DAYS\_TO\_FOLLOW\_UP: The number of days from the patient&#39;s discharge from the hospital to the first (if any) outpatient follow up visit (e.g., a patient discharged at 3PM on 1/3/2015 who had an initial outpatient follow up at 5PM on 1/6/2015 should have a DAYS\_TO\_FOLLOW\_UP of 3). The field should be blank if there is no follow up within 7 days.

**Part 3: Export the data set into a csv file for submission**

Export a dataset containing these required fields:

| Field name | Field Description | Data Type | Note  |
| --- | --- | --- | --- |
| PAT\_KEY | Patient identifier | Num | Found in the VISIT table. |
| VISIT\_KEY | Visit identifier | Num | Found in the VISIT table. |
| HOSP\_ADMIT\_DT | Hospital admit date | Date/time | Found in the VISIT table |
| AGE | Patient age at admission | Num | Found in the VISIT table |
| ANAPH\_DX\_IND | Indicator if the patient has a diagnosis containing the word &#39;anaphylaxis&#39; | 0 /1 | DX\_NM is found in the DIAGNOSIS table |
| EPI\_ORDER\_IND | Indicator if the patient had an order for epinephrine during their hospital visit | 0 /1 | MED\_ORD\_NM is found in the MEDICATION\_ORDER table |
| FOLLOW\_UP\_IND | Indicator if the patient was seen for an outpatient visit within 7 days of being discharged from their anaphylaxis/allergy hospital visit | 0/1 | All necessary source fields are found in the VISIT table. Outpatient office visits are defined by a dict\_enc\_type\_key value of 108 |
| FOLLOW\_UP\_DATE | Date of the first outpatient follow up visit within 7 days of being discharged | Date/time (blank if no follow up) | Found in the VISIT table |
| DAYS\_TO\_FOLLOW\_UP | Number of elapsed days between discharge from the hospitalization and the first outpatient follow up visit | Num (blank if no follow up) | Found in the VISIT table |
