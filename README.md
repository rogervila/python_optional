# Python Optional

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rogervila_python_optional&metric=alert_status)](https://sonarcloud.io/dashboard?id=rogervila_python_optional)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=rogervila_python_optional&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=rogervila_python_optional)


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
