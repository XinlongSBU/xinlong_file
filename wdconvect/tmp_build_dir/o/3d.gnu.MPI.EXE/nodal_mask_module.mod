GFORTRAN module version '10' created from /raid2/xinlong/git_folder/amrex/Src/LinearSolvers/F_MG/nodal_mask.f90
MD5:a209463716f66eee5a6d3c83dfd19935 -- If you edit this, you'll get what you deserve.

(() () () () () () () () () () () () () () () () () () () () () () ()
() () () ())

()

()

(('mpifcmb5' 2 1 0 '') ('mpifcmb9' 3 1 0 '') ('mpipriv1' 4 1 0 '') (
'mpipriv2' 5 1 0 '') ('mpiprivc' 6 1 0 ''))

()

()

(7 'create_nodal_mask' 'nodal_mask_module' '' 1 ((PROCEDURE
UNKNOWN-INTENT MODULE-PROC DECL UNKNOWN 0 0 SUBROUTINE) (UNKNOWN 0 0 0 0
UNKNOWN ()) 8 0 (9 10 11 12 13) () 0 () () () 0 0)
2 'mpi_unweighted' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 IN_COMMON) (INTEGER 4 0 0 0 INTEGER ())
0 0 () () 0 () () () 0 0)
3 'mpi_weights_empty' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 IN_COMMON) (INTEGER 4 0 0 0 INTEGER ())
0 0 () () 0 () () () 0 0)
4 'mpi_bottom' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 IN_COMMON) (INTEGER 4 0 0 0 INTEGER ()) 0 14 () () 0
() () () 0 0)
5 'mpi_statuses_ignore' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION IN_COMMON) (INTEGER 4 0 0 0
INTEGER ()) 0 15 () (2 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '5') (CONSTANT (INTEGER
4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1'))
0 () () () 0 0)
6 'mpi_argvs_null' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION IN_COMMON) (CHARACTER 1 0 0 0
CHARACTER ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1'))) 0 16 () (2 0
EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1')) 0 () () () 0 0)
9 'n' '' '' 8 ((VARIABLE IN UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DUMMY) (
INTEGER 4 0 0 0 INTEGER ()) 0 0 () () 0 () () () 0 0)
10 'mask' '' '' 8 ((VARIABLE INOUT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DUMMY) (DERIVED 17 0 0 0 DERIVED ()) 0 0 () () 0 () () () 0 0)
11 'mm_crse' '' '' 8 ((VARIABLE INOUT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DUMMY) (DERIVED 18 0 0 0 DERIVED ()) 0 0 () () 0 () () () 0 0)
12 'mm_fine' '' '' 8 ((VARIABLE INOUT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DUMMY) (DERIVED 18 0 0 0 DERIVED ()) 0 0 () () 0 () () () 0 0)
13 'mla' '' '' 8 ((VARIABLE IN UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DUMMY) (
DERIVED 19 0 0 0 DERIVED ()) 0 0 () () 0 () () () 0 0)
14 'mpi_in_place' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 IN_COMMON) (INTEGER 4 0 0 0 INTEGER ())
0 20 () () 0 () () () 0 0)
15 'mpi_errcodes_ignore' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION IN_COMMON) (INTEGER 4 0 0 0
INTEGER ()) 0 0 () (1 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1')) 0 () () () 0 0)
16 'mpi_argv_null' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION IN_COMMON) (CHARACTER 1 0 0 0
CHARACTER ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1'))) 0 0 () (1 0
EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '1')) 0 () () () 0 0)
17 'Lmultifab' 'multifab_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP PRIVATE_COMP) (UNKNOWN 0 0
0 0 UNKNOWN ()) 0 0 () () 0 ((21 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (22 'nc' (
INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '1')) (23 'ng' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (24 'la' (DERIVED 25 0 0 0
DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 25 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ())) ())) (26 'nodal' (LOGICAL 4 0 0 0 LOGICAL ()) (1 0
DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ())
0)) (27 'fbs' (DERIVED 28 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (
() () () ()) () 0 0 98738776)
18 'Imultifab' 'multifab_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP PRIVATE_COMP) (UNKNOWN 0 0
0 0 UNKNOWN ()) 0 0 () () 0 ((29 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (30 'nc' (
INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '1')) (31 'ng' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (32 'la' (DERIVED 25 0 0 0
DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 25 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ())) ())) (33 'nodal' (LOGICAL 4 0 0 0 LOGICAL ()) (1 0
DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ())
0)) (34 'fbs' (DERIVED 35 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (
() () () ()) () 0 0 58601813)
19 'Ml_layout' 'ml_layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP PRIVATE_COMP) (UNKNOWN 0 0
0 0 UNKNOWN ()) 0 0 () () 0 ((36 'owner' (LOGICAL 4 0 0 0 LOGICAL ()) ()
(UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 1)) (37 'dim' (
INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (38 'nlevel' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (39 'mba' (DERIVED 40 0 0
0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 40 0 0 0 DERIVED ()) 0 (((
CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 1) ()) ((CONSTANT (INTEGER 4 0 0
0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')
()) ((NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ()) ((NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ())) ())) (41
'la' (DERIVED 25 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (42 'mask' (
DERIVED 17 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (43 'pmask' (
LOGICAL 4 0 0 0 LOGICAL ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (() () ()
()) () 0 0 40820460)
20 'mpi_status_ignore' 'fboxlib_mpi' '' 1 ((VARIABLE UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION IN_COMMON) (INTEGER 4 0 0 0
INTEGER ()) 0 0 () (1 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '5')) 0 () () () 0 0)
25 'Layout' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () ()
0 ((44 'la_type' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (45 'lap' (DERIVED 46 0 0
0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0 POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)))
PUBLIC (() () () ()) () 0 0 5443688)
28 'Lfab' 'fab_module' '' 1 ((DERIVED UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 POINTER_COMP PRIVATE_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((47 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (48 'bx' (DERIVED 49 0 0 0
DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '-1000000') ())) ())) (50 'pbx' (DERIVED 49 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'-1000000') ())) ())) (51 'ibx' (DERIVED 49 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'-1000000') ())) ())) (52 'nc' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1')) (53 'p' (
LOGICAL 4 0 0 0 LOGICAL ()) (4 0 DEFERRED () () () () () () () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PRIVATE
(() () () ()) () 0 0 37975414)
35 'Ifab' 'fab_module' '' 1 ((DERIVED UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 POINTER_COMP PRIVATE_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((54 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (55 'bx' (DERIVED 49 0 0 0
DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '-1000000') ())) ())) (56 'pbx' (DERIVED 49 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'-1000000') ())) ())) (57 'ibx' (DERIVED 49 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'-1000000') ())) ())) (58 'nc' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1')) (59 'p' (
INTEGER 4 0 0 0 INTEGER ()) (4 0 DEFERRED () () () () () () () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PRIVATE
(() () () ()) () 0 0 96213817)
40 'Ml_boxarray' 'ml_boxarray_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((60 'owner' (LOGICAL 4 0 0 0 LOGICAL ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 1)) (61 'dim' (
INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (62 'nlevel' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (63 'rr' (INTEGER 4 0 0 0
INTEGER ()) (2 0 DEFERRED () () () ()) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (
NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (64 'bas' (DERIVED 65 0 0 0
DERIVED ()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0
0 0 UNKNOWN ()) 0)) (66 'pd' (DERIVED 49 0 0 0 DERIVED ()) (1 0 DEFERRED
() ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)))
PUBLIC (() () () ()) () 0 0 24620268)
46 'Layout_rep' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((67 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (68 'id' (INTEGER 4 0 0 0
INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (69
'nboxes' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (70 'nlocal' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (71 'pd' (
DERIVED 49 0 0 0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED
()) 0 (((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '-1000000') ())) ())) (72 'pmask' (LOGICAL 4 0 0 0 LOGICAL
()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN
UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0)) (73 'prc' (INTEGER 4 0 0 0 INTEGER ()) (1 0 DEFERRED ()
()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))
(74 'idx' (INTEGER 4 0 0 0 INTEGER ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (75 'sfc_order' (
INTEGER 4 0 0 0 INTEGER ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (76 'bxa' (
DERIVED 65 0 0 0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 65 0 0 0 DERIVED
()) 0 (((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0 UNKNOWN ())
0) ())) ())) (77 'bxasc' (DERIVED 78 0 0 0 DERIVED ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER) UNKNOWN-ACCESS
(NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (79 'fgasc' (DERIVED 80 0 0 0
DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0 POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (81
'snasc' (DERIVED 82 0 0 0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN
0 0 0 0 UNKNOWN ()) 0)) (83 'crse_la' (DERIVED 84 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (85 'tas' (
DERIVED 86 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (87 'bahash' (
INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '-1')) (88 'crsn' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '-1')) (89 'plo' (INTEGER 4 0 0
0 INTEGER ()) (1 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1')
(CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '3')) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (90 'phi'
(INTEGER 4 0 0 0 INTEGER ()) (1 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '3')) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (91 'vshft'
(INTEGER 4 0 0 0 INTEGER ()) (1 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '3')) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (92 'bins'
(DERIVED 93 0 0 0 DERIVED ()) (3 0 DEFERRED () () () () () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (
() () () ()) () 0 0 74931974)
49 'Box' 'box_module' '' 1 ((DERIVED UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN
UNKNOWN 0 0) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () () 0 ((94 'dim' (
INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (95 'lo' (INTEGER 4 0 0 0 INTEGER ()) (1 0 EXPLICIT (CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '3')) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DIMENSION) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'1000000')) (96 'hi' (INTEGER 4 0 0 0 INTEGER ()) (1 0 EXPLICIT (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '3')) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN
UNKNOWN 0 0 DIMENSION) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER
()) 0 '-1000000'))) PUBLIC (() () () ()) () 0 0 63394476)
65 'Boxarray' 'boxarray_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((97 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (98 'nboxes' (INTEGER 4 0
0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN
UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0'))
(99 'bxs' (DERIVED 49 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (
() () () ()) () 0 0 42403120)
78 'Boxassoc' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () ()
0 ((100 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (101 'nboxes' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (102 'grwth'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (103 'idim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (104 'nodal' (LOGICAL 4 0
0 0 LOGICAL ()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (
NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (105 'cross' (LOGICAL 4 0 0 0
LOGICAL ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 0)) (106
'l_con' (DERIVED 107 0 0 0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 107
0 0 0 DERIVED ()) 0 (((CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 0) ()) (
(CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0
0 UNKNOWN ()) 0) ())) ())) (108 'r_con' (DERIVED 109 0 0 0 DERIVED ()) ()
(UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 109 0 0 0 DERIVED ()) 0 (((CONSTANT (
LOGICAL 4 0 0 0 LOGICAL ()) 0 0) ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER
()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) (
(NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ())
((NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ())) ())) (110 'next' (DERIVED 78 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (() () ()
()) () 0 0 74212712)
80 'Fgassoc' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () ()
0 ((111 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (112 'grwth' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (113 'prc'
(INTEGER 4 0 0 0 INTEGER ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (114 'idx' (
INTEGER 4 0 0 0 INTEGER ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (115 'ba' (
DERIVED 65 0 0 0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 65 0 0 0 DERIVED
()) 0 (((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0 UNKNOWN ())
0) ())) ())) (116 'next' (DERIVED 80 0 0 0 DERIVED ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER) UNKNOWN-ACCESS
(NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (() () () ()) () 0 0
60033558)
82 'Syncassoc' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((117 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (118 'nboxes' (INTEGER 4 0
0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN
UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0'))
(119 'grwth' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (120 'lall' (LOGICAL 4 0 0 0 LOGICAL ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 0)) (121 'nodal'
(LOGICAL 4 0 0 0 LOGICAL ()) (1 0 DEFERRED () ()) (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (122 'l_con' (
DERIVED 107 0 0 0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 107 0 0 0
DERIVED ()) 0 (((CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 0) ()) ((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ())) ())) (123 'r_con' (DERIVED 109 0 0 0 DERIVED ()) ()
(UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 109 0 0 0 DERIVED ()) 0 (((CONSTANT (
LOGICAL 4 0 0 0 LOGICAL ()) 0 0) ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER
()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) (
(NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ())
((NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0) ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ())) ())) (124 'next' (DERIVED 82 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (() () ()
()) () 0 0 7521756)
84 'Coarsened_layout' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((125 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (126 'crse' (INTEGER 4 0 0
0 INTEGER ()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (
NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (127 'la' (DERIVED 25 0 0 0
DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0
0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 25 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((NULL (UNKNOWN 0 0 0 0
UNKNOWN ()) 0) ())) ())) (128 'next' (DERIVED 84 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER)
UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (() () ()
()) () 0 0 59660841)
86 'Tilearray' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((129 'dim' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (130 'nthreads' (INTEGER 4
0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN
UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0'))
(131 'ntiles' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (132 'tilesize' (INTEGER 4 0 0 0 INTEGER ()) (1
0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '1') (CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '3')) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION) UNKNOWN-ACCESS (CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (133 'tilelo' (INTEGER 4 0 0 0
INTEGER ()) (2 0 DEFERRED () () () ()) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (
NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (134 'tilehi' (INTEGER 4 0 0 0
INTEGER ()) (2 0 DEFERRED () () () ()) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (
NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (135 'gidx' (INTEGER 4 0 0 0
INTEGER ()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0
0 0 UNKNOWN ()) 0)) (136 'lidx' (INTEGER 4 0 0 0 INTEGER ()) (1 0
DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ())
0))) PUBLIC (() () () ()) () 0 0 88280269)
93 'Box_hash_bin' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((137 'iv' (INTEGER 4 0 0 0 INTEGER ()) (1 0 DEFERRED ()
()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0
DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)))
PUBLIC (() () () ()) () 0 0 65337768)
107 'Local_conn' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((138 'threadsafe' (LOGICAL 4 0 0 0 LOGICAL ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 0)) (139 'ncpy'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (140 'cpy' (DERIVED 141 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0))) PUBLIC (
() () () ()) () 0 0 84494846)
109 'Remote_conn' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 POINTER_COMP) (UNKNOWN 0 0 0 0 UNKNOWN
()) 0 0 () () 0 ((142 'threadsafe' (LOGICAL 4 0 0 0 LOGICAL ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (LOGICAL 4 0 0 0 LOGICAL ()) 0 0)) (143 'svol'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (144 'rvol' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (145 'nsnd' (INTEGER 4 0 0
0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (146
'nrcv' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (147 'snd' (DERIVED 148 0 0 0 DERIVED ()) (1 0
DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ())
0)) (149 'rcv' (DERIVED 148 0 0 0 DERIVED ()) (1 0 DEFERRED () ()) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION
POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (150 'nrp'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (151 'nsp' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (152 'str' (DERIVED 153 0
0 0 DERIVED ()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (
NULL (UNKNOWN 0 0 0 0 UNKNOWN ()) 0)) (154 'rtr' (DERIVED 153 0 0 0
DERIVED ()) (1 0 DEFERRED () ()) (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0 DIMENSION POINTER) UNKNOWN-ACCESS (NULL (UNKNOWN 0 0
0 0 UNKNOWN ()) 0))) PUBLIC (() () () ()) () 0 0 83257863)
141 'Local_copy_desc' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () ()
0 ((155 'ns' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (156 'nd' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (157 'lns'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (158 'lnd' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (159 'sbx' (DERIVED 49 0 0
0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '-1000000') ())) ())) (160 'dbx' (DERIVED 49 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'-1000000') ())) ()))) PUBLIC (() () () ()) () 0 0 81606601)
148 'Comm_dsc' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () ()
0 ((161 'nd' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (162 'ns' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (163 'lnd'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '0')) (164 'lns' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL
UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (165 'dbx' (DERIVED 49 0 0
0 DERIVED ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN
0 0) UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((
CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '-1000000') ())) ())) (166 'sbx' (DERIVED 49 0 0 0 DERIVED ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (STRUCTURE (DERIVED 49 0 0 0 DERIVED ()) 0 (((CONSTANT (
INTEGER 4 0 0 0 INTEGER ()) 0 '0') ()) ((CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1000000') ()) ((CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0
'-1000000') ())) ())) (167 'pv' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (168 'sh'
(INTEGER 4 0 0 0 INTEGER ()) (1 0 EXPLICIT (CONSTANT (INTEGER 4 0 0 0
INTEGER ()) 0 '1') (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '4')) (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0 DIMENSION)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '0')) (169 'pr'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS ())) PUBLIC (() () () ()) () 0 0
52313599)
153 'Trns_dsc' 'layout_module' '' 1 ((DERIVED UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) (UNKNOWN 0 0 0 0 UNKNOWN ()) 0 0 () ()
0 ((170 'sz' (INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT
UNKNOWN-PROC UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0
0 0 INTEGER ()) 0 '0')) (171 'pv' (INTEGER 4 0 0 0 INTEGER ()) () (
UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC UNKNOWN UNKNOWN 0 0)
UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ()) 0 '-1')) (172 'pr'
(INTEGER 4 0 0 0 INTEGER ()) () (UNKNOWN-FL UNKNOWN-INTENT UNKNOWN-PROC
UNKNOWN UNKNOWN 0 0) UNKNOWN-ACCESS (CONSTANT (INTEGER 4 0 0 0 INTEGER ())
0 '-2'))) PUBLIC (() () () ()) () 0 0 25989494)
)

('create_nodal_mask' 0 7)
