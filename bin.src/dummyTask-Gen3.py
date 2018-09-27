#!/usr/bin/env python

import lsst.daf.butler


if __name__ == "__main__":
    # create butler instance with dummy output collection "jobout"

    camera = "HSC"
    expnum = 904010
    sensor = 4
    incollect = "shared/ci_hsc"
    outcollect = "jobout"

    butler = lsst.daf.butler.Butler("jobrepo", collection=outcollect)
    #butler.registry.registerDatasetType(lsst.daf.butler.DatasetType("modified_raw", ["Camera", "Exposure", "Sensor"], lsst.daf.butler.StorageClassFactory().getStorageClass("DecoratedImageU")))

    dataId={"camera": camera, "exposure": expnum, "sensor": sensor}

    raw = butler.registry.getDatasetType("raw")
    ref = butler.registry.find(incollect, raw, dataId)

    butler.registry.associate(butler.collection, [ref])  # add it to output collection

    # load the exposure
    exposure = butler.get("raw", dataId)

    # Do some magic with the data, here add a new header value.
    metadata = exposure.getMetadata()
    metadata.set("FUDGE_FACTOR", "3.1415")


    # save the updated exposure
    dataId2 = {"camera": camera, "exposure": expnum, "sensor": sensor}
    butler.put(exposure, "modified_raw", dataId2)

