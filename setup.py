import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emojifyer",
    version="1.0.0",
    author="MakufonSkifto",
    description="Emojifyer is a module for emojifying text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Issue tracker": "https://github.com/MakufonSkifto/Emojifyer/issues",
        "Source": "https://github.com/MakufonSkifto/Emojifyer"
    },
    packages=setuptools.find_packages(),
    install_requires=["requests", "python-dotenv", "aiohttp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="reddit api async meme redditapi redditbot asyncreddit redditposts praw discord.py bot",
    python_requires='>=3.0',
)