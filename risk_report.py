from holdings import stocks, generate_description_page, holdings
from fpdf import FPDF
from correl_matrix import make_matrix
from monte_carlo import run_monte_carlo
import datetime as dt

today = str(dt.datetime.now().strftime('%Y-%m-%d'))
pdf = FPDF('P')
# Cover Page
pdf.add_page()
pdf.set_font('Arial', '', 35)
pdf.cell(0, 50, txt= 'Artemis FP Risk Report', border=0, ln=0, align='C', fill=False, link='')
pdf.cell(-200, 150, txt=today, border=0, ln=0, align='C', fill=False, link='')

# Page 1: Description of each of the mutual funds
pdf.add_page()
pdf.set_font('Arial', '', 16)
pdf.write(10, 'ETF Descriptions')
generate_description_page(holdings[:4], pdf)
pdf.add_page()
pdf.write(10, 'ETF Descriptions')
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
pdf.add_page()
pdf.write(10, 'Monte Carlo Simulation (10,000 Simulations)')
run_monte_carlo()
pdf.image('images/monte_carlo.png', 20, 40, 160, 120)

# Page 6: Historical Daily Returns going back 20 years

# Page 7: Markowitz Efficient Frontier Portfolio with current client portfolio

# Page 7: Scenario Analysis? Sensitivity to interest rate rises

pdf.output('risk_report.pdf')