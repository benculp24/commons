import string

vals = list(string.ascii_uppercase) + list(string.digits)

for d1 in vals:
    for d2 in vals:
        for d3 in vals:
            for d4 in vals:
                code = 'AS3' + d1 + 'A' + d2 + d3 + d4 + 'EM6XYA4'
                print(code)