def create_harvester_table(pdf, data):
    pdf.multi_cell(0, 5, f"TheHarvester was also able to discovere {len(data['ips'])} IP addresses connected to the specified domain and they are displayed in the following table: ")
    pdf.ln(8)
    
    pdf.set_font('Times', 'B', 10)
    pdf.set_fill_color(0, 0, 0)
    
    ips_table = [[]]
    i, j = 0, 0
    for item in data['ips']:
        ips_table[i].append(item)
        j+=1
        if (j%5 == 0 and not len(data['ips']) == j):
            ips_table.append([])
            i+=1
    
    with pdf.table(text_align="CENTER") as table:
        for data_row in ips_table:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
        
    hosts_table = [('Subdomain', 'IP')]
    for item in data['hosts']:
            info = item.split(':')
            if len(info) > 1:
                hosts_table.append((info[0], info[1]))
            else:
                hosts_table.append((info[0], '-'))
    
    pdf.set_font('Times', '', 12)
    pdf.ln(8)
    pdf.multi_cell(0, 5, "Furthermore, theHarvester recovered the hosts connected to this domain. The table below presents the subdomains and ip addresses for each of the hosts: ")
    pdf.ln(8)
    pdf.set_font('Times', '', 10)
    
    with pdf.table(text_align="CENTER") as table:
        for data_row in hosts_table:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
                
def create_amass_table(pdf, data):
    amass_table = [('Subdomain', 'Domain', 'Tag', 'Sources')]
    addr_table = [("Subdomain", "Ip", "Cidr", "Asn", "Description")]
    for key, value in data.items():
        amass_table.append((key, value['domain'], value['tag'], ', '.join(value['sources'])))
        for addr in value['addresses']:
            addr_table.append((key, addr['ip'], addr['cidr'], str(addr['asn']), addr['desc']))
     
    pdf.set_font('Times', '', 10)
    pdf.set_fill_color(0, 0, 0)
    
    with pdf.table(text_align="CENTER") as table:
        for data_row in amass_table:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    
    pdf.set_font('Times', '', 12)
    pdf.ln(8)
    pdf.multi_cell(0, 5, "Moreover, for each of the above subdomains, Amass was able to discover the IPS, Classless Inter-Domain Routing information (CIDRs), Autonomous System Numbers (ASNs) and descriptive information for every address involved:")
    pdf.ln(8)
    pdf.set_font('Times', '', 10)
                
    with pdf.table(text_align="CENTER") as table:
        for data_row in addr_table:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

def create_table(pdf, title, data):
    if title == 'TheHarvester Results':
        create_harvester_table(pdf, data)
    elif title == 'Amass Results':
        create_amass_table(pdf, data)