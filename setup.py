from setuptools import setup

setup(
    name='Prometheus-Toolbox',
    version='0.0.1',
    url='https://github.com/vbilyi/prometheus_toolbox',
    license='MIT',
    author='Vitaly Bilyi',
    author_email='vitalybilyi@gmail.com',
    maintainer='Vitaly Bilyi',
    maintainer_email='stbarratt@gmail.com',
    description='Prometheus toolbox for python',
    long_description=__doc__,
    packages=['prometheus_toolbox'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'prometheus-client>=0.3.1',
        'Django>=1.8'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Topic :: System :: Monitoring',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='prometheus toolbox'
)