from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='python_snake',
        version='1.0',
        url='https://github.com/Merbuz/Snake',
        license='GPL-3.0 license',
        author='Merbuz',
        description='Simple snake written on Python, that works in your console!',  # noqa: E501
        packages=find_packages(),
        install_requires=['asyncio<=3.4.3', 'keyboard<=0.13.5'],
        entry_points={
            'console_scripts': [
                'console_example=cli:cli'
            ],
        }
    )
