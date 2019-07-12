import csv
import usaddress

# Open the input CSV file with the messy address data
f = open('Addresses.csv')
csv_f = csv.reader(f)
# Some of the addresses don't match the typical format we're seeing in this file...
special_address_starts = ['PO Box','P.O. Box','One Audubon','1St.','One Nolte','40-5th','4335-A','Center2050']
# And let's prepare now to write the output CSV later
output_file = open('parsed_addresses.csv', mode='w', newline='')
output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
output_writer.writerow(['NAME','ADDRESS','ADDRESS','CITY','STATE','ZIPCODE','RAWDATA'])
# Loop over every row in the input CSV
for counter, row in enumerate(csv_f):
    # Skip any rows that effectively don't have data
    if len(row[0]) == 0:
        continue
    raw_data = row[0]
    this_name = ''
    raw_address = ''
    for entry in special_address_starts:
        if entry in raw_data:
            this_name = raw_data.split(entry)[0]
            raw_address = entry + raw_data.split(entry)[1]
            break
    if len(raw_address) == 0:
        raw_data_split = raw_data.split(' ')
        found_address_start = False
        for entry in raw_data_split:
            if found_address_start:
                raw_address += entry + ' '
            else:
                if entry.replace('-','').isdigit():
                    found_address_start = True
                    this_name = this_name[:-1]
                    raw_address = entry + ' '
                else:
                    this_name += entry + ' '
        raw_address = raw_address[:-1]
    if this_name[-1] == ' ':
        this_name = this_name[:-1]
    address1 = ''
    address2 = ''
    city = ''
    state = ''
    zipcode = ''
    parsed_address = usaddress.parse(raw_address)
    if len(parsed_address) < 5:
        output_writer.writerow([raw_data,'','','','','',''])
    else:
        zipcode = parsed_address[-1][0]
        state = parsed_address[-2][0]
        city = parsed_address[-3][0]
        city = city.replace(',','')
        # Trim the parsed address now that we have those things
        parsed_address = parsed_address[:-3]
        for entry in parsed_address:
            address1 += entry[0] + ' '
        address1 = address1[:-1]
        if ',' in address1:
            address2 = ' '.join(address1.split(',')[1:])
            address1 = address1.split(',')[0]
        output_writer.writerow([this_name,address1,address2,city,state,zipcode,raw_data])
