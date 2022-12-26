from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='pythonFinalProject-Iteration4',
    version='0.0.4',
    author='Prasanth Yedithe',
    author_email='prasanth_yedithe@epam.com',
    license='MIT',
    description='Demo Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='<github url where the tool code will remain>',
    py_modules=['rss_reader_utility', 'rss_reader', 'Constants', 'DateUtil', 'LoggingUtil', 'RSSFeedSupport',
                'RSSFeedUtil',
                'Utils'],
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'rss_reader_utility = rss_reader_utility:main'
        ]
    },
    keywords='rss_reader_utility',
    zip_safe=False

)
