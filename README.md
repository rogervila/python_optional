# Python Optional

Returns `None` if a dict key does not exist


## Install

```sh
pip install python_optional
```

## Usage

```py
from python_optional import optional

data = {
    'a' : 'b'
}

result = optional(data).get('a') # 'b'
result = optional(data).get('z') # None
```
