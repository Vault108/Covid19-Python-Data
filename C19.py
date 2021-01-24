import requests
import json
import rich
from rich import print
from rich.table import Table
from rich.console import Console
CC = Console().input("[blue]Enter a Country Code: ")
Name = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["name"]
Population = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["population"]
Today_Confirmed = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["today"]["confirmed"]
Today_Deaths = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["today"]["deaths"]
Latest_Deaths = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["latest_data"]["deaths"]
Latest_Confirmed = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["latest_data"]["confirmed"]
Latest_Recovered = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["latest_data"]["recovered"]
Latest_Critical = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["latest_data"]["critical"]
Death_rate = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["latest_data"]["calculated"]["death_rate"]
Recovery_rate = requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["latest_data"]["calculated"]["recovery_rate"]
Last_updated =  requests.get('https://corona-api.com/countries/'+ CC).json()["data"]["updated_at"]

print("[bold blue]Stats For: " +  Name )
print("[blue]Total Population:", Population)
print("[blue]Cases Confirmed Today:", Today_Confirmed)
print("[blue]Deaths Today:", Today_Deaths)
print("[blue]Latest Deaths:", Latest_Deaths)
print("[blue]Latest Confirmed:", Latest_Confirmed)
print("[blue]Latest Recovered:", Latest_Recovered)
print("[blue]Latest Critial:", Latest_Critical)
print ("[blue]Death Rate: {}%".format(Death_rate))
print("[blue]Recovery_rate: {}%".format(Recovery_rate))
print("[blue]Last Updated: " + Last_updated)
