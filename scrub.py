import csv


def get_csv_data(filepath):
    f = open(filepath, 'r')
    data = list(csv.DictReader(f))
    return data


def nouse(data):
    revise = []
    headers = list(data[0].keys())
    mark = True

    for i in headers:
        mark = True
        for j in range(len(data)):
            c = data[j][i]
            if len(str(c)) != 0:
                mark = False
        if mark == True:
            revise.append(headers.index(i))

    return revise

def munge(data,deletion, filepath1,filepath2):
    f1 = open(filepath1, 'r')
    f2 = open(filepath2, 'w')

    headers = list(data[0].keys())
    indexes = []
    for i in range(0,len(headers)):
        if i not in deletion:
            indexes.append(i)
    headers_ = []
    for j in indexes:
        headers_.append(headers[j])

    r = csv.reader(f1)
    w = csv.writer(f2)
    for k in r:
        w.writerow([k[i] for i in indexes])
    f2.close()


def main():
    data = get_csv_data("data/listings.csv")

    unuse = nouse(data)
    
    munge(data,unuse,"data/listings.csv","data/listings_clean.csv")
    
if __name__ == "__main__":
    main()
