import typing as t
from collections.abc import Mapping

from ansible.plugins.inventory import BaseInventoryPlugin

class _IncludeFilter(t.TypedDict):
    include: str | bool

class _ExcludeFilter(t.TypedDict):
    exclude: str | bool

Filters = list[_IncludeFilter | _ExcludeFilter]

def parse_filters(
    filters: list[t.Any] | None,
) -> Filters: ...
def filter_host(
    inventory_plugin: BaseInventoryPlugin,
    host: str,
    host_vars: Mapping[str, t.Any],
    filters: Filters,
) -> bool: ...
