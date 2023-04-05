import click
import subprocess
import pyfiglet
import shutil
from pathlib import Path
from converters.am_converter import am_converter
from converters.eh_converter import eh_converter
from converters.th_converter import th_converter
from creators.json_creator import json_creator
from creators.xml_creator import xml_creator
from creators.pdf_creator import pdf_creator
from helpers.execute_process import execute_process
from helpers.rm_artifacts import rm_artifacts

available_formats = ['json', 'xml', 'pdf']
artifacts_produced = ['th.json', 'th.xml', 'eh', 'eh.xml', 'am.json']
format_creators = {
    "json": json_creator,
    "xml": xml_creator,
    "pdf": pdf_creator
}

@click.command()
@click.option('-d', '--domain', prompt='Domain',
              help='The domain you want to gather information about.')
@click.option('-f', '--format', type=click.Choice(available_formats), multiple=True, help='Format of the output', default=available_formats)
@click.option('-o', '--output', help='Path to the output of the execution', default='./')
@click.option('-p', '--path', help='Path to the integrated tools directory', default='../tools')

def harvest(domain, output, format, path):
    """Harvest and correlate information for penetration testing."""

    # Create temp directory
    temp_path = Path("temp/")
    if not temp_path.exists(): temp_path.mkdir(parents=True)

    # ==========================================================================================================================================================================================================================

    execute_process([f'{path}/theHarvester/.venv/bin/python',f'{path}/theHarvester/theHarvester.py', '-b', "all", '-d', domain, "-f", "th"],
                                "Gathering information from theHarvester...", subprocess.DEVNULL)
    execute_process(['python3',f'{path}/EmailHarvester/EmailHarvester.py', '-d', domain, "-s", "eh", "--noprint"])
    execute_process([f'{path}/amass/amass','enum', '-d', domain, "-json", "am.json", "-timeout", "1"], "Gathering information from Amass...", subprocess.DEVNULL)

    # ==========================================================================================================================================================================================================================
        
    # Data conversion
    th_converter('th.json', './temp/harvester.json')
    eh_converter('eh.xml', './temp/emailharvester.json')
    am_converter('am.json', './temp/amass.json')

    # ==========================================================================================================================================================================================================================

    # Invoke output creators
    for item in available_formats:
        if item in format: 
            format_creators[item](domain, output)            

    # # Clean up artifacts
    rm_artifacts(artifacts_produced)

    # Remove temp directory
    if temp_path.exists() and temp_path.is_dir():
        shutil.rmtree(temp_path)

if __name__ == '__main__':
    logo = pyfiglet.figlet_format("InfoCrawler", font="big")
    print(logo)
    harvest()

    


