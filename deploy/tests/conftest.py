import pytest
import os
from os.path import dirname
from pathlib import Path

# fixtures defined in this file will be available to all tests. see
# https://docs.pytest.org/en/4.6.x/example/simple.html#package-directory-level-fixtures-setups

@pytest.fixture
def aws_test_credentials():
    """Mocked AWS Credentials for moto."""
    # see https://github.com/spulec/moto/blob/8281367dcea520d8971d88fbea1a8bbe552c4a3d/README.md#example-on-pytest-usage
    # ** You must use this on every test. **
    #
    # moto mock must be established before boto makes calls.  In the event that someone forgets to
    # mock the appropriate apis or more likely APIs used by a function called in a test change without
    # updating the test, these environment variables will prevent boto from being able to use
    # real credentials to make real calls to AWS.
    # see: https://github.com/spulec/moto/blob/8281367dcea520d8971d88fbea1a8bbe552c4a3d/README.md#very-important----recommended-usage
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    # Provide a default region, since one may not already be configured (true of CI)
    # This was an arbitrary selection
    os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'


# Point moto to JSON of AMI's to load for various EC2 queries
# The builtin AMI JSON doesn't have the FPGA Development AMI
# This can't really be done as a fixture because it needs to be defined at moto import time
# I don't like defining it in pytest.ini because the pwd used by pytest-env plugin
# is dependent on where pytest is invoked and intellij will run it in subdirs of deploy...
os.environ['MOTO_AMIS_PATH'] = '{}/test_amis.json'.format(dirname(__file__))


# enable simple `import firesim` work for testing without checking in a symlink or reorganizing
firesim_py = Path(__file__).parent.parent / 'firesim.py'
try:
    firesim_py.symlink_to('firesim')
except FileExistsError:
    pass