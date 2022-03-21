from json import JSONDecoder
import numpy
import skfuzzy
import matplotlib.pyplot as plt
from skfuzzy import control


def compute_tip(service_input, quality_input):

    quality = skfuzzy.control.Antecedent(numpy.arange(0, 11, 1), 'quality')    
    service = skfuzzy.control.Antecedent(numpy.arange(0, 11, 1), 'service')
    tip = skfuzzy.control.Consequent(numpy.arange(0, 26, 1), 'tip')            

    quality.automf(3)      
    service.automf(3)       

    tip['low'] = skfuzzy.trimf(tip.universe, [0, 0, 13])                      
    tip['medium'] = skfuzzy.trimf(tip.universe, [0, 13, 25])                   
    tip['high'] = skfuzzy.trimf(tip.universe, [13, 25, 25])                     

    rule1 = skfuzzy.control.Rule(quality['poor'] | service['poor'], tip['low'])    
    rule2 = skfuzzy.control.Rule(service['average'], tip['medium'])
    rule3 = skfuzzy.control.Rule(service['good'] | quality['good'], tip['high'])

    tipping_ctrl = skfuzzy.control.ControlSystem([rule1, rule2, rule3])        
                                                                        
    tipping = skfuzzy.control.ControlSystemSimulation(tipping_ctrl)             
                                                                    
    tipping.input['quality'] = quality_input
    tipping.input['service'] = service_input

    tipping.compute()                                             
    return (tipping.output['tip'])