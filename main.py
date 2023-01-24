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
    theHarvesterProcess = subprocess.Popen(['/usr/bin/theHarvester', '-b', "all", '-d', domain, "-f", f"~/info-crawler-output/{domain}"])
    try:
        theHarvesterProcess.wait()
    except KeyboardInterrupt:
        theHarvesterProcess.kill()

# TODO: add --path click.option for the output

# TODO: add --type click.option for the output type(s)

if __name__ == '__main__':
    logo = pyfiglet.figlet_format("InfoCrawler", font="big")
    print(logo)

    time.sleep(3)

    output_dir = os.path.expanduser('~/info-crawler-output')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    # TODO: add more tools to correlate
    harvest()


