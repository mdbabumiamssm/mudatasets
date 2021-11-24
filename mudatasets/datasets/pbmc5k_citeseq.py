from ..core import MuDataSet
from ..utils import sizefmt


class PBMC3kCITEseq(MuDataSet):
    """
    Peripheral blood mononuclear cells (PBMCs) 
    stained with a panel of 31 TotalSeq™-B antibodies
    provided by 10X Genomics
    """

    def __init__(self):
        self.name = "pbmc5k_citeseq"
        self.version = "1.0.0"
        self.format = "10x_h5"
        self.files = [
            {
                "name": "filtered_feature_bc_matrix.h5",
                "url": "https://cf.10xgenomics.com/samples/cell-exp/3.0.2/5k_pbmc_protein_v3/5k_pbmc_protein_v3_filtered_feature_bc_matrix.h5",
                "md5": "3366a47283177fe9af143d5819fad61f",
                "size": 17129253,
                "required": True,
            },
        ]

        self.total_size_int = sum([f["size"] for f in self.files])
        self.total_size = sizefmt(self.total_size_int)

        self.data = {
            "name": self.name,
            "version": self.version,
            "format": self.format,
            "total_size": self.total_size,
            "files": self.files,
        }
        self.data_versions = [
            self.data,
        ]

        self.info = {
            **self.data,
            "data_versions": self.data_versions,
        }


def dataset():
    return PBMC3kCITEseq()
