# Definition of CORSIKA7 containers

- Download CORSIKA 7.7100 from https://www.iap.kit.edu/corsika/ and untar the code in this folder
- run `sudo singularity build corsika<id>.sif corsika_<id>.def`

## CORSIKA compilation options

The `id` of the containers is defined as follows, following from the compilation options in CORSIKA (coconut script):

`container_name=corsika${cver}${hehim}${lehim}${geo}${ao}`

- `cver`: corsika version. Only possible value is `7` (meaning 77100) 

Then, the following options for the CORSIKA7 compilation in coconut:

- `hehim`: id=2 for `EPOS`, id=6 for `SYBILL`
- `lehim`: id=1 for `GHEISHA`, id=3 for `URQMD`
- `geo`: id=1 for `Flat`, id=2 `nonFlat`, id=3 `String`
- `ao`: 0 if they are standard options (see below), any other number (to be codified) for alternative options


### Standard options (i.e. alternative options set to 0): 

- option=4 for `NEUTRINO`
- option=6a for `CHARMED` (not active when you select EPOS)
- option=6 for `TAULEP` (taus with PYTHIA) 
- option=7a for `CURVED`
- option=7b for `UPWARD`
- option=h, h2 keeps track of the `HISTORY` of muons
