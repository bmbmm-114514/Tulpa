"""OS bootstrap variables retained by isolated application test environments."""
import os


def system_environment():
    # Windows OpenSSL needs SystemRoot to initialize its system provider.
    # Keep application settings, credentials and proxy overrides out of fixtures.
    return {key:os.environ[key] for key in ('SystemRoot','WINDIR') if key in os.environ}
