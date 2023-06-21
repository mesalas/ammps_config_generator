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
                                           "updateSecs": [60, 61, True],
                                           "lookbackPeriods": 15,
                                           "mpLookback": [120,121, True],
                                           "spreadFactor": [0.1, 0.11, True],
                                           "recalcOnLoss": "false",
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
    "initialCash" : 100000.0,
    "minLatency" : intraday_traders_minLatency,
    "meanLatency" : intraday_traders_meanLatency,
    "latencyStdevPct" : intraday_traders_latencyStdevPct,
    "agentSymbols" : intraday_traders_agentSymbols,
    "lookback" : [30, 60],
    "triggerSecs" : [15*60, 120*60],
    "stopMultiplier" : [0.5, 2.5, True],
    "parameter" : [1.5, 4.0, True],
    "recalcOnLoss" : "false",
    "getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                           )


## BreakoutTrend traders
breakout_traders_ST = AgentConfiguration( "BreakoutTrendST", {
    "initialCash": 100000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 30],
    "triggerSecs": [15 * 60, 120 * 60],
    "stopMultiplier" : [.5, 2.5, True],
    "parameter": [.5, 2.5, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                          )


## RsiReversion
rsireversion_traders_ST = AgentConfiguration( "RsiReversionST", {
    "initialCash": 100000.0,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 30],
    "triggerSecs": [15 * 60, 120 * 60],
    "stopMultiplier" : [.5, 2.5, True],
    "parameter": [5.0, 30.0, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                              )



## PullbackReversion traders
pullbackreversion_traders_ST = AgentConfiguration( "PullbackReversionST", {
    "initialCash": 100000,
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
    "initialCash": 100000,
    "minLatency": intraday_traders_minLatency,
    "meanLatency": intraday_traders_meanLatency,
    "latencyStdevPct": intraday_traders_latencyStdevPct,
    "agentSymbols": intraday_traders_agentSymbols,
    "lookback": [10, 30],
    "triggerSecs": [15 * 60, 120 * 60],
    "stopMultiplier" : [.5, 2.5, True],
    "parameter": [0.5, 4.0, True],
    "recalcOnLoss": "false",
    "getFlatOnClose": "true",
    "ziReversionFactor" : 0}
                                                  )




portfolio_trader = AgentConfiguration( "PortfolioTrader", {
    "initialCash": 10000000,
    "minLatency": 100,
    "meanLatency": 60000000,
    "latencyStdevPct": 0.5,
    "agentSymbols": intraday_traders_agentSymbols,
    "portfolioHorizonRangeMin" : 5,
    "portfolioHorizonRangeMax" : 30,
    "initialVol" : 0.02,
    "epsGrowthRate": 0.0003,
    "epsGrowthRateStd": 0.006,
    "updateOnEarningsPct" : 1.0,
    "rebalanceThresholdMin" :0.01 ,
    "rebalanceThresholdMax" : 0.05,
    "updatePortfolioThresholdMin" : 0.05,
    "updatePortfolioThresholdMax" :0.1
}
    )

basic_trader = AgentConfiguration("BasicTrader" , {"initialCash" : 100000,
                                                   "minLatency": 100,
                                                   "meanLatency" : 60000000,
                                                   "latencyStdevPct" : 0.5,
                                                   "agentSymbols": intraday_traders_agentSymbols,
                                                   "costScale" : 0.25,
                                                   "triggerSecs" : [0.1*23400,2*23400]})
