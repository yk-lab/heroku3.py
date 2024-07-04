from . import BaseResource


class Pipeline(BaseResource):
    _strs = ["id", "name"]
    _pks = ["id"]

    def __init__(self):
        self.app = None
        super().__init__()

    def __repr__(self):
        return "<Pipeline '{0} - {1}'>".format(self.name, self.id)
