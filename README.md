# raiderio

This library is a lightweight Python client to access [Raider.IO's](https://raider.io) 
public API.

It is recommended that you look at the official [API documentation](https://raider.io/api#/) while using this client
as that will provide more details and clarity on how what fields are available and how they must be formatted.


### Installation

Install directly from PyPi (recommended):

```
pip install raiderio
```

If you want to clone the repository to make your own changes:

```
git clone https://github.com/amas0/raiderio.git
pip install ./raiderio
```

### Example Usage

Here we will show a quick example to list the current Mythic+ affixes in the US:

```python
from raiderio import RaiderIO

with RaiderIO() as rio:
    affixes = rio.get_mythic_plus_affixes(region='us')
    affix_names = [affix.get('name') for affix in affixes.get('affix_details')]
    print(affix_names)
    # prints ['Fortified', 'Sanguine', 'Grievous', 'Awakened']
```

In the prior example, we use the `RaiderIO` object as a context manager -- this is recommended
to avoid creating too many sessions and ensuring the connection closes properly when finished.
