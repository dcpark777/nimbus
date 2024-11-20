import yaml
from typing import Any, Dict, List, Type
import inspect

class PluginExporter:
    @staticmethod
    def _get_class_params(cls: Type) -> Dict[str, Any]:
        """Extract initialization parameters from a class."""
        signature = inspect.signature(cls.__init__)
        params = {}
        
        for name, param in signature.parameters.items():
            if name == 'self':
                continue
            
            param_info = {
                'type': str(param.annotation.__name__) if param.annotation != inspect.Parameter.empty else 'Any',
                'default': None if param.default == inspect.Parameter.empty else param.default,
                'required': param.default == inspect.Parameter.empty
            }
            params[name] = param_info
            
        return params

    @staticmethod
    def export_plugin(cls: Type) -> Dict[str, Any]:
        """Export a single plugin class to a dictionary format."""
        return {
            'name': cls.__name__,
            'type': cls.__base__.__name__,
            'module': cls.__module__,
            'parameters': PluginExporter._get_class_params(cls),
            'doc': cls.__doc__ or ''
        }

    @classmethod
    def export_to_yaml(cls, plugins: List[Type], output_file: str) -> None:
        """Export all plugins to YAML format."""
        exported = {
            'version': '1.0',
            'plugins': [cls.export_plugin(plugin) for plugin in plugins]
        }
        
        with open(output_file, 'w') as f:
            yaml.dump(exported, f, default_flow_style=False, sort_keys=False)