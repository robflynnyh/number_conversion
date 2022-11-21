from setuptools import setup

setup(
    name='number_conversion',
    version='0.1',    
    description='For use with num2words. Convert a document with numbers in to a document with just words',
    url='https://github.com/robflynnyh/number_conversion',
    author='Rob Flynn',
    author_email='rjflynn2@sheffield.ac.uk',
    license='BSD 2-clause',
    packages=['number_conversion'],
    install_requires=['num2words'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: preprocessing',
    ],
)
