import functools
import inspect
from typing import Any, Type, Dict, List

_EXPORT_REGISTRY: List[Type] = []

def export(cls: Type) -> Type:
    """Decorator to mark Airflow plugin classes for YAML export."""
    _EXPORT_REGISTRY.append(cls)
    return cls

def get_registered_plugins() -> List[Type]:
    """Get all registered plugin classes."""
    return _EXPORT_REGISTRY.copy()