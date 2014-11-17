from distutils.core import setup
setup(
    name="chr_helpers",
    version="9999",
    description = "Helper function library for Chymera projects",
    author = "Horea Christian",
    author_email = "h.chr@mail.ru",
    url = "https://github.com/TheChymera/chr-helpers",
    download_url = "https://github.com/TheChymera/chr-helpers",
    keywords = ["library", "matplotlib", "pandas"],
    py_modules = ["chr_helpers", "chr_matplotlib"],
    classifiers = [],
    install_requires=[
	"pandas"
    ]
    )
