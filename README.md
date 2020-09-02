나 쓰려고 만듦 건들 ㄴ

# Universal Name Format

## Example

### JSON Format

```json
{
  "name": {
    "given": "John",
    "middle": "Middle",
    "family": "Doe"
  },
  "order": ["given", "middle", "family"],
  "encode": "latin"
}
```

```json
{
  "name": {
    "given": "길동",
    "middle": "",
    "family": "홍"
  },
  "order": ["family", "given"],
  "encode": "hangul"   
}
```