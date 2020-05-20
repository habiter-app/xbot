import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="x-bot", 
    version="0.0.7",
    author="Alessandro Solbiati",
    author_email="alessandro.solbiati@gmail.com",
    description="Code generation tool for translating messaging bots from one platform to another.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/habiter-app/xbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Jinja2',
        'astunparse',
        'pytest'
        ],
    python_requires='>=3.6',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
