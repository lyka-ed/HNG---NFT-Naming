import csv,json,hashlib

OUTPUT_FILE = 'output/output-NFT Naming csv - All Teams.csv'
f = open(OUTPUT_FILE, 'w')
writer = csv.writer(f)
writer.writerow(['S/N', 'Filename', 'UUID', 'Output File Name'])


with open('csv/NFT Naming csv - All Teams.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    next(csv_reader)
    data = [a for a in csv_reader]  
    for row in data:
        if row[1] and row[2]:
            sn = row[0]
            file_name = row[1]
            uuid = row[-1]
            nft = {
                'format' : 'CHIP-0007',
                'id' : uuid,
                'name' : file_name.replace('-',' ').title(),
                'filename': file_name,
                'description' : '',
                'minting_tool' : 'Matanmi SuperMint',
                'sensitive_content' : False,
                'series_number' : sn,
                'series_total' : data[-1][0],
                'collection' : {
                    'name' : 'NFT Collection',
                    'id' : '24f5ff82-a2f1-494e-8be5-69f1d5e42d15'
                }
            }
            jsonObj = json.dumps(nft, indent=4)
            with open(f'json/{file_name}.json', 'w') as output:
                output.write(jsonObj)
            output.close()
            hashString = hashlib.sha256(jsonObj.encode()).hexdigest()
            row.append(f'{file_name}.{hashString}.csv')
            writer.writerow(row)

f.close()
        