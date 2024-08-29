path = '' # add absolute path if needed
sys.path.append(path)
sys.path.append(os.path.join(path, 'scripts/'))
sys.path.append(os.path.join(path, 'data/'))
sys.path.append(os.path.join(path,'results/'))
sys.path.append(os.path.join(path,'precomputed_results/'))

results_path = os.path.join(path,'results/')
precomp_results_path = os.path.join(path,'precomputed_results/')

data_path = os.path.join(path, 'data/')
init_SEM_GWAS_path = os.path.join(path,'scripts/')

print('defined absolute path: {} and appended sub-folders scripts and results and defined init_SEM_GWAS_path: {}, results_path: {}, data_path: {}'.format(path, init_SEM_GWAS_path, results_path, data_path, precomp_results_path))

