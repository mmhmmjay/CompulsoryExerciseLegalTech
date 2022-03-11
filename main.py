# List of variables

legal_processing = "The processing is legal under Art. 9 GDPR. "

illegal_processing = "The processing is not legal under this exception according to Art. 9 (2) GDPR. Please proceed" \
                     "with the following question. "

illegal_processing_final = "The processing is illegal according to Art. 9 GDPR. Other derogations of Art. 9 (2) GDPR" \
                           "do not seem to apply. If you are unsure about this outcome, please contact your legal " \
                           "advisor. "

explicit_consent = "Has the tested person given explicit consent to the specific purpose of their data being "\
                            "used for the model of the COVID transition rate? "

unable_consent = "Is the person being tested physically or legally unable to give consent? "

vital_interests = "Is the processing necessary to protect vital interests of the person being tested or other natural" \
                  " persons? According to recital 46 GDPR, some types of processing can be serving bot vital " \
                  "interests of the data subject and important public interests such as monitoring epidemics and their"\
                  " spread. "

public_interest = "Is the processing necessary for reasons of substantial public interest such as monitoring epidemics"\
                  "and their spread? "

public_health = "Is the processing necessary for reasons of public interest in the area of public health (e.g." \
                "protection against serious cross-border health threats) "

legal_basis = "Is the processing based on an EU or Norwegian law? "

proportionate_law = "Is the legal basis proportionate to the aim being pursued? "

essence_of_data_protection = "Does the law respect the essence of the right to data protection? "

safeguard_measures = "Does the law provide for suitable and specific measures to safeguard the fundamental rights" \
                     "and the interests of the data subject (e.g. professional secrecy?)? "

made_public = "Was the data manifestly made public by the data subject? "

archiving = "Is the processing necessary for archiving purposes in the public interest, scientific or historical" \
            "research purposes or statistical purposes? "

preventive_medicine = "Is the processing necessary for the purposes of preventive medicine, for medical treatment, the"\
                      "provision of health care or the management of health care systems and services?"

legal_basis_preventive = "Is the processing based on an EU or Norwegian law or pursuant to contract with a health " \
                         "professional?"

safeguards_paragraph_three = "Are the data processed by or under the responsibility of a professional subject to the" \
                             "obligation of professional secrecy under Union or Norwegian law or rules established by" \
                             " national competent bodies or by another person also subject to an obligation of secrecy"\
                             " under Union or Norwegian law or rules established by national competent bodies."

# Functions

# Explicit Consent (Art. 9 (2) (a) GDPR)
def expcon (explicit_consent, legal_processing, illegal_processing):
    answer = input(explicit_consent)
    if answer.upper() == "YES":
        print(legal_processing)
        return 1
    elif answer.upper() == "NO":
        print(illegal_processing)
        return 0

# Unable to Give Consent (Art. 9 (2) (c) GDPR)
def unablecon(unable_consent, vital_interests, legal_processing, illegal_processing):
    answer = input(unable_consent )
    if answer.upper() == "YES":
        answertwo = input(vital_interests )
        if answertwo.upper() == "YES":
            print(legal_processing)
        else:
            print(illegal_processing)
            return 0
    else:
        print(illegal_processing)
        return 0

# Public Health (Art. 9 (2) (i) GDPR)
def publichealth (public_health, legal_basis, safeguard_measures, legal_processing, illegal_processing):
    answer = input(public_health )
    if answer.upper() == "YES":
        answertwo = input(legal_basis )
        if answertwo.upper() == "YES":
            answerthree = input(safeguard_measures )
            if answerthree.upper() == "YES":
                print(legal_processing)
                return 1
            else:
                print(illegal_processing)
                return 0
        else:
            print(illegal_processing)
            return 0
    else:
        print(illegal_processing)
        return 0

# Substantial Public Interest (Art. 9 (2) (g) GDPR)
def publicinterest (public_interest, legal_basis, proportionate_law, essence_of_data_protection, safeguard_measures,
                    legal_processing, illegal_processing):
    answer = input(public_interest )
    if answer.upper() == "YES":
        answertwo = input(legal_basis )
        if answertwo.upper() == "YES":
            answerthree = input(proportionate_law )
            if answerthree.upper() == "YES":
                answerfour = input(essence_of_data_protection )
                if answerfour.upper() == "YES":
                    answerfive = input(safeguard_measures )
                    if answerfive.upper() == "YES":
                        print(legal_processing)
                    else:
                        print(illegal_processing)
                        return 0
                else:
                    print(illegal_processing)
                    return 0
            else:
                print(illegal_processing)
                return 0
        else:
            print(illegal_processing)
            return 0
    else:
        print(illegal_processing)
        return 0

# Manifestly Made Public by the Data Subject (Art. 9 (2) (e) GDPR)
def madepublic (made_public, legal_processing, illegal_processing):
    answer = input(made_public )
    if answer.upper() == "YES":
        print(legal_processing)
        return 1
    else:
        print(illegal_processing)
        return 0

