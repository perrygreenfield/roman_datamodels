import asdf
import pytest

from roman_datamodels.testing import factories
from roman_datamodels import stnode


@pytest.mark.parametrize("node_class", stnode.NODE_CLASSES)
def test_factory_method_implemented(node_class):
    """
    Confirm that a subclass of TaggedObjectNode has a factory method
    available.
    """
    if node_class.__name__ == "KeywordPixelarea":
        pytest.xfail("No schema for KeywordPixelarea, see https://github.com/spacetelescope/rad/issues/11")

    factory_method = factories.get_factory_method(node_class)

    assert factory_method.__name__ in factories.__all__, (
        f"Missing {method_name} from roman_datamodels.factories.__all__."
    )

    instance = factory_method()
    assert isinstance(instance, node_class), (
        f"Method roman_datamodels.factories.{method_name} does not return an "
        f"instance of roman_datamodels.stnode.{node_class.__name__}."
    )


@pytest.mark.parametrize("node_class", stnode.NODE_CLASSES)
def test_instance_valid(node_class):
    """
    Confirm that a class's factory method creates an object that
    is valid against its schema.
    """
    if node_class.__name__ == "KeywordPixelarea":
        pytest.xfail("No schema for KeywordPixelarea, see https://github.com/spacetelescope/rad/issues/11")

    with asdf.AsdfFile() as af:
        af["node"] = factories.get_factory_method(node_class)()
        af.validate()
