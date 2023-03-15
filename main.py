import click
import subprocess
import pyfiglet
import os
import time


@click.command()
@click.option('-d', '--domain', prompt='Domain',
              help='The domain you want to gather information about.')
def harvest(domain):
    """Harvest and correlate information for penetration testing."""
    try:
        harvester_process = subprocess.Popen(['../tools/theHarvester/.venv/bin/python','../tools/theHarvester/theHarvester.py', '-b', "all", '-d', domain, "-f", f"~/info-crawler-output/{domain}-harvester"])
        harvester_process.wait()
        emailharvester_process = subprocess.Popen(['python3','../tools/EmailHarvester/EmailHarvester.py', '-d', domain, "-s", f"~/info-crawler-output/{domain}-emailharvester"])
        emailharvester_process.wait()
    except KeyboardInterrupt:
        harvester_process.kill()
        emailharvester_process.kill()

    # h8mailProcess = subprocess.Popen(
    #     ['h8mail', '-t', domain, '--loose'])
    # try:
    #     h8mailProcess.wait()
    # except KeyboardInterrupt:
    #     h8mailProcess.kill()

# TODO: add --output-path -o click.option for the output

# TODO: add --type -tclick.option for the output type(s)

# TODO: add --tools-path -p click.option for the tools path


if __name__ == '__main__':
    logo = pyfiglet.figlet_format("InfoCrawler", font="big")
    print(logo)

    time.sleep(3)

    output_dir = os.path.expanduser('~/info-crawler-output')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    # TODO: add more tools to correlate
    harvest()


