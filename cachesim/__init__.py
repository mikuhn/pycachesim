"""Cache simulation module."""
from __future__ import absolute_import

from .cache import *

__version__ = '0.3.0'

# To trigger travis deployment to pypi, do the following:
# 1. Increment __version___
# 2. commit to RRZE-HPC/pycachesim's master branch
# 3. wait for travis to complete successful (unless already tested)
# 4. tag commit with 'v{}'.format(__version__) (`git tag vX.Y.Z`)
# 5. push tag to github (`git push origin vX.Y.Z` or push all tags with `git push --tags`)
