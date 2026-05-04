from deerflow.tools import get_available_tools
from deerflow.tools.builtins import setup_agent


def resolve_tools(
    supports_tools: bool,
    is_bootstrap: bool,
    model_name: str,
    subagent_enabled: bool,
    agent_config=None,
):
    if not supports_tools:
        return []

    if is_bootstrap:
        return get_bootstrap_tools(model_name, subagent_enabled)

    return get_base_tools(model_name, subagent_enabled, agent_config)


def get_base_tools(model_name: str, subagent_enabled: bool, agent_config=None):
    return get_available_tools(
        model_name=model_name,
        groups=(agent_config.tool_groups if agent_config else None),
        subagent_enabled=subagent_enabled,
    )


def get_bootstrap_tools(model_name: str, subagent_enabled: bool):
    return get_available_tools(
        model_name=model_name,
        subagent_enabled=subagent_enabled,
    ) + [setup_agent]
