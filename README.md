# Datoma
[Datoma](https://datoma.cloud/) is a cloud computing web service solution that offers experimental scientists a fast and easy way to analyze mass spectrometry-based metabolomics data for free, while giving code developers the opportunity to increase visibility and usability of their code.
This Python module enables users to use the platform programmatically: upload files, launch new jobs and create custom metabolomics workflows from existing tools. Check out the documentation [here](https://datoma.readthedocs.io/en/latest/index.html#).

# Install
The library package is listed on [PyPI](https://pypi.org/project/datoma/).\
You install it by using the following command:\

    pip install datoma

# Configure
This is the step where you can specify if you have developer access. If you don't, please refrain from using the `--dev` flag.

```bash
$ python3 -m datoma login [--email <email>] [--password <password>] [--dev]
