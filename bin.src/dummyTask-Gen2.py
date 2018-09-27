#!/usr/bin/env python
from lsst.pex.config import Config
from lsst.pipe.base import CmdLineTask, Struct


class DummyTask(CmdLineTask):
    """A dummy task adding a field to the header of a raw image.
    """
    _DefaultName = 'DummyTask'
    ConfigClass = Config
    canMultiprocess = False

    def __init__(self, *args, **kwargs):
        CmdLineTask.__init__(self, *args, **kwargs)

    #MMGdef run(self, dataRef):
    def runDataRef(self, dataRef):
        """Modify raw image data header.

        Parameters
        ----------
        dataRef :
            butler data reference to a raw image
        """
        self.log.info("Processing %s: " % dataRef.dataId)
        exposure = dataRef.get("raw", immediate=True)

        # Do some magic with the data, here add a new header value.
        metadata = exposure.getMetadata()
        metadata.set("FUDGE_FACTOR", "3.1415")

        dataRef.put(exposure, "calexp")
        return Struct(exposure=exposure)

    def _getConfigName(self):
        return None

    def _getMetadataName(self):
        return None


if __name__ == "__main__":
    DummyTask.parseAndRun()
