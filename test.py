
class BaseValidator:

    def __init__(self):
        self._errors = []

    @property
    def errors(self):
        return self._errors

    def push(self, error_name, error_text):
        self._errors.append({
            error_name: error_text
        })

    def pop(self):
        return self._errors.pop(0)

    def any(self):
        return len(self._errors) > 0

    def first(self):
        if len(self._errors) != 0:
            return self._errors[0]
        return {}

    def get(self, error_name):
        return next(iter(filter(lambda x: error_name in x.keys(), self._errors)))


def validate(validate_data, fields):
    pass

user = {
    'username': 'test',
    'password': 'qwerty123'
}

user.validate({
    'username': ['required', '2:len:5']
})



