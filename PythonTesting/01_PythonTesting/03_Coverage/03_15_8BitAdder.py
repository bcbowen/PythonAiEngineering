# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 17 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100% 
# statement coverage of the add8 function.

def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)

def test():
    a0 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    b0 = 0
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0
    b6 = 0
    b7 = 0
    c0 = 0

    s1 = 0 
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    c8 = 0

    def run_test(): 
        vals = [a0, a1, a2, a3, a4, a5, a6, a7, b0, b1, b2, b3, b4, b5, b6, b7, c0] 
        expected = (s1, s2, s3, s4, s5, s6, s7, s8, c8)
        result = add8(*vals)
        print(result)
        assert(result == expected)

    # run test all zeros
    run_test()

    # first bit is set for a, expect 1st bit to be set in result
    a0 = 1
    s1 = 1
    run_test()

    # first bits set for a and b, expect second bit to be set in result
    b0 = 1
    s1 = 0
    s2 = 1
    run_test()

    # second bit set for a, expect second bit in result
    a0 = 0
    b0 = 0
    s1 = 0
    a1 = 1
    run_test()

    # second bit set for a and b, third bit set in result
    b1 = 1
    s2 = 0
    s3 = 1
    run_test()

    # third bit set for a, expect third bit in result
    a1 = 0
    b1 = 0
    a2 = 1
    run_test() 

    # third bit set for a and b, expect 4th bit in result
    b2 = 1
    s3 = 0
    s4 = 1
    run_test()

    # 4bit set for a, expect 4 bit for r
    a2 = 0
    b2 = 0
    a3 = 1
    run_test()

    # 4 bit set for b, expect 5 bit for r
    b3 = 1
    s4 = 0
    s5 = 1
    run_test()

    ################3

    # 5 bit set for a, expect 5 bit for r
    a3 = 0
    b3 = 0
    a4 = 1
    run_test()

    # 5 bit set for b, expect 6 bit for r
    b4 = 1
    s5 = 0
    s6 = 1
    run_test()

    # 6 bit set for a, expect 6 bit for r
    a4 = 0
    b4 = 0
    a5 = 1
    run_test()

    # 6 bit set for b, expect 7 bit for r
    b5 = 1
    s6 = 0
    s7 = 1
    run_test()

    # 7 bit set for a, expect 7 bit for r
    a5 = 0
    b5 = 0
    a6 = 1
    run_test()

    # 7 bit set for b, expect 8 bit for r
    b6 = 1
    s7 = 0
    s8 = 1
    run_test()

    # 8 bit set for a, expect 8 bit for r
    a6 = 0
    b6 = 0
    a7 = 1
    run_test()

    # 8 bit set for b, expect c bit for r
    b7 = 1
    s8 = 0
    c8 = 1
    run_test()


test()


