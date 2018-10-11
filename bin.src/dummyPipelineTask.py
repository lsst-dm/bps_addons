"""A dummy task adding a new value to a raw image header.
"""

import lsst.log
from lsst.pipe.base import (Struct, PipelineTask, PipelineTaskConfig,
                            InputDatasetField, OutputDatasetField)


logger = lsst.log.Log.getLogger(__name__)


class DummyPipelineTaskConfig(PipelineTaskConfig):
    input = InputDatasetField(name="raw",
                              units=["Camera", "Exposure", "Sensor"],
                              storageClass="DecoratedImageU",
                              scalar=True,
                              doc="Input dataset type")
    output = OutputDatasetField(name="modified_raw",
                                units=["Camera", "Exposure", "Sensor"],
                                storageClass="DecoratedImageU",
                                scalar=True,
                                doc="Output dataset type")

    def setDefaults(self):
        self.quantum.units = ["Camera", "Exposure", "Sensor"]


class DummyPipelineTask(PipelineTask):
    """A dummy PipelineTask.
    """
    ConfigClass = DummyPipelineTaskConfig
    _DefaultName = 'dummyPipelineTask'

    def run(self, input):
        """Add a value to raw header file.
        """
        metadata = input.getMetadata()
        metadata.set("FUDGE_FACTOR", "3.1415")
        return Struct(output=input)

    def __str__(self):
        return "{}(name={})".format(self.__class__.__name__, self.getName())
