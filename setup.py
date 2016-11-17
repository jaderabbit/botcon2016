from setuptools import setup

setup(
    name='BotconAfrica2016',
    version='0.1.0',
    author='jaderabbit',
    author_email='jabbott [at] retrorabbit [dot] co [dot] za',
    url='https://github.com/jaderabbit/botcon2016',
    description='3 Toy Problems for Natural Language Processing',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'gensim',
        'theano',
        'keras',
        'nltk',
        'jupyter'
    ],
    dependency_links = ['https://github.com/jaderabbit/WikiRockWord2Vec']
)
