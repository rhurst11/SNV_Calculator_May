# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from apps.authentication.forms import CalculationForm

class Calculator:
    def __init__(self, name, tam, sam, som, seed_round_amount, pre_money_val, sales_multiple, dilution_estimate):  

#       listing basic variables here
        self.name = name
        self.Seed_roundamt = seed_round_amount * 1000000
        self.Seed_premoney = pre_money_val * 1000000
        self.Seed_postmoney = self.Seed_premoney + self.Seed_roundamt
        self.Seed_EquitySoldInRound = self.Seed_roundamt / self.Seed_postmoney
        self.Seedfirmcheck = 50000 

        self.tam = tam * 1000000000
        self.sam = sam * 1000000
        self.som = som * 1000000

        self.sales_multiple = sales_multiple

        self.dilution_hard_code =  dilution_estimate

#       listing assumed values here
#       for round amounts, I am using an average multiple to represent valuation jumps
        self.A_roundamt = self.Seed_roundamt * 4
        self.B_roundamt = self.A_roundamt * 1.875
        self.C_roundamt = self.B_roundamt * 2   

#       Consult with Jeff on this item, our discount may be much higher, and I will also need to factor in a scenario for it then
        self.Seed_option = 0.07
        self.A_option = 0.07     

#       for round amounts, I am using an average multiple to represent valuation jumps        
        self.A_premoney = self.Seed_premoney * 4
        self.B_premoney = self.A_premoney * 2.65625
        self.C_premoney = self.B_premoney * 2.35294  

#       direct derivative of user input: seed premoney valuation 
        self.A_postmoney = self.A_premoney + self.A_roundamt
        self.B_postmoney = self.B_premoney + self.B_roundamt
        self.C_postmoney = self.C_premoney + self.C_roundamt



# can have a default calculation for dilution if they plug in an assumption
# make sure that is can both filter and also educate

# USE CASE: don't propose a stupid valuation
# this is a hand holding exercise through dilution obstacles, it is a sanity check essentially

#       listing equity calculations here
#       direct derivative of user input: seed premoney valuation 
        self.A_EquitySoldInRound = self.A_roundamt / self.A_postmoney
        self.B_EquitySoldInRound = self.B_roundamt / self.B_postmoney
        self.C_EquitySoldInRound = self.C_roundamt / self.C_postmoney

        self.Seedfirmequity = self.Seedfirmcheck / self.Seed_postmoney 
        

# THIS IS THE MOST IMPORTANT FOR THE OUTPUT DISPLAY
        self.required_exit_for_40xMOIC = ((self.Seed_premoney * 40) + self.Seedfirmcheck)/ (1-self.dilution_hard_code) - 100000
        self.required_exit_for_20xMOIC = ((self.Seed_premoney * 20) + self.Seedfirmcheck)/ (1-self.dilution_hard_code) - 100000
        self.required_exit_for_10xMOIC = ((self.Seed_premoney * 10) + self.Seedfirmcheck)/ (1-self.dilution_hard_code) - 100000
        self.required_exit_for_5xMOIC = ((self.Seed_premoney * 5) + self.Seedfirmcheck)/ (1-self.dilution_hard_code) - 100000

        self.required_annual_sales = self.required_exit_for_40xMOIC / self.sales_multiple

@blueprint.route('/index', methods = ["POST", "GET"])
@login_required
def index():

    # user_pre_mon_val = TestCompany.Seed_premoney
    # user_post_mon_val = TestCompany.Seed_postmoney
    # output40x = TestCompany.required_exit_for_40xMOIC
    # output20x = TestCompany.required_exit_for_20xMOIC
    # output10x = TestCompany.required_exit_for_10xMOIC
    # output5x = TestCompany.required_exit_for_5xMOIC

    # low_alt_output40x = ControlCompanyLow.required_exit_for_40xMOIC
    # low_alt_output20x = ControlCompanyLow.required_exit_for_20xMOIC
    # low_alt_output10x = ControlCompanyLow.required_exit_for_10xMOIC
    # low_alt_output5x = ControlCompanyLow.required_exit_for_5xMOIC
 
    # high_alt_output40x = ControlCompanyHigh.required_exit_for_40xMOIC
    # high_alt_output20x = ControlCompanyHigh.required_exit_for_20xMOIC
    # high_alt_output10x = ControlCompanyHigh.required_exit_for_10xMOIC
    # high_alt_output5x = ControlCompanyHigh.required_exit_for_5xMOIC
    
    return render_template('home/index.html', segment='index')    

