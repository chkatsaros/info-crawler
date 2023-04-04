import click
import subprocess
from converters.eh_converter import eh_converter
from converters.th_converter import th_converter
import pyfiglet
import time
from pathlib import Path

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
def harvest(domain):
    """Harvest and correlate information for penetration testing."""
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

# TODO: add --output-path -o click.option for the output

# TODO: add --type -tclick.option for the output type(s)

# TODO: add --tools-path -p click.option for the tools path

if __name__ == '__main__':
    logo = pyfiglet.figlet_format("InfoCrawler", font="big")
    print(logo)

    path = Path.home().joinpath('info-crawler-output/')
    if not path.exists():
        path.mkdir(parents=True)
    harvest()


