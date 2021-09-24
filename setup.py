from setuptools import setup


setup(
    name='cldfbench_wersing',
    py_modules=['cldfbench_wersing'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'wersing=cldfbench_wersing:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pyglottolog',
        'pydictionaria>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
