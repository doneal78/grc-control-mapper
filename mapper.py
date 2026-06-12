import csv
from rich import print
from rich.table import Table
from rich import box

tool_name = "GRC Control Mapper"
version = "1.0"
author = "OracleRecon"

print(f"\n[bold green]{tool_name}[/bold green]")
print(f"[dim]Version {version} | Built by {author}[/dim]\n")

controls = []

with open("controls.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        controls.append(row)

table = Table(title="Cross-Framework Control Mapping", box=box.ROUNDED)
table.add_column("Control ID", style="bold white")
table.add_column("Name", style="cyan")
table.add_column("NIST 800-53", style="green")
table.add_column("ISO 27001", style="blue")
table.add_column("SOC 2", style="magenta")

for control in controls:
    table.add_row(
        control["control_id"],
        control["name"],
        control["nist"],
        control["iso"],
        control["soc2"]
    )

print(table)