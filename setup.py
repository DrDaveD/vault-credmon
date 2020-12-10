from setuptools import setup, find_packages

setup(
    name='vault-credmon',
    version = '0.1',
    description = 'Vault credential monitor for use with HTCondor',
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = 'https://github.com/htcondor/vault-credmon',
    author = 'Jason Patton',
    author_email = 'jpatton@cs.wisc.edu',
    license = 'MIT',
    packages = find_packages(),
    scripts = ['bin/condor_credmon_vault', 'bin/vault_credential_producer'],
    install_requires = [
        'htcondor >= 8.8.2',
        'six',
        'cryptography',
        ],
    include_package_data = True
    )
