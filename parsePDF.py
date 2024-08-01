import tabula
import concurrent.futures

result = []

def process_page(page_number):
    dfs = tabula.read_pdf("GPAT.pdf", pages=f"{page_number}", multiple_tables=True)
    output = []
    df = dfs[0]
    data = df.columns.to_list()
    
    if data[2] == "ST" and data[5] != "ABSENT" and data[5] != "NOT QUALIFIED":
        output.append(data[0:6])

    
    if data[8] == "ST" and data[10] != "ABSENT" and data[11] != "NOT QUALIFIED":
        output.append(data[6:])
    
    ind = 0
    while df.empty != True:
        data = df.loc[ind].to_list()
        df = df.drop(ind)
        ind += 1
        
        if data[2] == "ST" and data[5] != "ABSENT" and data[5] != "NOT QUALIFIED":
            output.append(data[0:6])
        
        
        if data[8] == "ST" and data[10] != "ABSENT" and data[11] != "NOT QUALIFIED":
            output.append(data[6:])
    print("Page", page_number, "done.")
    return output
        

if __name__ == "__main__":
    for i in range(1, 406):
        result += process_page(i)

    with open("ST_candidates_selected.txt", "w") as fh:
        for data in result:
            buff = f"{data[0]}\t{data[1]}\t{data[2]}\t{data[3]}\t{data[4]}\t{data[5]}\n"
            fh.write(buff)