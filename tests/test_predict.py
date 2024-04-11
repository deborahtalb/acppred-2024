from acppred.predict import predict_anticancer_peptide

def test_predict_anticancer_peptide_input_variable_type():
    peptide_input = predict_anticancer_peptide('ALBCAQQ')
    assert isinstance(peptide_input, float)
    

    