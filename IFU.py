class IFU(object):
    """Read an existing IFU model stored in the data directory as a pickle
    Internal Parameters
    ----------
    ID: array
        array of lens IDs in the focal plane
    blockID: array 
        IFU block number 
    blockN: array
        Fiber ID in the block
    x: array
        x-position in focal plane
    y: array
        y-position in focal plane
    r: array
        lens radius defined as average radius from center to corner
    lensKernel: 2d-array
        Place holder to store a 2d-array lens kernel 
        calculated from the analytic hexagon and 
        the datacube PIXSCALE

    """
    def __init__ (self, ifuname):
        """ Initialize the IFU class"""
        self.lensKernel = None
        self.lensx = None
        self.lensy = None
        self.lensr = None
        self.lensID = None
        self.blockID= None
        self.blockN = None
