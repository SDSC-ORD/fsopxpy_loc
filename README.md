## FSO PX Asset Locator

# About

Many statistical data in Switzerland are offered in the px file format.

They can be downloaded and used for data analysis.
The url where to download that data from is often not directly visible.
Therefore this python package helps to locate that url.

## Usage

install with your favorite package manager (pip, poetry, etc.)

```python
from fsopxpy_loc.locator import get_asset_url, FSOLocateExcetion

try:
    px_source_url = get_asset_url(pxid)
except FSOLocateExcetion:
    print("location of the px table could not be derived")
```
