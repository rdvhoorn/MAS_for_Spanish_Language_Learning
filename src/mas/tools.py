from typing import Callable, List

def get_grammar_concept_proficiency() -> str:
    return """
    Current user's level of Spanish proficiency in grammar:
    - Verb conjugation: not yet started
    - Past tense: not yet started
    - Present perfect: not yet started
    - Present participle: not yet started
    - Preterite: not yet started
    - Future: not yet started
    - Conditional: not yet started
    - Imperative: not yet started
    """

def get_tool_list_from_list_of_strings(list_of_tools: list[str]) -> List[Callable]:
    # Gets list of functions as strings (['get_grammar_concept_proficiency'])
    # Returns list of functions (get_grammar_concept_proficiency)
    return [globals()[tool] for tool in list_of_tools]
