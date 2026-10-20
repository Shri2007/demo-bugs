# Can't open the last page of results

When I browse a category with more than one page of products, I can never get
to the final page. The page counter says "Page 2 of 3", but clicking "Next"
from page 2 gives an error instead of the remaining products.

Steps to reproduce:

```python
from pagination import get_page, total_pages

items = list(range(25))
total_pages(len(items), 10)   # 3
get_page(items, 3, 10)        # ValueError: page 3 out of range (1..3)
```

The error message even says 3 is in range, so this seems wrong. I'd expect
page 3 to return the last 5 items.

Also: when there are only a few products (one page total), I get the same
error just opening the category on page 1.
