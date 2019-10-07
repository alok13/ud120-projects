#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import operator  
    
    cleaned_data = []
    errors = [a-b for a,b in zip(predictions, net_worths)]    
    data = zip(ages, net_worths, errors)
    ##data.sort(key=operator.itemgetter(2))
    list_1=sorted(data,key = lambda t: t[2])
    new_data=list(list_1)
    #cleaned_data = list(data[:int(len(predictions)*0.9)])
    cleaned_data = new_data[:int(len(predictions)*0.9)]

    ### your code goes here

    
    return cleaned_data

