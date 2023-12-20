import pytest

from app.exceptions.document import ValidationError


def test_validation_error():
    
    with pytest.raises(ValidationError) as exc_info:
        raise ValidationError("Некорректные данные")

    assert str(exc_info.value) == "Некорректные данные"
    assert exc_info.value.status_code == 422
