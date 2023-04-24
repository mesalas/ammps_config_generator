## In this file we define the actors and the default values of them
# Based on the homemade modules:
from  configgenerator.agent_configuration import AgentConfiguration

### INSTITUTIONS ###

hark_broker_institution = AgentConfiguration("HarkBrokerInstitution", {"minLatency":100,
                                                                        "meanLatency":500000,
                                                                        "latencyStdevPct":0.5,
                                                                        "brokerSide": "empty",
                                                                        "initialCash":1000000})

hark_broker_two_venue_institution = AgentConfiguration("HarkBrokerInstitution", {"minLatency":100,
                                                                        "meanLatency":500000,
                                                                        "latencyStdevPct":0.5,
                                                                        "brokerSide": "empty",
                                                                        "initialCash":1000000,
                                                                        "publicSymbol" : "ABC_NYSE",
                                                                        "internalSymbol" : "ABC_CITADEL",
                                                                         "publicMarketFraction" : 0.5}
                                                       )
longshort_institutions_LT = AgentConfiguration( "LongShortInstitutionLT" ,
                                                {"minLatency" : 100,
                                                 "meanLatency" : 500000,
                                                 "latencyStdevPct" : 0.5,
                                                 "forecastMin" : 10,
                                                 "ForecastMax" : 45,
                                                 "executionMin" : 1,
                                                 "executionMax" : 10,
                                                 "sizeMin" : 0.025, "sizeMax" : 0.05,
                                                 "initialCash" : 250000.0,
                                                 "entryThreshold" : 0.25,
                                                 "defaultVol" : 0.005})

longshort_institutions_ST = AgentConfiguration( "LongShortInstitutionST" ,
                                                {"minLatency" : 100,
                                                 "meanLatency" : 500000,
                                                 "latencyStdevPct" : 0.5,
                                                 "forecastMin" : 4,
                                                 "ForecastMax" : 10,
                                                 "executionMin" : 1,
                                                 "executionMax" : 4,
                                                 "sizeMin" : 0.025, "sizeMax" : 0.05,
                                                 "initialCash" : 125000.0,
                                                 "entryThreshold" : 0.25,
                                                 "defaultVol" : 0.005})

dividend_longshort_institutions = AgentConfiguration( "DividendInstitution" ,
                                                {"minLatency" : 100,
                                                 "meanLatency" : 500000,
                                                 "latencyStdevPct" : 0.5,
                                                 "forecastMin" : 60,
                                                 "ForecastMax" : 120,
                                                 "sizeMin" : 0.005, "sizeMax" : 0.025,
                                                 "initialCash" : 1000000.0,
                                                 "entryThreshold" : 0.001,
                                                 "defaultVol" : 0.01,
                                                 "discountFactor" : 0.96,
                                                 "CRRA" : 5,
                                                 "dividendGrowthRate": 1.000628,
                                                 "dividendStd" : 0.011988,
                                                 "daysPerQuarter" : 90,
                                                 "symbol" : "ABC_NYSE",
                                                 "valuationStd" : 0.15})

# chock_institutions = traders_v2.Institutions(
#     initial_number = 1,
#     minLatency = 100,
#     meanLatency = 500000,
#     latencyStdevPct = 0.5,
#     forecast_LT = [40, 40],
#     execution_LT = [39, 39],
#     size_LT = [1., 1.],
#     tot_initialCash_LT = 16000000,
#     forecast_ST = [4, 10],
#     execution_ST = [1, 4],
#     size_ST = [0.025, 0.05],
#     tot_initialCash_ST = 125000.0,
#     default_vol = 100.
# )


sectorrotate_institution_LT = AgentConfiguration( "SectorRotateInstitutionLT",
                                                  {"minLatency" : 100,
                                                   "meanLatency" : 500000,
                                                   "latencyStdevPct" : 0.5,
                                                   "forecastMin" : 10,
                                                   "ForecastMax" : 40,
                                                   "executionMin" : 1, "executionMax" :  10,
                                                   "sizeMin" : 0.025, "sizeMax" : 0.05,
                                                   "initialCash" : 250000.0,
                                                   "entryThreshold" : 0.1,
                                                   "defaultVol" : 0.005}
                                                  )

