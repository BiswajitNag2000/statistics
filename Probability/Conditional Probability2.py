having_cancer = 1/100 
positive_test_cancer = 90/100
positive_test_no_cancer =10/100
final_ans  =  (positive_test_cancer*having_cancer)/((positive_test_cancer*having_cancer)+(positive_test_no_cancer*(1-having_cancer)))
print("the probability that a woman has cancer if she tests positive:",round(final_ans,2))