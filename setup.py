from setuptools import setup, find_packages
setup(
      name="logger",
      version="0.4",
      description="logger",
      author="Edwin.JH.Lee",
      url="http://github.com/lteam/logger-python",
      license="Apache Lisence 2",
      packages= find_packages(),
      scripts=["logger/logger.py"],
      )