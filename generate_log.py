# generate_log.py (project root)

# Re-export the real implementation from lib/, so both:
#   from generate_log import generate_log        (root-level import)
#   from lib.generate_log import generate_log    (package import)
# resolve to the exact same function.
from lib.generate_log import generate_log