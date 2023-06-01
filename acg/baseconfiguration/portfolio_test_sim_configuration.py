## In this file we define the actors and the default values of them
# Based on the homemade modules:
from acg.configgenerator.agent_configuration import AgentConfiguration

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
                                           "recalcOnLoss": "true",
                                           "workSize": 105,
                                           "levels": 30,
                                           "minSpread": 0.0101,
                                           "inventoryPenalty": 0.0,
                                           "inventoryFactor" : 0.000333333,
                                           "followTrend" : 0.0,
                                           "scaleWorkSize": "false"}
                                          )



### INTRADAY TRADERS ###

# Shared variables
intraday_traders_minLatency = 100
intraday_traders_meanLatency = 500000
intraday_traders_latencyStdevPct = 0.5
intraday_traders_agentSymbols = "ABC"


## Aggressor traders
aggressor_traders_ST = AgentConfiguration( "AggressorTrendST", {
    "initialCash" : 300000.0,
    "minLatency" : intraday_traders_minLatency,
    "meanLatency" : intraday_traders_meanLatency,
    "latencyStdevPct" : intraday_traders_latencyStdevPct,
    "agentSymbols" : intraday_traders_agentSymbols,
    "lookback" : [10, 20],
    "triggerSecs" : [5*60, 120*60],
    "stopMultiplier" : [1.5, 3.5, True],
    "parameter" : [1.75, 3.0, True],
    "recalcOnLoss" : "false",
    "getFlatOnClose": "false",
    "ziReversionFactor" : 0}
                                           )


## BreakoutTrend traders
breakout_traders_ST = AgentConfiguration( "BreakoutTrendST", {
    "initialCash": 300000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 20],
    "triggerSecs": [5 * 60, 60 * 60],
    "stopMultiplier" : [1.5, 3.5, True],
    "parameter": [1., 3., True],
    "recalcOnLoss": "false","getFlatOnClose": "false",
    "ziReversionFactor" : 0}
                                          )


## RsiReversion
rsireversion_traders_ST = AgentConfiguration( "RsiReversionST", {
    "initialCash": 300000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 20],
    "triggerSecs": [30 * 60, 120 * 60],
    "stopMultiplier" : [1.5, 3.5, True],
    "parameter": [5.0, 25.0, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "false",
    "ziReversionFactor" : 0}
                                              )



## PullbackReversion traders
pullbackreversion_traders_ST = AgentConfiguration( "PullbackReversionST", {
    "initialCash": 300000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 50],
    "triggerSecs": [15 * 60, 180 * 60],
    "stopMultiplier" : [.5, 3.5, True],
    "parameter": [0.0, 0.0, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "false",
    "ziReversionFactor" : 0}
                                                   )



## ScalperReversion traders
scalperreversion_traders_ST = AgentConfiguration( "ScalperReversionST", {
    "initialCash": 300000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [25, 50],
    "triggerSecs": [30 * 60, 90 * 60],
    "stopMultiplier" : [1.5, 3.5, True],
    "parameter": [1.25, 2.5, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "false",
    "ziReversionFactor" : 0}
                                                  )


zero_info_trader_ST = AgentConfiguration( "ZeroInfoST", {
    "initialCash": 100000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [20, 50],
    "triggerSecs": [600, 3600],
    "stopMultiplier": [0.5, 5., True],
    "parameter": [600, 3600, True],
    "recalcOnLoss": "false",
    "getFlatOnClose" : "false",
    "ziReversionFactor" : 0.25}
                                          )


portfolio_trader = AgentConfiguration( "PortfolioTrader", {
    "initialCash": 10000000,
    "minLatency": 100,
    "meanLatency": 60000000,
    "latencyStdevPct": 0.5,
    "agentSymbols": intraday_traders_agentSymbols,
    "portfolioHorizonRangeMin" : 5,
    "portfolioHorizonRangeMax" : 60,
    "initialVol" : 0.02,
    "epsGrowthRate": 0.0003,
    "epsGrowthRateStd": 0.006,
    "updateOnEarningsPct" : 1.0}
                                          )

basic_trader = AgentConfiguration("BasicTrader" , {"initialCash" : 100000,
                                                   "minLatency": 100,
                                                   "meanLatency" : 60000000,
                                                   "latencyStdevPct" : 0.5,
                                                   "agentSymbols": "ABC,DEF,GHI",
                                                   "costScale" : 1.0 })
