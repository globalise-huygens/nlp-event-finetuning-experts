#### all classes present in data, no merging of classes (this labelset is the labelset of the EtE model)

ID2LABELALL = {0: 'O', 1: 'Leaving', 2: 'Occupation', 3: 'BeingDead', 4: 'Arriving',5: 'BeingAtAPlace',
                6: 'SocialInteraction', 7: 'Giving', 8: 'BeingInARelationship', 9: 'Request', 10: 'HavingInPossession',
                11: 'StartingConflict', 12: 'Trade', 13: 'Transportation', 14: 'Getting', 15: 'Enslaving', 16: 'BeingEmployed',
                17: 'InternalChange', 18: 'BeingInDebt', 19: 'Translocation', 20: 'Buying', 21: 'HavingContractualAgreement',
                22: 'Selling', 23: 'Decreasing', 24: 'BeingLeader', 25: 'Replacing', 26: 'Increasing', 27: 'FallingIll',
                28: 'Visit', 29: 'HavingInternalState-', 30: 'BeginningARelationship', 31: 'AlteringARelationship', 32: 'EndingARelationship',
                33: 'BeingInConflict', 34: 'LosingPossession', 35: 'IntentionalDamaging', 36: 'Damaging', 37: 'BeingDamaged',
                38: 'Destroying', 39: 'StartingAWar', 40: 'Dying', 41: 'TakingUnderControl', 42: 'ViolentContest', 43: 'None', 44: 'Collaboration',
                45: 'Killing', 46: 'ForceToAct', 47: 'Attacking', 48: 'ChangeOfPossession', 49: 'FinancialTransaction', 50: 'EndingContractualAgreement',
                51: 'LeavingAnOrganization', 52: 'Mutiny', 53: 'SocialStatusChange', 54: 'Encounter', 55: 'Voyage', 56: 'Communication',
                57: 'Repairing', 58: 'BeginningContractualAgreement', 59: 'BeingAtPeace', 60: 'BeingDestroyed', 61: 'HavingInternalState+',
                62: 'Mismanagement', 63: 'HavingAMedicalCondition', 64: 'Besieging', 65: 'Invasion', 66: 'EndingConflict', 67: 'Sinking',
                68: 'ExtendingContractualAgreement', 69: 'QuantityChange', 70: 'Production', 71: 'Unrest', 72: 'Uprising', 73: 'ScalarChange',
                74: 'Punishing', 75: 'JoiningAnOrganization', 76: 'Healing', 77: 'RelationshipChange'}

def select_labeldicts_all(parameter):
    """
    According to a setting, return correct id2label and label2id dicts

    :param param: str ('all', 'majority' or 'translocation')
    :return: dict
    """
    label2id = {}

    if parameter == 'all':
        id2label = ID2LABELALL
    else:
        raise ValueError(f"Unknown parameter: '{parameter}'")

    for key, value in id2label.items():
        label2id[value] = key

    return(id2label, label2id)



