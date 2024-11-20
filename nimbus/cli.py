import argparse
import importlib
import sys
from pathlib import Path
from typing import List

from . import get_registered_plugins
from .exporter import PluginExporter

def import_module(module_path: str) -> None:
    """Import a module by path."""
    try:
        importlib.import_module(module_path)
    except ImportError as e:
        print(f"Error importing module {module_path}: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(description="Export Airflow plugins to YAML")
    parser.add_argument(
        "modules",
        nargs="+",
        help="Python modules containing plugins to export"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="plugins.yaml",
        help="Output YAML file (default: plugins.yaml)"
    )
    
    args = parser.parse_args()
    
    # Import all specified modules
    for module in args.modules:
        import_module(module)
    
    # Get registered plugins and export them
    plugins = get_registered_plugins()
    if not plugins:
        print("No plugins found with @nimbus.export decorator", file=sys.stderr)
        sys.exit(1)
        
    try:
        PluginExporter.export_to_yaml(plugins, args.output)
        print(f"Successfully exported {len(plugins)} plugins to {args.output}")
    except Exception as e:
        print(f"Error exporting plugins: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()