sectorrotate_institution_ST = AgentConfiguration( "SectorRotateInstitutionST",
                                                  {"minLatency": 100,
                                                   "meanLatency": 500000,
                                                   "latencyStdevPct": 0.5,
                                                   "forecastMin": 4,
                                                   "ForecastMax": 10,
                                                   "executionMin": 1,
                                                   "executionMax": 4,
                                                   "sizeMin": 0.025,
                                                   "sizeMax": 0.05,
                                                   "initialCash": 125000.0,
                                                   "entryThreshold" : 0.1,
                                                   "defaultVol": 0.005}
                                                  )

#institutions_types = {
#    "LongShortInstitution": longshort_institutions,
#    "SectorRotateInstitution": sectorrotate_institutions,
#    "Chock" : chock_institutions
#}


### RANDOM TRADERS ###
# random_traders = traders_v2.Random(
#     initialCash = 1.0e6,
#     minLatency = 10,
#     meanLatency = 500000,
#     latencyStdevPct = 0.5,
#     agentSymbols = "ABC,DEF,GHI",
#     number = 300,
#     reversion_factor = 0.1,
#     weibull_shape = 1,
#     weibull_scale = 120,
#     lookback = 20,
#     trading_fraction = 0.003
# )
# # ChockTrader
# chock_traders = traders_v2.ChockTrader(
#     minLatency = 10,
#     meanLatency = 500000,
#     latencyStdevPct = 0.5
# )


### MARKET MAKERS ###
marketmaker_traders = AgentConfiguration( "MarketMaker",
                                          {"initialCash": 1000000,
                                           "minLatency": 25,
                                           "meanLatency": 150,
                                           "latencyStdevPct": 0.5,
                                           "symbolA": "ABC",
                                           "symbolACorrelation": 0.02,
                                           "symbolB": "DEF",
                                           "symbolBCorrelation": 0.02,
                                           "symbolC": "GHI",
                                           "symbolCCorrelation": 0.02,
                                           "updateSecs": [600, 601, True],
                                           "lookbackPeriods": 50,
                                           "mpLookback": [120,121, True],
                                           "spreadFactor": [0.15, 0.16, True],
                                           "recalcOnLoss": "false",
                                           "workSize": 105,
                                           "levels": 30,
                                           "minSpread": 0.0101,
                                           "inventoryPenalty": 0.0,
                                           "inventoryFactor" : 0.000333333,
                                           "followTrend" : 0.0,
                                           "scaleWorkSize": "true"}
                                          )
lucas_marketmaker_traders = AgentConfiguration( "LucasMarketMaker",
                                          {"initialCash": 1000000,
                                           "minLatency": 25,
                                           "meanLatency": 150,
                                           "latencyStdevPct": 0.5,
                                           "symbolA": "ABC",
                                           "symbolACorrelation": 0.02,
                                           "symbolB": "DEF",
                                           "symbolBCorrelation": 0.02,
                                           "symbolC": "GHI",
                                           "symbolCCorrelation": 0.02,
                                           "updateSecs": [600, 601, True],
                                           "lookbackPeriods": 50,
                                           "mpLookback": [120,121, True],
                                           "spreadFactor": [0.15, 0.16, True],
                                           "recalcOnLoss": "false",
                                           "workSize": 105,
                                           "levels": 30,
                                           "minSpread": 0.0101,
                                           "inventoryPenalty": 0.0,
                                           "inventoryFactor" : 0.000333333,
                                           "followTrend" : 0.0,
                                           "scaleWorkSize": "true",
                                           "lucasFactor" : 0.0,
                                           "CRRA" : 5.0,
                                           "discountFactor" : 0.96,
                                           "dividendGrowthRate": 1.000628,
                                           "dividendStd": 0.011988,
                                           "daysPerQuarter" : 90}
                                          )

internal_marketmaker  = AgentConfiguration( "InternalMarketMaker",
                                          {"initialCash": 1000000,
                                           "minLatency": "-",
                                           "meanLatency": 1,
                                           "latencyStdevPct": "-",
                                           "publicSymbol": "ABC_NYSE",
                                           "internalSymbol": "ABC_CITADEL"}
                                          )


### PAIRS TRADERS ###
pair_traders = AgentConfiguration( "PairsTrader",
                                   {"initialCash": 1.0e5,
                                    "minLatency": 100,
                                    "meanLatency": 1500,
                                    "latencyStdevPct": 0.5,
                                    "agentPairs": "ABC,DEF;DEF,GHI;GHI,ABC",
                                    "horizon" : [10*23400, 30*23400],
                                    "lookbackPeriods": 0 ,
                                    "updateInterval": [30 * 60, 360 * 60],
                                    "zThreshold": [1.74, 2.5],
                                    "tradeFraction": 0.001}
                                   )


