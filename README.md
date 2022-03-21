# Tipping-Problem
Tipping Problem solved using fuzzy logic and UI implemented using tkinter.
The tipping problem is commonly used to illustrate the power of fuzzy logic principles to generate complex behavior from a compact, intuitive set of expert rules.

## Input variables
A number of variables play into the decision about how much to tip while dining. Consider two of them:

**quality** : Quality of the food
**service** : Quality of the service

## Output variable
The output variable is simply the tip amount, in percentage points:

**tip** : Percent of bill to add as tip

## Execution
Window.py executes the main problemand gives the UI designed in tkinter.
Fuzzy.py is the logic execution of the fuzzy controler in the program.
FuzzyLofic.py is the main complete execution of the fuzzy controler that provdes the membership graphs which are not necessary in the application UI.

### To run the application, execute

```shell
cd Tipping-Problem
```
```shell
pip install requirements.txt
```
```shell
python3 window.py
```
## Fuzzy Logic Plots

![alt text](https://github.com/therrshan/Tipping-Problem/blob/main/assets/plot1.png "Input Membership Functions")
![alt text](https://github.com/therrshan/Tipping-Problem/blob/main/assets/plot2.png "Output Membership Function")
![alt text](https://github.com/therrshan/Tipping-Problem/blob/main/assets/plot3.png "Aggregated Membership(Result)")
