import click
import subprocess
from converters.eh_converter import eh_converter
from converters.th_converter import th_converter
import pyfiglet
import time
from pathlib import Path

available_formats = ['json', 'xml', 'pdf']

def loader(flag):
    animation_sequence = "|/-\\"
    idx = 0
    while flag:
        print(animation_sequence[idx % len(animation_sequence)], end="\r")
        idx += 1
        time.sleep(0.1)

        if idx == len(animation_sequence):
            idx = 0
    # Verify the change in idx variable
    print(f'   idx: {idx}', end='\r')

@click.command()
@click.option('-d', '--domain', prompt='Domain',
              help='The domain you want to gather information about.')
@click.option('-f', '--format', multiple=True, type=click.Choice(available_formats), help='Format of the output')
@click.option('-o', '--output', help='Path to the output of the execution')
@click.option('-p', '--path', help='Path to the integrated tools directory')

def harvest(domain, output, format, path):
    """Harvest and correlate information for penetration testing."""
    print(output,format, path)
    try:
        print("Gathering information from theHarvester...")
        harvester_process = subprocess.Popen(['../tools/theHarvester/.venv/bin/python','../tools/theHarvester/theHarvester.py', '-b', "all", '-d', domain, "-f", "th"])
        harvester_process.wait()
        print("Gathering information from EmailHarvester...")
        emailharvester_process = subprocess.Popen(['python3','../tools/EmailHarvester/EmailHarvester.py', '-d', domain, "-s", "eh"])
        emailharvester_process.wait()  
    except KeyboardInterrupt:
        harvester_process.kill()
        emailharvester_process.kill()
        
    # Data conversion
    th_converter('th.json', 'harvester.json')
    eh_converter('eh.xml', 'emailharvester.json')

if __name__ == '__main__':
    logo = pyfiglet.figlet_format("InfoCrawler", font="big")
    print(logo)
    harvest()


