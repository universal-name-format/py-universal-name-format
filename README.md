나 쓰려고 만듦 건들 ㄴ

# UNF: Universal Name Format

## Installation

1. Download latest wheel file from [here](https://github.com/k44ng/universal-name-format/releases)
   
2. Execute following command on your terminal

`pip3 install unf-{downloaded version}-py3-none-any.whl`

## Examples

### Case: Western Name

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
```

### Case: Eastern Name

```python
from unf import Name

me = Name({
  "name": {
    "given": "길동",
    "family": "홍"
  },
  "order": ["family", "given"],
  "encode": "eastern"
})
me.name()  # "홍길동"
```

### Case: Mononym

```python
from unf import Name

me = Name({
    "name": "Mr. Random",
    "order": [],
    "encode": "mononym"
})
me.name()  # "Mr. Random"
```
