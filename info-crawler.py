#!/usr/bin/env python3
import click
import subprocess
import pyfiglet
import shutil
from pathlib import Path

from converters import am_converter
from converters import eh_converter
from converters import th_converter
from creators import json_creator
from creators import xml_creator
from creators import pdf_creator
from helpers import execute_process

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
@click.option('-e', '--encryption', help='Password to protect produced PDF', default="")

def harvest(domain, output, format, path, encryption):
    """Harvest and correlate information for penetration testing."""

    # Create temp directory
    temp_path = Path("temp/")
    if not temp_path.exists(): temp_path.mkdir(parents=True)

    # ==========================================================================================================================================================================================================================

    execute_process([f'theHarvester', '-b', "all", '-d', domain, "-f", "th"],
                                "Gathering information from theHarvester...", subprocess.DEVNULL)
    execute_process([f'emailharvester', '-d', domain, "-s", "eh", "--noprint"])
    execute_process([f'amass','enum', '-d', domain, "-json", "am.json", "-timeout", "1"], "Gathering information from Amass...", subprocess.DEVNULL)

    # ==========================================================================================================================================================================================================================
        
    # Data conversion
    th_converter('th.json', './temp/harvester')
    eh_converter('eh.xml', './temp/emailharvester')
    am_converter('am.json', './temp/amass')

    # ==========================================================================================================================================================================================================================
    
    for file in artifacts_produced:
        shutil.move(file, './temp/')
    
    # Invoke output creators
    print('Deleting artifacts...')
    for f in available_formats:
        if f in format: 
            if f == 'pdf': 
                format_creators[f](domain, output, encryption)
            else:
                format_creators[f](domain, output)          

    # Remove temp directory
    if temp_path.exists() and temp_path.is_dir():
        shutil.rmtree(temp_path)

if __name__ == '__main__':
    logo = pyfiglet.figlet_format("InfoCrawler", font="big")
    print(logo)
    harvest()

    


