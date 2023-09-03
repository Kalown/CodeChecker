import re
file_path = input("Enter the file path: ")
# Define a regular expression pattern to match IP addresses and domains
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
domain_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}\b'

# Open and read the file
#file_path = 'filetest.sh'  # Replace with your file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Iterate through each line in the file
for line_number, line in enumerate(lines, start=1):
    # Search for IP addresses in the line
    ips = re.findall(ip_pattern, line)
    
    # Search for domains in the line
    domains = re.findall(domain_pattern, line)
    
    # Print the line number and the IPs/domains found
    if ips or domains:
        print(f"Line {line_number}: {line.strip()}")
        if ips:
            print(f"IP addresses: {', '.join(ips)}")
        if domains:
            print(f"Domains: {', '.join(domains)}")
        print("\n")
