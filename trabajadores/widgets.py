from django import forms

class MultiFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs is not None:
            self.attrs.update(attrs)
        self.attrs.setdefault('multiple', 'multiple')

    def value_from_datadict(self, data, files, name):
        upload = files.getlist(name)
        if not upload:
            return []
        return upload
