import io

class BulkLogger(io.StringIO):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def close(self):
        self.level(self.getvalue())
        super().close()
