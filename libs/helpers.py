from aries_cloudcontroller import AriesAgentController
import ast
import asyncio
import json
from pprintpp import pprint
import requests
from termcolor import colored

def get_identifiers() -> dict:
    """
    Opens identifiers.json file to get newest scheme_id, cred_def_id, and authority_did as defined in the
    authority agent's init_authority_as_issuer.ipynb notebook
    Returns: (dict) relevant identifiers
    """
    with open("libs/identifiers.json") as f:
        identifiers = json.load(f)
        f.close()
    return identifiers


def store_identifiers(identifiers: dict):
    """
    Writes dict with newest scheme_id, cred_def_id, and authority_did to identifiers.json as defined in the
    authority agent's init_authority_as_issuer.ipynb notebook
    Args:
        identifiers: (dict) contains newe

    Returns: -

    """
    with open("libs/identifiers.json", "w") as fp:
         json.dump(identifiers, fp,  indent=4)
    print(colored("Successfully stored identifiers dictionary in libs/identifiers.json.", "green", attrs=["bold"]), "(Will be needed in other notebooks and by other agents.)")
    pprint(identifiers)