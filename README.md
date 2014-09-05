#chr-helpers

The Chr (Christian/Chymera) Helpers are helper functions doing menial operations for Python scripts written by TheChymera (Horea Christian).

##Installation

####On [Gentoo Linux](http://en.wikipedia.org/wiki/Gentoo_linux) and [Derivatives](http://en.wikipedia.org/wiki/Category:Gentoo_Linux_derivatives):

The *chr-helpers* library is available in [Portage](http://en.wikipedia.org/wiki/Portage_(software)) as [dev-python/chr-helpers](https://github.com/TheChymera/chymeric/tree/master/dev-python/chr-helpers) from the Chymeric Overlay.
Just run the following command:

```
emerge chr-helpers
```

*If you are not yet using this overlay, it can be enabled with just two commands, as seen in [the README](https://github.com/TheChymera/chymeric).*

####On all other Operating Systems:

For all other Linux distributions or operating systems, the package can easily be installed via [pip](http://en.wikipedia.org/wiki/Pip_(Python)).
This also handles all Python dependencies.

```
git clone https://github.com/TheChymera/chr-helpers.git your/local/repository/path
pip install [--user] -e your/local/repository/path
```

##Dependencies

####Mandatory:
* **[pandas](https://github.com/pydata/pandas)** - in Portage as **dev-python/pandas**

####Optional:
* **[Matplotlib](http://en.wikipedia.org/wiki/Matplotlib)** - in Portage as **dev-python/matplotlib**

Released under the GPLv3 license.
Project led by Horea Christian (address all correspondence to: h.chr@mail.ru)
