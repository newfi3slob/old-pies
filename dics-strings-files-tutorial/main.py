# CMPUT 175 - Lab 1 - Dictionaries, Strings, Files GOOD COPY
# Utilizes dictionaries, placeholders, and str formatting to meet requirements
# Nathan Juguilon

# Example 1: Python Warm-up

# creates dic. for bulb prices (Q1)
def bulb_price_dic():   
    # Q1
    bulb_prices = {'daffodil':0.35, 'tulip':0.33,   # key:value == bulb:price
                   'crocus':0.25, 'hyacinth':0.75, 
                   'bluebell':0.50}    
    return bulb_prices

# creates dic. for marys order (Q2)
def mary_order_dic():   
    # Q2
    mary_order = {'daffodil':50, 'tulip':100}   # key:value == bulb:qty    
    return mary_order

# updates tulip bulb_price by 25% rnded to 2 decimal places (Q3)
def price_update(bulb_prices):
    pct = 0.25
    init_price = bulb_prices['tulip']
    increase = init_price * pct
    total = init_price + increase
    bulb_prices['tulip'] = round(total,2)   # does rounding to 2 decimals
    
# adds key:value pair to marys order dic. (Q4)
def mary_order_update(mary_order):
    mary_order['hyacinth'] = 30    
    
# ORGANIZES + SORTS marys order (Q5.1) // calculates total bulbs + cost (Q6.1)
def organize_sort_order(bulb_prices, mary_order):
    bulb_tot = 0    
    receipt_tot = 0     # Q6 totals calculated in creating Q5 receipt
    receipt = []
    for flower in mary_order:   # organizes line by line (flower by flower)
        bulb_qty = mary_order[flower]
        bulb_price = bulb_prices[flower]
        bulb_code = flower[:3]
        subtotal = bulb_qty * bulb_price
        bulb_tot += bulb_qty    # ADDS amounts to the totals for Q6
        receipt_tot += subtotal
        line = '%-5s *%4d = $%6.2f' % (bulb_code.upper(), bulb_qty, subtotal)
        receipt.append(line)
    receipt.sort()  # SORTS receipt
    return receipt, bulb_tot, receipt_tot

# DISPLAYS/PRINTS marys purchase receipt (Q5.2)
def display_print_receipt(receipt):
    intro = 'You have purchased the following bulbs:'
    print(intro)
    for line in receipt:
        print(line)
        
# DISPLAY/PRINT totals for receipt bottom (Q6.2)
def display_print_receipt_totals(bulb_tot, receipt_tot):
    outro_P1 = '\nThank you for purchasing %d bulbs from Bluebell Greenhouses.' % bulb_tot
    outro_P2 = 'Your total comes to $%6.2f.' % receipt_tot
    print(outro_P1,outro_P2, sep = '\n')
     
# Example 2A: Rainfall

# reads txt file and returns its CONTENTS
def read_file():
    filename = 'rainfall.txt'
    filemode = 'r'
    file = open(filename, filemode)
    contents = file.read()
    file.close()        
    return contents

# split CONTENTS into rainfall data dic. SORTED in asc. order
def create_rain_dic():
    contents = read_file()
    contents = contents.split('\n')
    rainfall_data = {}
    for info in contents:
        key, value = info.split()
        rainfall_data[key] = float(value)   # converts str value to float value
        
    # sorted method takes the rain data (rain[1]) and sorts + creates dic. (dict)
    rainfall_data = dict(sorted(rainfall_data.items(), key = lambda rain:rain[1])) 
    return rainfall_data
    
# data processing; GROUPS annual rainfall into seperate categories
def process_data(rainfall_data):
    sixty_mm = []
    seventy_mm = []  
    eighty_mm = []
    ninety_mm = []
    for city in rainfall_data:  # appends data pairs to appropriate categories
        rain_amt = rainfall_data[city]
        pair = (city, rain_amt)  
        if rain_amt < 60:
            sixty_mm.append(pair)   
        elif rain_amt < 70:
            seventy_mm.append(pair)
        elif rain_amt < 80:
            eighty_mm.append(pair)
        else:
            ninety_mm.append(pair)   
    processed_data = (sixty_mm, seventy_mm, eighty_mm, ninety_mm)  # list of lists
    return processed_data
    
# writes PROCESSED DATA into a new txt file
def write_file(processed_data):
    filename = 'rainfallfmt.txt'
    filemode = 'w'
    file = open(filename, filemode)  
    category_strs = ('50-60','60-70','70-80','80-90')
    for i in range(len(processed_data)):
        category = category_strs[i]  # grabs category name fr/list
        header = '[%s mm)\n' % category
        file.write(header)
        for key,value in processed_data[i]:
            city = key.upper()  # transforms string to UPPERCASE
            rain = float(value)  # turns into float in case of 'input errors'
            body = '%25s %-5.1f\n' % (city.center(25),rain)  # .center() method 
            file.write(body)
    file.close()
    
def main():
    bulb_prices = bulb_price_dic()
    mary_order = mary_order_dic()
    price_update(bulb_prices)
    mary_order_update(mary_order)
    receipt = (organize_sort_order(bulb_prices, mary_order)[0])
    display_print_receipt(receipt)
    bulb_tot = (organize_sort_order(bulb_prices, mary_order)[1])
    receipt_tot = (organize_sort_order(bulb_prices, mary_order)[2])
    display_print_receipt_totals(bulb_tot, receipt_tot)
    rainfall_data = create_rain_dic()
    processed_data = process_data(rainfall_data)
    write_file(processed_data)
main()