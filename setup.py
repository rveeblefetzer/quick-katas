import setuptools

setuptools.setup(
    name="quick-katas",
    version="0.1.0",
    url="https://github.com/rveeblefetzer/quick-katas",

    author="Rick Valenzuela",
    author_email="rv@rickv.com",

    description="A pair of problems and a pair of solutions",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
