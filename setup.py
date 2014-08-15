from distutils.core import setup
setup(
    name="chr_helpers",
    packages = ["chr_helpers"], # this must be the same as the name above
    version="9999",
    description = "Helper function library for Chymera projects",
    author = "Horea Christian",
    author_email = "h.chr@mail.ru",
    url = "https://github.com/TheChymera/chr-helpers",
    download_url = "https://github.com/TheChymera/chr-helpers",
    heywords = ["library", "matplotlib", "pandas"],
    py_modules = ["chr_helpers"],
    classifiers = [],
    install_requires=[
	"pandas"
    ]
    )
