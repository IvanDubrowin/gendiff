class FileFormatError(AttributeError):
    def __init__(self):
         default_message = 'This format is not supported!'
         super().__init__(default_message)