# Archiving/Research (Art. 9 (2) (j) GDPR)
def archive (archiving, legal_basis, proportionate_law, essence_of_data_protection, safeguard_measures,
            legal_processing, illegal_processing):
    answer = input(archiving)
    if answer.upper() == "YES":
        answertwo = input(legal_basis)
        if answertwo.upper() == "YES":
            answerthree = input(proportionate_law)
            if answerthree.upper() == "YES":
                answerfour = input(essence_of_data_protection)
                if answerfour.upper() == "YES":
                    print("Specific safeguard measures in accordance with Art. 89 (1) GDPR include pseudonymisation"
                          "and anonymisation where possible.")
                    answerfive = input(safeguard_measures)
                    if answerfive.upper() == "YES":
                        print(legal_processing)
                        return 1
                    else:
                        print(illegal_processing)
                        return 0
                else:
                    print(illegal_processing)
                    return 0
            else:
                print(illegal_processing)
                return 0
        else:
            print(illegal_processing)
            return 0
    else:
        print(illegal_processing)
        return 0

# Preventive Medicine (Art. 9 (2) (h) GDPR)
def preventive (preventive_medicine, legal_basis_preventive, safeguards_paragraph_three, legal_processing,
                illegal_processing):
    answer = input(preventive_medicine)
    if answer.upper() == "YES":
        answer_two = input(legal_basis_preventive)
        if answer_two.upper() == "YES":
            answer_three = input(safeguards_paragraph_three)
            if answer_three.upper() == "YES":
                print(legal_processing)
                return 1
            else:
                print(illegal_processing)
                return 0
        else:
            print(illegal_processing)
            return 0
    else:
        print(illegal_processing)
        return 0


# Beginning of the program


print("Is the processing of personal data regarding COVID19-testing legal in accordance with Art. 9 GDPR? ")

type_of_test = input("What kind of test has been carried out? (Possible Answers: PCR-Test or Antibody-Test)" )

if type_of_test.upper() == "PCR-TEST":
    print("The type of data you are processing is health data. Therefore Art. 9 GDPR is applicable and "
          "processing is thus generally prohibited (see Art. 9 (1) GDPR. However an exception according to Art. 9 (2)"
          "GDPR might be applicable.")

    outcome_expcon = expcon(explicit_consent, legal_processing, illegal_processing)
    if outcome_expcon == 0:
        outcome_unablecon = unablecon(unable_consent, vital_interests, legal_processing, illegal_processing)
        if outcome_unablecon == 0:
            outcome_publichealth = publichealth(public_health, legal_basis, safeguard_measures, legal_processing,
                                                illegal_processing)
            if outcome_publichealth == 0:
                outcome_publicinterest = publicinterest(public_interest, legal_basis, proportionate_law,
                                                        essence_of_data_protection, safeguard_measures,
                                                        legal_processing, illegal_processing)
                if outcome_publicinterest == 0:
                    outcome_madepublic = madepublic(made_public, legal_processing, illegal_processing)
                    if outcome_madepublic == 0:
                        outcome_archive = archive(archiving, legal_basis, proportionate_law, essence_of_data_protection,
                                safeguard_measures, legal_processing, illegal_processing)
                        if outcome_archive == 0:
                            outcome_preventive = preventive(preventive_medicine, legal_basis_preventive,
                                                        safeguards_paragraph_three, legal_processing,
                                                        illegal_processing)
                            if outcome_preventive == 0:
                                print(illegal_processing_final)
                            elif outcome_preventive == 1:
                                print(legal_processing)

elif type_of_test.upper() == "ANTIBODY-TEST":
    print("The type of data you are processing is genetic data. Therefore Art. 9 GDPR is applicable and processing"
          "is thus generally prohibited (see Art. 9 (1) GDPR. However an exception according to Art. 9 (2) GDPR might"
          "be applicable.")
    outcome_expcon = expcon(explicit_consent, legal_processing, illegal_processing)
    if outcome_expcon == 0:
        outcome_unablecon = unablecon(unable_consent, vital_interests, legal_processing, illegal_processing)
        if outcome_unablecon == 0:
            outcome_preventive = preventive(preventive_medicine, legal_basis_preventive,
                                            safeguards_paragraph_three, legal_processing,
                                            illegal_processing)
            if outcome_preventive == 0:
                outcome_publichealth = publichealth(public_health, legal_basis, safeguard_measures, legal_processing,
                                                    illegal_processing)
                if outcome_publichealth == 0:
                    outcome_publicinterest = publicinterest(public_interest, legal_basis, proportionate_law,
                                                            essence_of_data_protection, safeguard_measures,
                                                            legal_processing, illegal_processing)
                if outcome_publicinterest == 0:
                    outcome_archive = archive(archiving, legal_basis, proportionate_law, essence_of_data_protection,
                                              safeguard_measures, legal_processing, illegal_processing)
                    if outcome_archive == 0:
                        outcome_madepublic = madepublic(made_public, legal_processing, illegal_processing)
                        if outcome_madepublic == 0:
                            print(illegal_processing_final)
                        elif outcome_madepublic == 1:
                            print(legal_processing)



else:
    print("Invalid input, this program is only designed for PCR- and antibody-tests.")
