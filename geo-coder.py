import requests,csv,time
from pathlib import Path

base_url = "https://api.postcodes.io/postcodes/?filter="
filters = "postcode,longitude,latitude"

# Create Empty list which will be appened to when the CSV file is opened.
postcodes_list = []
# Create Dictionary with key of postcodes and value which is a list of postcodes.
postcodes_dict = {"postcodes": postcodes_list}
# Create variable for input and output filenames, output filename is timestamped with current time.
home = Path.home()
timestamp = time.strftime("%Y%m%d-%H%M")
filename = f"{timestamp}--postcodes-and-coordinates.csv"

input_absolute = Path(home, "geo-coder", "input", "postcodes.csv")
output_absolute = home / "geo-coder" / "output" / filename

# open CSV file, and add each postcode to the aforementioned list.
with open(input_absolute) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for row in csv_reader:
        postcodes_list.append(row["postcode"])

# API call providing aforementioned dict as payload, list of sites stored in r_list
r = requests.post(base_url + filters,json=postcodes_dict).json()
r_list = (r["result"])

address_info = []

# Iterate over list returned from API, pullling out pertintent details.
# Error-handling included in case a None data type is returned from an invalid postcode.
for p in r_list:
    try:
        address_info.append(
        {
            "postcode": p["result"]["postcode"],
            "longitude": p["result"]["longitude"],
            "latitude": p["result"]["latitude"],
        }
        )
    except TypeError:
        print(f"Postcode: {p['query']} is not valid - skipping.")
        continue

# Create .CSV file with 3 headings, and write the address-info list into each row.
with open(output_absolute, mode="w", newline="") as csv_file:
    fieldnames = ["postcode", "longitude", "latitude"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(address_info)

print(f"Script complete, file saved to {output_absolute}")