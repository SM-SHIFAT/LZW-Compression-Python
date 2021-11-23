# LZW-Compression-Python


Data: ababbabcababba

<table><thead><tr><th> encode </th><th>Subject Code</th><th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lib&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th></tr></thead><tbody><tr><td>-</td><td>0</td><td>a</td></tr><tr><td>-</td><td>1</td><td>b</td></tr><tr><td>-</td><td>2</td><td>c</td></tr><tr><td>0</td><td>3</td><td>ab</td></tr><tr><td>1</td><td>4</td><td>ba</td></tr><tr><td>3</td><td>5</td><td>abb</td></tr><tr><td>4</td><td>6</td><td>bab</td></tr><tr><td>1</td><td>7</td><td>bc</td></tr><tr><td>2</td><td>8</td><td>ca</td></tr><tr><td>3</td><td>9</td><td>aba</td></tr><tr><td>5</td><td>10</td><td>abba</td></tr><tr><td>0</td><td>11</td><td>-</td></tr></tbody></table>

Encoded Output:
```python
abc
0 1 3 4 1 2 3 5 0
```

