from src.mas.agents import load_agent_mapping


def get_prompt(history, user_input) -> str:
    if len(history) == 0:
        return f"The user has given the following request: {user_input}."
    
    # Else
    new_prompt = f"The user has given the following initial request: {user_input}.\n The following is the history of responses of the various agents that have acted so far on this request:\n"
    for agent, response, next_agent in history:
        new_prompt += f"Agent {agent} instructed agent {next_agent}: {response}\n"

    return new_prompt


def get_system_response(user_input: str) -> tuple[str, list[tuple[str, str, str]]]:
    agent_mapping = load_agent_mapping()
    current_agent = 'supervisor_agent'
    history = []
    
    for _ in range(10): # Limit number of possible iterations
        prompt = get_prompt(history, user_input)
        
        result = agent_mapping[current_agent].run_sync(prompt)

        history.append((current_agent, result.output.response, result.output.goto))
        current_agent = result.output.goto

        if result.output.goto == 'user':
            break

    return history[-1][1], history