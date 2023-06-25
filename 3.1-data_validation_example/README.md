Data Validation is an important component in any data-driven business: quantitative trading funds, electronic trading shops, technology companies providing solutions to their clients and even healthcare company who tries to employ data-driven strategies to sell their products to healthcare institution. 

Doing data validation at the core of its name is not rocket science. First, you form an expectation of how your data should look like and then you test your data against that expectation. Of course, there will be anomalies that you want to handle and you wouldn't want a simple anomalies to jam up your orchestration process.

Learn by Scenario: 
You manage a portfolio quantitatively. You want to perform some automated sanity checks so you know that your rebalancing strategy is sane. Here are the conditions:
1) sum of weights should add up to 1
2) the data should not differ too much from yesterday's data
3) the weights should all be positive
4) Other more mainsteam checks: all rows are populated, all rows has ticker names

We will implement this check using great expectation library.

We have 3 stocks: AAPL, TESLA, KLAC. Based on 3 years of historical price history, formulate a risk parity portfolio and implement checks to ensure that your weights are sane.

