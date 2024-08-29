print('loading data')

# load genotypes
X_df_norm = pd.read_csv(data_path+'genotypes_norm.zip', index_col = 0) # genotypes matrix with direct effect markers, used for QOM
X_df_full = pd.read_csv(data_path+'genotypes_norm_full.zip', index_col = 0) # genotypes matrix with all genotyped markers, used for unrestricted PRS

# load heritability estimates of 183 transcription factors by Albert et al (2018)
heritability_df = pd.read_csv(data_path+'heritability_df.csv', index_col = 0)

# load gene expressions of 183 transcription factors and 1011 individuals
Y_df_norm = pd.read_csv(data_path+'GE_norm_PC1corr.csv', index_col = 0)

# load GRN matrix topology
B_prior = pd.read_csv(data_path+'B_prior.csv', index_col = 0)

# load direct effects matrix topology
D_prior = pd.read_csv(data_path+'D_prior.csv', index_col = 0)

# defining QOM_bound topology
for n in range(10):
    A = 0.0*B_prior
    x = B_prior.values.nonzero()[0]
    for x, y in zip(B_prior.values.nonzero()[0], B_prior.values.nonzero()[1]):
        A.iloc[x, y] = 5E-3*np.random.rand()

QOM_bound_prior = np.matmul(D_prior.values, np.linalg.inv(np.identity(B_prior.shape[0])-A))
QOM_bound_prior = pd.DataFrame(np.abs(np.sign(QOM_bound_prior)), index = D_prior.index, columns=D_prior.columns)

# define sets of individuals for cross-validatoion
individuals_test = np.array([   7,   26,   36,   40,   54,   57,   61,   68,   88,   91,   94,
        109,  131,  138,  144,  194,  198,  199,  214,  219,  228,  236,
        244,  249,  252,  257,  268,  277,  280,  283,  285,  289,  301,
        331,  333,  334,  344,  348,  370,  371,  381,  392,  393,  400,
        407,  424,  426,  437,  440,  446,  452,  455,  467,  480,  481,
        488,  490,  494,  495,  511,  512,  532,  552,  555,  572,  574,
        585,  600,  609,  610,  643,  645,  653,  656,  680,  689,  698,
        719,  723,  731,  743,  745,  747,  770,  772,  781,  787,  796,
        797,  799,  802,  814,  828,  834,  867,  873,  878,  880,  882,
        884,  886,  890,  895,  897,  930,  942,  949,  956,  958,  976,
        999, 1010])
individuals_train = np.setdiff1d(np.arange(1012), individuals_test)

individuals_val = np.array([809,  486,  601,  592,  547,  279,  765,  378,  246,  434,  524,
        972,  261,  877,  350,  738,  385,  917,  766,  167,  463,  843,
        441,  517,  792,   39,   70,  947,  503,   95,   98,  275,  479,
         90,  684,  483,   23,  556,  819,  341,  465,  561,  635,  538,
        270,  439,  380,  943,   85,  642,  752,  990,  398,  634,  856,
        844,  450,  964,  464,   56,  415,  850,  551,  343,  394,  339,
        389,  657,  889,  676,  586,   37,  576,  516,  925,  496,  644,
        130,  963,  442,  546,  310,  337,  775,  948,  119,  165,  272,
        912,  172,  654,  319,  223, 1002,  852,  851,  550,  726,  203,
        212])
individuals_train = np.setdiff1d(individuals_train, individuals_val)
individuals_testval = np.append(individuals_val, individuals_test)

test_folds_df = pd.read_csv(data_path+'test_folds.csv')
val_folds_df = pd.read_csv(data_path+'val_folds.csv')
N_folds = val_folds_df.shape[0]

I = np.identity(B_prior.shape[0])    

print('loaded X_df_norm, X_df_norm_full, Y_df_norm, B_prior, D_prior, test_folds_df, val_folds_df and defined QOM_bound_prior, N_folds, individuals_test, individuals_train, individuals_val, individuals_testval')