# Configuration generator
import xlsxwriter as xlwrt

class AgentConfig:

    def __init__(self,agent_name, parameters):
        self.agent_name = agent_name
        self.parameters = parameters

class ConfigurationWriter:

    def __init__(self, config_name, seed, path, file_name):
        self.filename = path + file_name
        self.xlsxfile = xlwrt.Workbook(self.filename)
        self.add_sim_name(config_name)
        self.add_seed(seed)

    def write_file(self):
        self.xlsxfile.close()

    def add_dates(self,start_year,start_month,start_day,start_hour, start_min, start_sec,
                  end_year,end_month,end_day,end_hour,end_min, end_sec):
        name = "SimulationDates"
        attributes = ["StartDate","EndDate"]
        values = [{ "StartDate" : str(start_year) +","+ str(start_month) + ","+ str(start_day)+ ","+ str(start_hour) + "," + str(start_min) + "," + str(start_sec) ,
                  "EndDate" : str(end_year) +","+ str(end_month) + ","+ str(end_day)+ ","+ str(end_hour) + "," + str(end_min) + "," + str(end_sec)}]
        self._write_sheet(name,attributes,values)

    def add_seed(self, seed):
        name = "Random seed"
        attributes = ["seed"]
        values = [{"seed":seed}]
        self._write_sheet(name, attributes, values)

    def add_sim_name(self, sim_name):

        name = "SimulationName"
        attributes = ["name"]
        values = [{"name" : sim_name}]
        self._write_sheet(name, attributes, values)

    def _write_sheet(self, name, attributes, values):
        if len(values) > 0:
            sheet = self.xlsxfile.add_worksheet(name=name)
            # Set initial row and columns
            row = 0
            col = 0
            sheet.write(row, col, name)
            row += 1  # move to next row

            # write attributes
            for attr in attributes:
                sheet.write(row, col, attr)
                col += 1
            row += 1
            col = 0
            # write values
            for value_set in values:
                for attr in attributes:
                    sheet.write(row, col, value_set[attr])
                    col += 1
                row += 1
                col = 0

    def add_agent(self, name, values):
        if len(values) == 0:
            return
        attributes = list(values[0])
        if "index" in attributes:
            attributes.remove("index")
        self._write_sheet(name, attributes, values)
