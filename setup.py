from setuptools import setup, find_packages

setup(
    name='acppred',
    version='0.0.1',
    packages=find_packages(),
    author='Deborah Trota F. de Albernaz',
    author_email='trotadeborah@gmail.com', 
    description='anticancer peptide prediction tool',
    entry_points={
        'console_scripts':[
            'acppred-preprocess = acppred.preprocess:main',
            'acppred-train = acppred.train:main',
            'acppred-predict = acppred.predict:main',
            'acppred-server = acppred.server:main'
        ]
    }
)