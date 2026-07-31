### Translocation classes

ID2LABELTRANSLOC = {0: 'O', 1: 'Arriving', 2: 'BeingAtAPlace', 3: 'Leaving', 4: 'Transportation', 5: 'Voyage',
                6: 'Translocation'}

ID2LABEL700PLUS = {0: 'O', 1: 'Communication'}

ID2LABEL300PLUS = {0: 'O', 1: 'HavingInPossession'}

ID2LABEL100PLUS = {0: 'O',  1: 'Giving', 2: 'Request', 3: 'Trade', 4: 'Getting', 5: 'Enslaving', 6: 'BeingEmployed',
                7: 'TakingUnderControl'}

ID2LABEL30TO100 = {0: 'O', 1: 'BeingInARelationship', 2: 'BeingDamaged', 3: 'Killing', 4: 'Collaboration', 5: 'FinancialTransaction', 6:'BeingInConflict',
                 7: 'BeingLeader', 8:'LeavingAnOrganization', 9:'HavingInternalState-', 10:'Attacking', 11: 'HavingContractualAgreement',
                12:'StartingAWar', 13: 'ForceToAct', 14:'Encounter', 15:'SocialInteraction', 16: 'Visit', 17: 'BeingDestroyed', 18: 'Production', 19:'Selling',
                    20: 'BeingDead', 21:'RelationshipChange'}

ID2LABEL10TO30 = {0: 'O', 1: 'Buying', 2: 'BeginningARelationship', 3: 'ViolentContest', 4: 'BeingInDebt', 5: 'Replacing',
            6: 'LosingPossession', 7: 'ChangeOfPossession', 8: 'JoiningAnOrganization' , 9: 'Unrest', 10: 'HavingInternalState+', 11: 'Mismanagement',
                12: 'HavingAMedicalCondition', 13: 'BeingAtPeace', 14: 'QuantityChange'}

ID2LABELALLSELECTED = {0: 'O', 1: 'Arriving', 2: 'BeingAtAPlace', 3: 'Leaving', 4: 'Transportation', 5: 'Voyage',
                6: 'Translocation', 7: 'Communication', 8: 'HavingInPossession', 9: 'Giving', 10: 'Request', 11: 'Trade', 12: 'Getting', 13: 'Enslaving', 14: 'BeingEmployed',
                15: 'TakingUnderControl', 16: 'BeingInARelationship', 17: 'BeingDamaged', 18: 'Killing', 19: 'Collaboration', 20: 'FinancialTransaction', 21:'BeingInConflict',
                 22: 'BeingLeader', 23:'LeavingAnOrganization', 24:'HavingInternalState-', 25:'Attacking', 26: 'HavingContractualAgreement',
                27:'StartingAWar', 28: 'ForceToAct', 29:'Encounter', 30:'SocialInteraction', 31: 'Visit', 32: 'BeingDestroyed', 33: 'Production', 34:'Selling',
                    35: 'BeingDead', 36:'RelationshipChange', 37: 'Buying', 38: 'BeginningARelationship', 39: 'ViolentContest', 40: 'BeingInDebt', 41: 'Replacing',
            42: 'LosingPossession', 43: 'ChangeOfPossession', 44: 'JoiningAnOrganization' , 45: 'Unrest', 46: 'HavingInternalState+', 47: 'Mismanagement',
                48: 'HavingAMedicalCondition', 49: 'BeingAtPeace', 50: 'QuantityChange'}

ID2LABELDETECT = {0: 'O', 1: 'B-event', 2: 'I-event'}

ID2LABELPOSSESSION = {0: 'O', 1: 'HavingInPossession', 2: 'Giving', 3: 'Buying', 4: 'Selling',
                      5: 'ChangeOfPossession', 6: 'Trade', 7: 'FinancialTransaction', 8: 'LosingPossession', 9: 'Getting'}

ID2LABELVIOLENCE = {0: 'O', 1: 'TakingUnderControl', 2: 'Enslaving', 3: 'Unrest', 4: 'Attacking', 5: 'StartingAWar', 6: 'Killing',
                    7: 'BeingInConflict', 8: 'ViolentContest', 9: 'ForceToAct'}


def select_labeldicts(parameter):
    label2id = {}

    if parameter == 'translocation':
        id2label = ID2LABELTRANSLOC
    elif parameter == 'over700':
        id2label = ID2LABEL700PLUS
    elif parameter == 'over100':
        id2label = ID2LABEL100PLUS
    elif parameter == 'over300':
        id2label = ID2LABEL300PLUS
    elif parameter == '30to100':
        id2label = ID2LABEL30TO100
    elif parameter == '10to30':
        id2label = ID2LABEL10TO30
    elif parameter == 'allselected':
        id2label = ID2LABELALLSELECTED
    elif parameter == 'detection':
        id2label = ID2LABELDETECT
    elif parameter == 'possession':
        id2label = ID2LABELPOSSESSION
    elif parameter == 'violence':
        id2label = ID2LABELVIOLENCE
    else:
        raise ValueError(f"Unknown parameter: '{parameter}'")

    for key, value in id2label.items():
        label2id[value] = key

    return id2label, label2id




