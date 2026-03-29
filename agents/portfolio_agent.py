def check_portfolio(portfolio, stock):
    if stock in portfolio:
        return "⚠️ High Exposure"
    else:
        return "No Risk"