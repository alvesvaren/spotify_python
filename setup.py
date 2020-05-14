import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="spotify_python",
    version="0.0.3",
    author="Alve Svarén",
    author_email="alve@hotmail.se",
    description="A dbus spotify client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvesvaren/spotify_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
