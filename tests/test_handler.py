import pytest

from app.services.utils.handlers import DataHandler
from .data_for_test import tree, expected_result


@pytest.mark.parametrize('tree_input, expected_output', (
        (tree, expected_result),
))
@pytest.mark.asyncio
async def test_correct_splitting_dicts(tree_input, expected_output):
    result = await DataHandler.merge_trees(tree_input)
    assert result == expected_output
