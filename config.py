from utils import ReadOnlyDict, ReadOnlyList

# following patterns are used to search useful data in annotated image path
PATTERNS = ReadOnlyDict({'species': r'T\.\s?\w*',
                             'ploid': r'([А-Я][а-я]*)',
                             'vegetation': r'(X|Х|I){1,2}-?\d{2}',
                             'subspecies': r'\d{2,4}-?(\d{2,4})?',
                             'table': r'\d{2,5}(_\{[ХXI]{1,2}-?\d{2,5}\})?\.(jpg|JPG)$',
                             'pin': r'\d{2,5}_[1-4](_\{[ХXI]{1,2}-?\d{2,5}\})?\.(jpg|JPG)$'
                            })

# path-related constants
PROJECT_DIR = '/home/jupyter-n.artemenko/projects/spikelet_pubescence'
DATA_DIR = '/data/cv_project/spikedroid/ploid_classification'

# supported architectures for that project
ALLOWED_MODELS = ReadOnlyList(['resnet18'] + [f'efficientnet_b{i}' for i in range(8)])
ALLOWED_METRICS = ReadOnlyList(['accuracy_score', 'precision_score', 'recall_score', 'f1_score', 'roc_auc_score'])
ALLOWED_SCHEDULERS = ReadOnlyList(['ReduceLROnPlateau'])