### INTRADAY TRADERS ###

# Shared variables
intraday_traders_minLatency = 100
intraday_traders_meanLatency = 500000
intraday_traders_latencyStdevPct = 0.5
intraday_traders_agentSymbols = "ABC" #,DEF,GHI"

## Opening range traders
openingrange_traders = AgentConfiguration( "OpeningRangeTrend",
                                           {"initialCash": 50000.0,
                                            "minLatency": intraday_traders_minLatency,
                                            "meanLatency": intraday_traders_meanLatency,
                                            "latencyStdevPct": intraday_traders_latencyStdevPct,
                                            "agentSymbols": intraday_traders_agentSymbols,
                                            "lookback": [10, 30],
                                            "triggerSecs": [20 * 60, 180 * 60],
                                            "stopMultiplier": [0.15, 1., True],
                                            "parameter": [10 * 60, 60 * 60, True],
                                            "recalcOnLoss": "false",
                                            "getFlatOnClose": "true",
                                            "ziReversionFactor" : 0
                                            }
                                           )

## Aggressor traders
aggressor_traders_ST = AgentConfiguration( "AggressorTrendST", {
    "initialCash" : 100000.0,
    "minLatency" : intraday_traders_minLatency,
    "meanLatency" : intraday_traders_meanLatency,
    "latencyStdevPct" : intraday_traders_latencyStdevPct,
    "agentSymbols" : intraday_traders_agentSymbols,
    "lookback" : [10, 20],
    "triggerSecs" : [5*60, 120*60],
    "stopMultiplier" : [1., 3., True],
    "parameter" : [1.75, 3.0, True],
    "recalcOnLoss" : "false",
    "getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                           )

aggressor_traders_LT = AgentConfiguration("AggressorTrendLT",
                                          {"initialCash": 500000.0,
                                           "minLatency": intraday_traders_minLatency,
                                           "meanLatency": intraday_traders_meanLatency,
                                           "latencyStdevPct": intraday_traders_latencyStdevPct,
                                           "agentSymbols": intraday_traders_agentSymbols,
                                           "lookback": [10, 20],
                                           "triggerSecs": [2500, 7500],
                                           "stopMultiplier": [0.5, 2.0, True],
                                           "parameter": [1.5, 3.0, True],
                                           "recalcOnLoss": "false",
                                           "getFlatOnClose" : "false",
                                           "ziReversionFactor" : 0}
                                          )

## BreakoutTrend traders
breakout_traders_ST = AgentConfiguration( "BreakoutTrendST", {
    "initialCash": 100000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 20],
    "triggerSecs": [5 * 60, 60 * 60],
    "stopMultiplier": [1., 3.0, True],
    "parameter": [1., 4., True],
    "recalcOnLoss": "false","getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                          )

breakout_traders_LT = AgentConfiguration( "BreakoutTrendLT", {
    "initialCash": 100000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 20],
    "triggerSecs": [60 * 60, 270 * 60],
    "stopMultiplier": [0.5, 2.5, True],
    "parameter": [0.25, 2.5, True],
    "recalcOnLoss": "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0}
                                          )

## HighLowTrend traders
# highlow_traders : traders.Intraday(
#     initialCash : intraday_traders_initialCash,
#     minLatency : intraday_traders_minLatency,
#     meanLatency : intraday_traders_meanLatency,
#     latencyStdevPct : intraday_traders_latencyStdevPct,
#     agentSymbols : intraday_traders_agentSymbols,
#     number : 100,
#     lookback : [10, 30],
#     fast_triggerSecs : [5*60, 60*60],
#     triggerSecs : [60*60, 270*60],
#     stopMultiplier : [0.2, 4.0],
#     parameter : [0.5, 2.5],
#     recalcOnLoss : "true"
# )

# ## DailyReversion traders
# dailyreversion_traders : traders.Intraday(
#     initialCash : intraday_traders_initialCash,
#     minLatency : intraday_traders_minLatency,
#     meanLatency : intraday_traders_meanLatency,
#     latencyStdevPct : intraday_traders_latencyStdevPct,
#     agentSymbols : intraday_traders_agentSymbols,
#     number : 100,
#     lookback : [10, 30],
#     triggerSecs : [30*60, 120*60],
#     stopMultiplier : [0.2, 4.0],
#     parameter : [0.25, 2.5],
#     recalcOnLoss : "true"
#)

## RsiReversion
rsireversion_traders_ST = AgentConfiguration( "RsiReversionST", {
    "initialCash": 150000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 20],
    "triggerSecs": [60*60, 120*60],
    "stopMultiplier": [1., 5.0, True],
    "parameter": [20, 40, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "false",
    "ziReversionFactor" : 0}
                                              )

rsireversion_traders_LT = AgentConfiguration( "RsiReversionLT", {
    "initialCash" : 500000.0,
    "minLatency" : intraday_traders_minLatency,
    "meanLatency" : intraday_traders_meanLatency,
    "latencyStdevPct" : intraday_traders_latencyStdevPct,
    "agentSymbols" : intraday_traders_agentSymbols,
    "lookback" : [5, 15],
    "triggerSecs" : [2500, 7500],
    "stopMultiplier" : [1., 3.0, True],
    "parameter" : [5, 25, True],
    "recalcOnLoss" : "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0}
                                              )

## PullbackReversion traders
pullbackreversion_traders_ST = AgentConfiguration( "PullbackReversionST", {
    "initialCash": 150000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 30],
    "triggerSecs": [30 * 60, 180 * 60],
    "stopMultiplier": [1., 2.0, True],
    "parameter": [0.0, 0.0, True],
    "recalcOnLoss": "false","getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                                   )

pullbackreversion_traders_LT = AgentConfiguration( "PullbackReversionLT", {
    "initialCash": 150000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [5, 20],
    "triggerSecs": [180 * 60, 360 * 60],
    "stopMultiplier": [1., 2.0, True],
    "parameter": [0.0, 0.0, True],
    "recalcOnLoss": "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0}
                                                   )

## ScalperReversion traders
scalperreversion_traders_ST = AgentConfiguration( "ScalperReversionST", {
    "initialCash": 150000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [25, 50],
    "triggerSecs": [30 * 60, 90 * 60],
    "stopMultiplier": [1., 5., True],
    "parameter": [1.25, 4, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                                  )

scalperreversion_traders_LT = AgentConfiguration( "ScalperReversionLT", {
    "initialCash": 150000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [15, 30],
    "triggerSecs": [120 * 60, 400 * 60],
    "stopMultiplier": [2., 10., True],
    "parameter": [1., 2.5, True],
    "recalcOnLoss": "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0}
                                                  )

zero_info_trader_ST = AgentConfiguration( "ZeroInfoST", {
    "initialCash": 100000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [20, 50],
    "triggerSecs": [200, 900],
    "stopMultiplier": [10., 20., True],
    "parameter": [200, 900, True],
    "recalcOnLoss": "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0.5}
                                          )

zero_info_trader_LT = AgentConfiguration( "ZeroInfoLT", {
    "initialCash" : 100000,
    "minLatency" : intraday_traders_minLatency,
    "meanLatency" : intraday_traders_meanLatency,
    "latencyStdevPct" : intraday_traders_latencyStdevPct,
    "agentSymbols" : intraday_traders_agentSymbols,
    "lookback" : [20, 50],
    "triggerSecs" : [3600, 10800],
    "stopMultiplier" : [10., 20., True],
    "parameter" : [3600, 10800, True],
    "recalcOnLoss" : "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0.5}
                                          )

# # Define dictionary of intraday traders for later use
# intraday_traders = {
#     "OpeningRangeTrend": openingrange_traders,
#     "AggressorTrendST": aggressor_traders_ST,
#     "AggressorTrendLT": aggressor_traders_LT,
#     "BreakoutTrendST": breakout_traders_ST,
#     "BreakoutTrendLT": breakout_traders_LT,
#     #"HighLowTrend": highlow_traders,
#     #"DailyReversion": dailyreversion_traders,
#     "PullbackReversionST": pullbackreversion_traders_ST,
#     "PullbackReversionLT": pullbackreversion_traders_LT,
#     "ScalperReversionST": scalperreversion_traders_ST,
#     "ScalperReversionLT": scalperreversion_traders_LT,
#     "RsiReversionST": rsireversion_traders_ST,
#     "RsiReversionLT": rsireversion_traders_LT,
#     "ZeroInfoST" : zero_info_trader_ST,
#     "ZeroInfoLT" : zero_info_trader_LT,
# }
