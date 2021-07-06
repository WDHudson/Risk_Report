from holdings import stocks, generate_description_page, holdings
from fpdf import FPDF
from correl_matrix import make_matrix

pdf = FPDF('P')
# Page 1: Description of each of the mutual funds
pdf.add_page()
generate_description_page(holdings[:4], pdf)
pdf.add_page()
generate_description_page(holdings[4:], pdf)

# Page 2: Pie Chart showing allocations

# Page 3: Asset Class allocation

# Page 4: Correlation Matrix with covariance table below it
pdf.add_page()
pdf.write(10, 'Correlation Matrix with Covariance Table')
make_matrix()
pdf.image("images/correl_matrix.png", 20, 40, 150, 120)
pdf.image('images/cov_table.png', 20, 180, 170, 85)

# Page 5: Monte Carlo Simulation with VaR and CVaR

# Page 6: Historical Daily Returns going back 20 years

# Page 7: Markowitz Efficient Frontier Portfolio with current client portfolio

# Page 7: Scenario Analysis? Sensitivity to interest rate rises

pdf.output('risk_report.pdf')