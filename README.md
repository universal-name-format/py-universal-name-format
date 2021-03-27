나 쓰려고 만듦 건들 ㄴ

# UNF: Universal Name Format

## Installation

1. Download the latest wheel file from [here](https://github.com/k44ng/universal-name-format/releases)
   
2. Execute following command on your terminal

`pip3 install unf-{downloaded version}-py3-none-any.whl`

## Examples and Common Usages

### Create the model from UNF JSON source

```python
from unf import Name

# Eastern name

me = Name({
  "name": {
    "given": "길동",
    "family": "홍"
  },
  "order": ["family", "given"],
  "encode": "eastern"
})
me.name()  # "홍길동"

# Mononym

from unf import Name

me = Name({
    "name": "Mr. Random",
    "order": [],
    "encode": "mononym"
})
me.name()  # "Mr. Random"

# Western name

me = Name({
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
})
me.name()  # "John Middle Doe"
```

### Migrate to the model from a pure string

```python
from unf.utils import eastern_to_name, mononym_to_name, western_to_name

# From an eastern name

target_string = "홍길동"
me = eastern_to_name(target_string)

# From a mononym

target_string = "k4ng"
me = mononym_to_name(target_string)

# From a western name

target_string = "John Middle Doe"
me = western_to_name(target_string)
```

### Change the name order and get its source

```python
from unf import Name
from unf.models.orders import EASTERN_ORDER

me = Name({
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
})
me.set_order(EASTERN_ORDER)  # ["family", "given"]
me.source()
# {'name': {'given': 'John', 'middle': ...
```

### Print western name as other name orders

```python
from unf import Name

me = Name({
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
})
me.name()  # "John Middle Doe"
me.name("lexical")  # "Doe, John"
me.name("eastern")  # "Doe John"
```

### Print the name as a capitalized family name

```python
from unf import Name

me = Name({
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
})
me.capital_family_name().name()  # "John Middle DOE"
```

### Print the name as a simplified middle name

```python
from unf import Name

me = Name({
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
})
me.initial_middle_name().name()  # "John M. Doe"
```

### Add honorifics with simplified given name

```python
from unf import Name

me = Name({
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
})
me.initial_given_name().prefix("Dr.").full_name()  # "Dr. J. Doe"
me.initial_given_name(include_middle=True).full_name()  # "Dr. J. Middle Doe"
```
