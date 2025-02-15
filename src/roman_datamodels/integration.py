import sys

from asdf.resource import DirectoryResourceMapping

if sys.version_info < (3, 9):
    import importlib_resources
else:
    import importlib.resources as importlib_resources


# def get_resource_mappings():
#     """
#     Get the resource mapping instances for the datamodel schemas
#     and manifests.  This method is registered with the
#     asdf.resource_mappings entry point.

#     Returns
#     -------
#     list of collections.abc.Mapping
#     """
#     from . import resources
#     resources_root = importlib_resources.files(resources)

#     return [
#         DirectoryResourceMapping(resources_root / "schemas", "http://stsci.edu/schemas/datamodels", recursive=True),
#         DirectoryResourceMapping(resources_root / "manifests", "http://stsci.edu/asdf/datamodels/manifests"),
#     ]


def get_extensions():
    """
    Get the extension instances for the various astropy
    extensions.  This method is registered with the
    asdf.extensions entry point.

    Returns
    -------
    list of asdf.extension.Extension
    """
    from . import extensions
    return extensions.DATAMODEL_EXTENSIONS
