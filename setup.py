from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processador_de_imagens",
    version="0.0.1",
    author="Leonardo ",
    description="Pacote de processamento de imagens feito com o skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Leo-I-G/processamento_de_imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
