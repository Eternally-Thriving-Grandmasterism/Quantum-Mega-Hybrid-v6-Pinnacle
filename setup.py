from setuptools import setup, find_packages

setup(
    name="quantum-mega-hybrid-v6",
    version="6.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "torch>=2.0.0",
        "chess>=1.10.0",
        "qutip>=4.7.0",
        "astropy>=5.0"
    ],
    description="Quantum Mega Hybrid v6 Pinnacle - Universal thriving alchemist",
    author="Eternally-Thriving-Grandmasterism",
    license="MIT",
)
