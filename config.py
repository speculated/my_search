HPO_search_space = {
        # discrete
        # 'lr':                    ('choice', [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]), 
        'lr':                    ('choice', [3e-4]), 
        # 'hidden_dim':            ('choice', [16, 32, 48, 64, 128, 256]),
        'hidden_dim':            ('choice', [64]),
        # 'attn_dim':              ('choice', [2, 4, 8, 16, 32, 64]),
        'attn_dim':              ('choice', [5]),
        # 'n_layer':               ('choice', [3, 4, 5, 6, 7, 8]),
        'n_layer':               ('choice', [8]),
        # 'n_node_topk':           ('choice', [100, 200, 500, 1000, 2000]),
        'n_node_topk':           ('choice', [1000]),
        'n_edge_topk':           ('choice', [-1]),
        # 'act':                   ('choice', ['relu', 'idd', 'tanh']),
        'act':                   ('choice', ['idd']),
        # 'MESS_FUNC':             ('choice', ['TransE', 'DistMult', 'RotatE']),
        'MESS_FUNC':             ('choice', ['DistMult']),
        # 'AGG_FUNC':              ('choice', ['sum', 'mean', 'max']),
        'AGG_FUNC':              ('choice', ['sum']),
        # 'COMB_FUNC':             ('choice', ['discard', 'residual']),
        'COMB_FUNC':             ('choice', ['discard']),
        # 'n_batch':               ('choice', [8, 16, 32, 64, 128]),
        'n_batch':               ('choice', [100]),
        # 'n_tbatch':              ('choice', [16]),
        'n_tbatch':              ('choice', [50]),
        
        # continuous
        # 'decay_rate':            ('uniform', (0.8, 1)),
        'decay_rate':            ('uniform', (0.994)),
        # 'lamb':                  ('uniform', (1e-5, 1e-3)),
        'lamb':                  ('uniform', (14e-5)),
        # 'dropout':               ('uniform', (0, 0.5)),
        'dropout':               ('uniform', (0.02)),
    }
