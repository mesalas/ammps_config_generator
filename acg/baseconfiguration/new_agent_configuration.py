## In this file we define the actors and the default values of them
# Based on the homemade modules:
from acg.configgenerator.agent_configuration import AgentConfiguration

### INSTITUTIONS ###



portfolio_trader = AgentConfiguration( "RandomPortfolioTrader",
                                                  {"minLatency": 100,
                                                   "meanLatency": 60000000,
                                                   "latencyStdevPct": 0.5,
                                                   "portfolioHorizonRangeMin": 1,
                                                   "portfolioHorizonRangeMax": 21,
                                                   "initialCash": 50000.0,
                                                   "agentSymbols" : "ABC,DEF,GHI",
                                                   "initialVol": 0.006,
                                                   "epsGrowthRate" : 0.0,
                                                   "epsGrowthRateStd" : 0.0,
                                                   "earningsZscoreThreshold" : 0.0,
                                                   "updatePortfolioThresholdMin" : 0.0,
                                                   "updatePortfolioThresholdMax" : 100.0,
                                                   "updateCovariance" : "true",
                                                   "alpha" : 0.0
                                                   }
                                                  )

eps_portfolio_trader = AgentConfiguration( "EPSportfolioTrader",
                                                  {"minLatency": 100,
                                                   "meanLatency": 1000000,
                                                   "latencyStdevPct": 0.5,
                                                   "portfolioHorizonRangeMin": 1,
                                                   "portfolioHorizonRangeMax": 31,
                                                   "initialCash": 4000000.0,
                                                   "agentSymbols" : "ABC,DEF,GHI",
                                                   "initialVol": 0.006,
                                                   "epsGrowthRate" : 0.0003,
                                                   "epsGrowthRateStd" : 0.003,
                                                   "earningsZscoreThreshold" : [0.0, 100],
                                                   "updatePortfolioThresholdMin" : 0.0,
                                                   "updatePortfolioThresholdMax" : 100.0,
                                                   "updateCovariance" : "true",
                                                   }
                                                  )



### MARKET MAKERS ###
marketmaker_traders = AgentConfiguration( "MarketMaker",
                                          {"initialCash": 1000000,
                                           "minLatency": 25,
                                           "meanLatency": 150,
                                           "latencyStdevPct": 0.5,
                                           "agentSymbols" : "ABC,DEF,GHI",
                                          "initialVolatility" : "0.5,0.5,0.5",
                                           "updateSecs": [3600, 23400, True],
                                           "lookbackPeriods": [20,31],
                                           "mpLookback": [120,121, True],
                                           "spreadFactor": [7.0, 8.0, True],
                                           "recalcOnLoss": "false",
                                           "workSize": 100,
                                           "levels": 10,
                                           "minSpread": 0.0101,
                                           "instrumentFactor" : 2.5,
                                           "aggressiveFactor": 0.0,
                                           "portfolioFactor": 0.0,
                                           "updateParams" : "false",
                                           "learningRate" : 0.0,
                                           "learningDiscountFactor" : 0.0
                                           }
                                          )



### PAIRS TRADERS ###
pair_traders = AgentConfiguration( "PairsTrader",
                                   {"initialCash": 50000,
                                    "minLatency": 100,
                                    "meanLatency": 1500,
                                    "latencyStdevPct": 0.5,
                                    "agentPairs": "ABC,DEF;DEF,GHI;GHI,ABC",
                                    "horizon" : [10*23400, 30*23400],
                                    "lookbackPeriods": [10,30] ,
                                    "updateInterval": [30 * 60, 360 * 60],
                                    "zThreshold": [1, 2.5],
                                    "tradeFraction": 0.001}
                                   )


### INTRADAY TRADERS ###

technical_traders = AgentConfiguration( "TechnicalTrader",
                                           {"initialCash": 50000.0,
                                            "minLatency": 100,
                                            "meanLatency": 500000,
                                            "latencyStdevPct": 0.5,
                                            "agentSymbols": "ABC,DEF,GHI",
                                            "lookback": [10, 20],
                                            "triggerSecs": [10 * 60, 390 * 60],
                                            "stopMultiplier": [0.25, 3.5, True],
                                            "parameter": [0.0,1.0, True],
                                            "recalcOnLoss": "false",
                                            "getFlatOnClose": "false",
                                            }
                                           )


