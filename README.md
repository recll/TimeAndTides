# TimeAndTides
AMA3020 Investigations Paired Project (Group 13)

Supplementary Materials

### Code
- [code/tidal_pred.py](code/tidal_pred.py) is the initial Python code used to develop the method to predict the time and heights of high and low tides.
- [code/Predict_Tide_Times.ipynb](code/Predict_Tide_Times.ipynb) is the Python notebook used to solve the systems of linear equations for the initial model at Bristol and Donaghadee. It shows more of the data and working for the plots and solutions focused on in the report. Dataframes of more precise values can also be found here.
- [code/Tide_Times_Lunar_Solar.ipynb](code/Tide_Times_Lunar_Solar.ipynb) is the Python notebook containing the work and solution for the extension part of the course at the Bristol port. It also includes attempts to apply this better model to Donaghadee (to mixed results), and attempts to extend the model further with more constituents that use more data points, however these were not included in the report to keep focus on the main outcomes instead. This also contains some additional dataframes and plots.
- [code/TideTimesM2S2N2.ipynb](code/TideTimesM2S2N2.ipynb) is an extra notebook that explored using the M2, S2 and N2 constituents together.

### Plots 
- [plots/BristolTimeAndErrors_a.pdf](plots/BristolTimeAndErrors_a.pdf) - Figure 1 in the report
- [plots/Donaghadee4DaysAndSimpleErrors_b.pdf](plots/Donaghadee4DaysAndSimpleErrors_b.pdf) - Figure 2 in the report
- [plots/BristolM2S2PlotAndErrors_horiz.pdf](plots/BristolM2S2PlotAndErrors_horiz.pdf) - Figure 3 in the report

### Derivations
- [Matrix_Equation.pdf](Matrix_Equation.pdf) - the long form derivation of the solution of the initial system of 3 linear equations to solve for a, b and h_0 by hand.
- [time_derivation_first_model.pdf](time_derivation_first_model.pdf) - the derivation to find the high and low tide times of the initial model exactly using the max and min values of t in the main equation. It should be noted this is not extended to the enhanced model with more sin and cos terms of other constituents, as this becomes a problem of finding the roots of a general Fourier Series which is beyond our scope.

### Data
- [TideData.xlsx](TideData.xlsx) - Our collected data from the Admiralty forecasts in an Excel spreadsheet that is fed into the code to build the models, along with some early predictions that were stored in Excel.

Admiralty EasyTide Tide Tables
- [Tidal_Times_Bristol _Week_1.pdf](Tidal_Times_Bristol_Week_1.pdf)
- [Tidal_Times_Bristol_Week_2.pdf](Tidal_Times_Bristol_Week_2.pdf)
- [Tidal_Times_Donaghadee_Week_1.pdf](Tidal_Times_Donaghadee_Week_1.pdf)
- [Tidal_Times_Donaghadee_Week_2.pdf](Tidal_Times_Donaghadee_Week_2.pdf)
