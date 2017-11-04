from setuptools import setup, find_packages

setup(
    name='datasite',
    version='0.1',
    packages=find_packages(),
    package_data={'datasite': ['templates/*.html']},
    include_package_data=True,
    install_requires=[
        'click==6.7',
        'click-default-group==1.2',
        'sanic==0.6.0',
        'sanic-jinja2==0.5.5',
    ],
    entry_points='''
        [console_scripts]
        datasite=datasite.cli:cli
    ''',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
