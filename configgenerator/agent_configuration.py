import pandas as pd
import numpy as np
class AgentConfiguration:
    def __init__(self, name, params):
        self.parameters = params
        self.name = name

    def _make_param_table(self):
        parameter_output_dict = dict()
        for k,v in self.parameters.items():
            if type(v) == list:
                parameter_output_dict[k+"Min"] = [min(v)]
                parameter_output_dict[k + "Max"] = [max(v)]
            else:
                parameter_output_dict[k] = [v]
        return pd.DataFrame(parameter_output_dict)

    def make_param(self, n, start_number = 0, name_suffix = ""):
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


