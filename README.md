# Nimbus

A Python library for exporting Airflow plugins as YAML for DAG Factory.

## Installation

```bash
pip install nimbus
```

## Usage

1. Create your Airflow plugins and decorate them with `@nimbus.export`:

```python
import nimbus
from airflow.operators.bash import BashOperator

@nimbus.export
class MyCustomOperator(BashOperator):
    def __init__(self, custom_param: str, **kwargs):
        super().__init__(**kwargs)
        self.custom_param = custom_param
```

2. Export your plugins to YAML using the CLI:

```bash
nimbus-export your_plugin_module.py -o plugins.yaml
```

The generated YAML will contain all the necessary information for DAG Factory to use your plugins.

## Example Output

```yaml
version: '1.0'
plugins:
  - name: MyCustomOperator
    type: BashOperator
    module: your_plugin_module
    parameters:
      custom_param:
        type: str
        required: true
      bash_command:
        type: str
        required: true
    doc: Custom operator documentation
```