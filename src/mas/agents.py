from pydantic import BaseModel
from pydantic_ai import Agent
from typing import Literal
import yaml
from pathlib import Path

from src.mas.tools import get_tool_list_from_list_of_strings


def create_agent_output_class(list_of_next_agents: list[str]):
    class MASAgentResponse(BaseModel):
        goto: Literal[*list_of_next_agents]  # Unpacks list into Literal values
        response: str

        def __repr__(self):
            return (
                f"MASAgentResponse(response={self.response}, next_agent={self.goto})\n"
                f"  [next_agent must be one of: {list_of_next_agents}]"
            )

    return MASAgentResponse


def create_agent(config: dict):
    return Agent(
        config['model'],
        system_prompt=config['system_prompt'],
        output_type=create_agent_output_class(config['next_agents']),
        tools=get_tool_list_from_list_of_strings(config['tools'])
    )


def load_agent_configs() -> list[dict]:
    config_path = Path('src/mas/agent_configs')
    configs = []
    for yaml_file in config_path.glob('*.yaml'):
        with open(yaml_file) as f:
            config = yaml.safe_load(f)
            configs.append(config)
    return configs


def load_agent_mapping() -> dict[str, Agent]:
    agent_configs = load_agent_configs()
    return {config['name']: create_agent(config) for config in agent_configs}