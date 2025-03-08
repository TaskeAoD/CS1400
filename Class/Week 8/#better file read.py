#better file read

try:
    with open('mydata.data') as f:
        sum = 0
        try:
            for line in f:
                sum += int(line)
        except Exception as er:
            print(er)
        print(f'sum = {sum}')
except:
    print('failed')
        