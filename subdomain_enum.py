import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python3 subdomain.py <domain> <subdomains_file>")
    sys.exit(1)

target_domain = sys.argv[1]
subdomains_file_path = sys.argv[2]


try:
    with open(subdomains_file_path, 'r') as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print(f"Error: The file '{subdomains_file_path}' was not found.")
    sys.exit(1)

print(f"Checking subdomains for domain: {target_domain}")
print(f"Total subdomains to check: {len(subdomains)}")


for subdomain in subdomains:
    full_domain = f"http://{subdomain}.{target_domain}"
    
    try:
        response = requests.get(full_domain)
        response.raise_for_status()
    except requests.ConnectionError:
        pass
    else:
        print("Domain:", full_domain)
