totalsales = [0]*8
with open('carSale.csv') as pseudocsv:
    while 1:
        try:
            _manufacturer=pseudocsv.readline()
            sales=map(int,pseudocsv.readline().split(','))
            i=0
            for sale in sales:
                totalsales[i]+=sale
                i+=1
        except:
            print(totalsales)
            print(sum(totalsales))
            break
