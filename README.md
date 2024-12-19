This project is a study of biomass conditions and the effects on hydrogen and char production. Input variables such as elemental percentages will predict the two factors: the H2 content and Char yield. This project is finding the relationship using a machine learning algorithm to find a relationship between the inputs and the outputs.

Link to app: https://mlfinalexam.streamlit.app/

All the data processing and steps to get the final ML models are in "final_project_data_science.ipynb"

The input variables are ['H (%)', 'N (%)', 'O (%)', 'S (%)', 'VM (%)', 'Ash (%)', 'FC (%)', 'T (°C)', 'OC (%)', 'SBR']

C (%): Carbon content - The percentage of carbon in the biomass material

H (%): Hydrogen content - How much hydrogen is naturally present in the biomass

N (%): Nitrogen content - The amount of nitrogen in the material

O (%): Oxygen content - How much oxygen is present in the biomass

S (%): Sulfur content - The percentage of sulfur in the material (typically low in biomass)


Material Properties:


VM (%): Volatile Matter - The portion of the biomass that turns into gas when heated

Ash (%): Ash content - The non-combustible minerals left after complete burning

FC (%): Fixed Carbon - The solid carbon left after the volatile matter is removed


Process Conditions (How the experiment was run):


T (°C): Temperature - How hot the reaction was run

OC (%): Oxygen Content - How much oxygen was provided during the process

SBR: Steam to Biomass Ratio - The amount of steam used compared to the amount of biomass (like a recipe ratio)

The output variables are ['H2 (wt.%)', 'Char yield (wt.%)']

H2 (wt.%): Hydrogen Yield - How much hydrogen gas was produced (by weight)

Char yield (wt.%): Char Yield - How much solid material (char) was left after the process

This is written by Jolien Tran
