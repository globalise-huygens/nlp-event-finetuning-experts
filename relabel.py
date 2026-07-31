from select_id2label_experts import select_labeldicts
from select_id2label import select_labeldicts_all
def relabel(label, label_parameter):
    '''relabels the dataset according to expertise'''

    if label_parameter=='over100':
        id2label, label2id = select_labeldicts('over100')
        if label == 'Occupation':
            new_label = 'TakingUnderControl'
        elif label == 'None':
            new_label = 'O'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter=='over700':
        id2label, label2id = select_labeldicts('over700')
        if label == 'None':
            new_label = 'O'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter=='30to100':
        id2label, label2id = select_labeldicts('30to100')
        if label == 'None':
            new_label = 'O'
        elif label == 'IntentionalDamaging' or label == 'Damaging':
            new_label = 'BeingDamaged'
        elif label == 'Besieging' or label == 'Invasion':
            new_label = 'Attacking'
        elif label == 'BeginningContractualAgreement' or label == 'ExtendingContractualAgreement' or label == 'EndingContractualAgreement':
            new_label = 'HavingContractualAgreement'
        elif label == 'Destroying':
            new_label = 'BeingDestroyed'
        elif label == 'Dying':
            new_label = 'BeingDead'
        elif label == 'AlteringARelationship' or label =='EndingARelationship':
            new_label = 'RelationshipChange'
        elif label == 'StartingConflict' or label == 'EndingConflict':
            new_label = 'BeingInConflict'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter == 'over300':
        id2label, label2id = select_labeldicts('over300')
        if label == 'None':
            new_label = 'O'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter == 'translocation':
        id2label, label2id = select_labeldicts('translocation')
        if label == 'None':
            new_label = 'O'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter=='10to30':
        id2label, label2id = select_labeldicts('10to30')
        if label == 'None':
            new_label = 'O'
        elif label == 'Uprising' or label == 'Mutiny':
            new_label = 'Unrest'
        elif label == 'Repairing' or label == 'Healing':
            new_label = 'HavingInternalState+'
        elif label == 'FallingIll':
            new_label = 'HavingAMedicalCondition'
        elif label == 'Increasing' or label == 'Decreasing':
            new_label = 'QuantityChange'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter=='allselected':
        id2label, label2id = select_labeldicts('allselected')
        if label == 'None':
            new_label = 'O'
        elif label == 'Uprising' or label == 'Mutiny':
            new_label = 'Unrest'
        elif label == 'Repairing' or label == 'Healing':
            new_label = 'HavingInternalState+'
        elif label == 'FallingIll':
            new_label = 'HavingAMedicalCondition'
        elif label == 'Increasing' or label == 'Decreasing':
            new_label = 'QuantityChange'
        elif label == 'IntentionalDamaging' or label == 'Damaging':
            new_label = 'BeingDamaged'
        elif label == 'Besieging' or label == 'Invasion':
            new_label = 'Attacking'
        elif label == 'BeginningContractualAgreement' or label == 'ExtendingContractualAgreement' or label == 'EndingContractualAgreement':
            new_label = 'HavingContractualAgreement'
        elif label == 'Destroying':
            new_label = 'BeingDestroyed'
        elif label == 'Dying':
            new_label = 'BeingDead'
        elif label == 'AlteringARelationship' or label =='EndingARelationship':
            new_label = 'RelationshipChange'
        elif label == 'StartingConflict' or label == 'EndingConflict':
            new_label = 'BeingInConflict'
        elif label == 'Occupation':
            new_label = 'TakingUnderControl'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter == 'all':
        id2label, label2id = select_labeldicts_all('all')
        if label == 'None':
            new_label = 'O'
        elif label == 'Miscelaneous':
            new_label = 'O'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter == 'possession':
        id2label, label2id = select_labeldicts('possession')
        if label == 'None':
            new_label = 'O'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    elif label_parameter == 'violence':
        id2label, label2id = select_labeldicts('violence')
        if label == 'None':
            new_label = 'O'
        elif label == 'Occupation':
            new_label = 'TakingUnderControl'
        elif label not in label2id.keys():
            new_label = 'O'
        else:
            new_label = label

    return(new_label)
