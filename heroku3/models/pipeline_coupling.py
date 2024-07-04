from . import BaseResource
from .app import App
from .pipeline import Pipeline


class PipelineCoupling(BaseResource):
    _strs = ["id", "stage"]
    _dates = ["created_at", "updated_at"]
    _map = {"app": App, "pipeline": Pipeline}
    _pks = ["id"]

    def __init__(self):
        self.app = None
        self.pipeline = None
        super().__init__()

    def __repr__(self):
        return "<PipelineCoupling '{0} - {1}'>".format(self.id, self.stage)
