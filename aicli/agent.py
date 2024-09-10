import os
import subprocess
from pathlib import Path

from GeneralAgent import Agent

from aicli.conf import settings
from aicli.role import SYSTEM_PROMPT


def run_command(command: str):
    # run command use subprocess and return the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout


agent = Agent(
    role=SYSTEM_PROMPT,
    workspace=Path(os.getcwd()) / ".workspace",
    functions=[run_command],
    api_key=settings.api_key,
    base_url=settings.base_url,
    model=settings.model,
)

if __name__ == "__main__":
    ret = agent.user_input("use du tell me the size of pwd")
    print(ret)
