import pytest
from app.logic import is_eligible_for_loan

def test_eligible_user():
    assert is_eligible_for_loan(60000,23,'employed') == True

def test_underage_user():
    assert is_eligible_for_loan(60000,18,'employed') == False

def test_low_income():
    assert is_eligible_for_loan(30000,23,'employed') == False

def test_unemployed_user():
    assert is_eligible_for_loan(50000,23,'unemployed') == False

def boundary_case():
    assert is_eligible_for_loan(5000,21,'employed') == True