import re
for i in range(int(input('enter how many credit card nums want to validate'))):
    S = input('enter credit card number').strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        print ('Invalid' if final_match else 'Valid')
    else:
        print ('Invalid')
