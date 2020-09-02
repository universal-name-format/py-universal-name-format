나 쓰려고 만듦 건들 ㄴ

# Universal Name Format

## Examples

### Case: Western Name

```json
{
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "western"
}
```

### Case: Eastern Name

```json
{
  "name": {
    "given": "길동",
    "family": "홍"
  },
  "order": ["family", "given"],
  "encode": "eastern"
}
```

### Case: Mononym

```json
{
    "name": "Mr. Random",
    "order": [],
    "encode": "mononym"
}
```
