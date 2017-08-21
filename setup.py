from setuptools import setup

setup(
    name='Flask-log-request-id',
    version='0.1.0',
    url='http://github.com/Workable/flask-log-request-id',
    license='BSD',
    author='Konstantinos Paliouras, Ioannis Foukarakis',
    author_email='paliouras@workable.com, foukarakis@workable.com',
    description='An extension that detects trace id headers on request '
                'and propagates on logging module through the life-cycle of request',
    packages=['flask_log_request_id'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.8',
    ],
    tests_require=[
        'nose',
        'mock==2.0.0',
        'coverage==4.3.4'
    ],
    setup_requires=[
        "flake8"
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])
