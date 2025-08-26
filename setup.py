from setuptools import setup, find_packages

setup(
    name="guessing_game",  # Your package name on PyPI (unique)
    version="0.1.0",       # Initial version
    author="Janki Dhanani",
    author_email="jnkdhanani@gmail.com",
    description="A simple number guessing game with difficulty levels",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-repo-name",
    packages=find_packages(),  # Automatically find packages inside /guess/
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "guessing-game=guess.game:main",  # Command-line entry point
        ],
    },
    install_requires=[
        # List dependencies here if any, e.g. "pytest", but probably none
    ],
)