@blueprint.route('/results', methods = ["POST", "GET"])
@login_required
def results():

    form = CalculationForm(request.form)

    given_dilution_estimate = int(request.form.get("user_dilution_estimate"))

    TestCompany = Calculator(request.form.get("company name"), float(request.form.get("tam")), float(request.form.get("sam")), float(request.form.get("som")), float(request.form.get("round_size")), float(request.form.get("premoney")), float(request.form.get("sales_multiple")), float((int(request.form.get("user_dilution_estimate"))/100)))

    ControlCompanyLow = Calculator('Control Low', 1000000000, 500000000, 50000000, 2000000, 3000000, 5, 0.5)

    ControlCompanyHigh = Calculator('Control High', 1000000000, 500000000, 50000000, 2000000, 10000000, 5, 0.5)

    user_pre_mon_val = TestCompany.Seed_premoney
    user_post_money_val = TestCompany.Seed_postmoney
    user_round_size = TestCompany.Seed_roundamt
    output40x = TestCompany.required_exit_for_40xMOIC
    output20x = TestCompany.required_exit_for_20xMOIC
    output10x = TestCompany.required_exit_for_10xMOIC
    output5x = TestCompany.required_exit_for_5xMOIC
    sales_multiple = TestCompany.sales_multiple

    tam_text = TestCompany.tam
    sam_text = TestCompany.sam
    som_text = TestCompany.som

    required_sales_annual_sales_text = TestCompany.required_annual_sales

    sam_pct40x = ((TestCompany.required_exit_for_40xMOIC / TestCompany.sam) * 100)

    tam_pct_sam = ((TestCompany.sam / TestCompany.tam) * 100)

    low_tam_text = ControlCompanyLow.tam
    low_sam_text = ControlCompanyLow.sam
    low_som_text = ControlCompanyLow.som

    high_tam_text = ControlCompanyHigh.tam
    high_sam_text = ControlCompanyHigh.sam
    high_som_text = ControlCompanyHigh.som

    pct_40x_post = (TestCompany.Seed_postmoney / TestCompany.som) * 100

    low_alt_output40x = ControlCompanyLow.required_exit_for_40xMOIC
    low_alt_output20x = ControlCompanyLow.required_exit_for_20xMOIC
    low_alt_output10x = ControlCompanyLow.required_exit_for_10xMOIC
    low_alt_output5x = ControlCompanyLow.required_exit_for_5xMOIC
 
    high_alt_output40x = ControlCompanyHigh.required_exit_for_40xMOIC
    high_alt_output20x = ControlCompanyHigh.required_exit_for_20xMOIC
    high_alt_output10x = ControlCompanyHigh.required_exit_for_10xMOIC
    high_alt_output5x = ControlCompanyHigh.required_exit_for_5xMOIC

    return render_template('home/index.html', segment='index', dilution_estimate=(f"previous input: {given_dilution_estimate}"), round_size=(f"previous input: {user_round_size}"), sales_multiple_text = (int(sales_multiple)), sales_multiple = (f"Previous Input: {sales_multiple}"), pre_mon_val=(f"previous input: {user_pre_mon_val}"), calculation_text40x='{:,.0f}'.format(output40x), calculation_text20x='{:,.0f}'.format(output20x), calculation_text10x='{:,.0f}'.format(output10x), calculation_text5x='{:,.0f}'.format(output5x), user_post_mon_val='{:,.0f}'.format(user_post_money_val), low_output_text40x='{:,.0f}'.format(low_alt_output40x), low_output_text20x='{:,.0f}'.format(low_alt_output20x), low_output_text10x='{:,.0f}'.format(low_alt_output10x), low_output_text5x='{:,.0f}'.format(low_alt_output5x), sam_pct40x_text = '{:,.0f}'.format(sam_pct40x), high_output_text40x='{:,.0f}'.format( high_alt_output40x), high_output_text20x='{:,.0f}'.format( high_alt_output20x),  high_output_text10x='{:,.0f}'.format( high_alt_output10x),  high_output_text5x='{:,.0f}'.format(high_alt_output5x), tam_text='{:,.0f}'.format(tam_text), sam_text='{:,.0f}'.format(sam_text), som_text='{:,.0f}'.format(som_text), tam_pct_sam_text='{:,.0f}'.format(tam_pct_sam), pct_40x_post_text='{:,.0f}'.format(pct_40x_post), required_sales_annual_sales = (f"Previous Input: {required_sales_annual_sales_text}"), required_sales_annual_sales_text1 = '{:,.0f}'.format((int(required_sales_annual_sales_text))))


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
