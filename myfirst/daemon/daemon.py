import time
import click

data = {
    "init": [
        "Processing... 10%",
        "Processing... 20%",
        "Processing... 30%",
        "Processing... 60%",
        "Processing... 90%",
        "Processing... 99%",
        "Deamon installed"
    ],
    "status": ["OK"]
}


@click.command()
@click.argument('command', required=True)
@click.option('--ip', required=False, help='IP address for the initialization')
@click.option('--key', required=False, help='Key for secure access')
def run_process(command, ip, key):
    """
    This CLI tool simulates a process that updates its output over time,
    overwriting its previous output in the terminal.
    """
    outputs = data.get(command, ["No such process."])

    for output in outputs:
        click.echo('\r' + output + ' ' * 20, nl=False)  # Clear remaining characters
        time.sleep(0.7564)  # Delay to simulate processing time
    click.echo()  # Move to new line after completion


if __name__ == '__main__':
    run_process()
