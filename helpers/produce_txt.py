import json
import random
from pathlib import Path

harvester_txt = "TheHarvester is an open-source tool for gathering information about a specific target or organization. It is a command-line based tool that allows the user to search for data from various sources, including search engines, social media platforms, and DNS records. The purpose of TheHarvester is to gather information that may be useful in a security assessment or for reconnaissance purposes. It assists security professionals identify potential vulnerabilities in their organization's online presence and provide insights into how their brand is perceived online. It can also be used by attackers to gather information about a target for malicious purposes. It is able to retrieve include email addresses, domain names, subdomains, IP addresses, and employee names. The tool is highly customizable, allowing the user to specify which sources to query and which search terms to use.\n"
emailharvester_txt="EmailHarvester is also a CLI tool, which is commonly used to extract email connected to a specific domain. It is a software tool that can automatically collect email addresses from various sources, making it an efficient tool for email marketing campaigns, lead generation, and outreach efforts. The tool can extract email addresses from websites, social media platforms, and search engines using methods such as web scraping, data mining, and web crawling.\nIn order to initiate the email gathering - harvesting - process, EmailHarvester typically requires a search query, a domain name as mentioned above, or a list of URLs from the user. Once the tool is given this information, it searches web pages and social media platforms for email addresses that match the query. "
amass_txt = "Amass is another open-source tool for reconnaissance and information gathering purposes. It is designed to be a comprehensive tool that can collect information from a wide variety of sources, including DNS, web pages, and search engines. Amass is a command-line tool that can be used on Linux, macOS, and Windows. The primary purpose of Amass is to provide a comprehensive view of an organization's online presence, including its domains, subdomains, IP addresses, and other relevant information.\nIt is a powerful tool that can be used by security professionals, penetration testers, and other researchers to identify potential vulnerabilities and weaknesses in an organization's online infrastructure. Amass has a large number of features and capabilities, including the ability to perform zone transfers, brute force subdomain names, and identify subdomains that are hosted on cloud-based services. It can also use search engines such as Bing, Google, and Yahoo to find additional information about an organization.\n"

keys = {
        "harvester": ["asns", "emails", "hosts", "interesting_urls", "ips", "shodan"],
        "emailharvester": ["email"],
        "amass": ["domain", {"addresses": ["ip", "cidr", "asn", "desc"]}, "tag", "sources"]
    }

sentence_start_alternatives = ["Also for", "About the", "In regards of the", "As for the", "For the", "Regarding"]
information_collected_alternatives = ["discovered", "collected", "gathered", "was able to gather", "found", "was able to pinpoint"]

def print_list_item(file, item, pre):
    file.write(f'\n{pre}{item}\n')

def create_harvester_txt(path, data):
    th_txt = Path(path).open("w")
    th_txt.write(harvester_txt)
    for key, value in data.items():
        if not len(value) == 0 and key != 'hosts' and key != 'ips':
            th_txt.write(f'{random.choice(sentence_start_alternatives)} {key}, theHarvester {random.choice(information_collected_alternatives)} the following information: \n')
            i = 1
            for item in value:
                if key == 'interesting_urls':
                    print_list_item(th_txt, item, f"")
                else:
                    print_list_item(th_txt, item, f"{i}) ")
                i += 1
            th_txt.write("\n")    
    th_txt.close()

def create_emailharvester_txt(path, data):
    eh_txt = Path(path).open("w")
    eh_txt.write(emailharvester_txt)
    for _, value in data.items():
        if not len(value) == 0:
            eh_txt.write(f'EmailHarvester {random.choice(information_collected_alternatives)} the following information: \n')
            i = 1
            for item in value:
                eh_txt.write(f'\n        {i}) {item}\n')
                i += 1
    eh_txt.close()
    
def create_amass_txt(path):
    am_txt = Path(path).open("w")
    am_txt.write(amass_txt)
    am_txt.close()
                    
def produce_txt(data):    
    create_harvester_txt('./temp/harvester.txt', data['TheHarvester'])
    create_emailharvester_txt('./temp/emailharvester.txt', data['EmailHarvester'])
    create_amass_txt('./temp/amass.txt')
    
    