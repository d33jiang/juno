import re
from typing import Callable, Dict

_str_len = len  # type: Callable[[str], int]


def get_replacer(substitutions: Dict[str, str]) -> Callable[[str], str]:
    def replace(s: str) -> str:
        return pattern.sub(lambda match: substitutions[match.group()], s)

    key_patterns = sorted(substitutions, key=_str_len, reverse=True)
    pattern = re.compile('|'.join(map(re.escape, key_patterns)))
    return replace
