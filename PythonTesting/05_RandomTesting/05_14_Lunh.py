# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.
def is_luhn_valid(val):
    if val == None or len(val) < 3: 
        return False
    val = str(val)
    n = len(val)
    total = 0
    is_even = n % 2 == 0

    i = 0
    while i < len(val): 
        digit = int(val[i])
        if (is_even and i % 2 == 0) or (not is_even and i % 2 == 1): 
            digit *= 2
            if digit > 9: 
                digit -= 9
    
        total += digit
        i += 1
    
    return total % 10 == 0
    

"""
    Visa	4242424242424242	Any 3 digits	Any future date
    Visa (debit)	4000056655665556	Any 3 digits	Any future date
    Mastercard	5555555555554444	Any 3 digits	Any future date
    Mastercard (2-series)	2223003122003222	Any 3 digits	Any future date
    Mastercard (debit)	5200828282828210	Any 3 digits	Any future date
    Mastercard (prepaid)	5105105105105100	Any 3 digits	Any future date
    American Express	378282246310005	Any 4 digits	Any future date
    American Express	371449635398431	Any 4 digits	Any future date
    Discover	6011111111111117	Any 3 digits	Any future date
    Discover	6011000990139424	Any 3 digits	Any future date
    Discover (debit)	6011981111111113	Any 3 digits
"""
def test_validate_cc(): 
    valid_card_nums = ["4242424242424242", "4000056655665556", "5555555555554444", "2223003122003222", "5200828282828210", "5105105105105100", "378282246310005", "371449635398431", "6011111111111117", "6011000990139424", "6011981111111113"]
    invalid_card_nums = ["4242424242424249", "4000056655665559", "5555555555554449", "2223003122003229", "5200828282828219", "5105105105105109", "378282246310009", "371449635398439", "6011111111111119", "6011000990139429", "6011981111111119"]
    
    for c in valid_card_nums: 
        assert(is_luhn_valid(c))
        print(f"{c} pass")

    for c in invalid_card_nums: 
        assert(not is_luhn_valid(c))
        print(f"{c} pass")

test_validate_cc()