#!/usr/bin/env python

import json
import csv
import click
from pathlib import Path
from tabulate import tabulate

def visualise(speakers, events, style): 
    flatten = []
    for speaker in speakers:
        flatten.append([speaker] + list(["Y" if v else "" for v in speakers[speaker].values()]))

    flatten = sorted(flatten)

    if style=="table":
        print(tabulate(flatten, headers=events))
    
    if style=="csv": 
        with open('results.csv', 'w') as csvfile:
            writer = csv.writer(csvfile,  delimiter="\t")
            writer.writerow(["speaker"] + events)
            writer.writerows(flatten)
 


@click.command()
@click.option('-d', '--pyvideo-data', type=click.Path(exists=True), help="Location of the PyVideo data cloned repo")
@click.option('-s', '--style', default="table", type=click.Choice(['table', 'csv']), help="Visualisation style")
@click.argument("event_search")
def cli(event_search, pyvideo_data, style):
    """Visualise event speakers from PyVideo data"""
    events = sorted([f.stem for f in list(Path(pyvideo_data).glob(f"*{event_search}*"))])
    speakers = {}

    folders = Path(pyvideo_data).glob(f"*{event_search}*")

    for folder in folders:
        event = folder.stem
        for file in Path(folder).glob("videos/*.json"):
            with open(file) as f:
                data = json.load(f)
            for speaker in data["speakers"]:
                if speaker not in speakers: 
                    speakers[speaker] = dict.fromkeys(events)
                speakers[speaker][event] = data["title"]


    visualise(events=events, speakers=speakers, style=style)


if __name__ == "__main__":
    cli()