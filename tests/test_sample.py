# 

def test_pass():
    assert True, "dummy sample test"

def test_get_covid_cases_uk():
    from pycovid import pycovid
    cases = pycovid.getCovidCases(countries=['United Kingdom'])
    assert len(cases)

def test_get_covid_cases_wide_uk():
    from pycovid import pycovid
    cases = pycovid.getCovidCasesWide(countries=['United Kingdom'])
    assert len(cases)
