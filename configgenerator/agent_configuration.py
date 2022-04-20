import pandas as pd
#import numpy as np
class AgentConfiguration:
    '''
    Class for setting up a configuration for a group of agents.
    Calling the make_param will generate a pandas DataFrame for the specified number of agents.
    A row for each agent and the columns are the parameters.
    '''
    def __init__(self, name, params):
        self.parameters = params
        self.name = name

    def make_param(self,np, n, start_number = 0, name_suffix = "") -> pd.DataFrame:
        '''For each agent generate a set of parameters from defined in self.params. There are three ways the
         params can be generated, depending on the type of value in the self.params dict.
         1. if val is a list of length 2. a random value is returned bound by the first and second number in the list
         2. if value is a list of length three, containing two numbers and a bool, a random value is drawn between the
          first and second number as well as keeping the limits.
         3. if value is not a list its is passed through.'''

        if type(n) == float:
            n = int(n)
        if type(start_number) == float :
            start_number = int(start_number)
        if n == 0:
            return pd.DataFrame([])
        confs = list()
        for i in range(n):
            parameter_output_dict = dict()
            parameter_output_dict["name"] = self.name +name_suffix+ "-"+ str(i+start_number)
            for k,v in self.parameters.items():
                if type(v) == list:
                    v_min = v[0]
                    v_max = v[1]
                    random_method = np.random.uniform
                    if (type(v_min) is int and type(v_max) is int):
                        random_method = np.random.randint
                    if v_min > v_max:
                        v_min = v[1]
                        v_max = v[0]
                    parameter_output_dict[k] = random_method(v_min, v_max)
                    if len(v) == 3:
                        if v[2] == True:
                            parameter_output_dict[k+"Min"] = [v_min]
                            parameter_output_dict[k + "Max"] = [v_max]

                else:
                    parameter_output_dict[k] = [v]
            confs.append(pd.DataFrame(parameter_output_dict))
        return pd.concat(confs).reset_index()


