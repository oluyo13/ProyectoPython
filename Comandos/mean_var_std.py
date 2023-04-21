import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
 
    lb = np.array(list)
    print(lb)

    
    mean_rows = [lb[[0,1,2]].mean(), lb[[3,4,5]].mean(), lb[[6,7,8]].mean()] 
    mean_columns = [lb[[0,3,6]].mean(), lb[[1,4,7]].mean(), lb[[2,5,8]].mean()] 
    
    var_rows = [lb[[0,1,2]].var(), lb[[3,4,5]].var(), lb[[6,7,8]].var()] 
    var_columns = ([lb[[0,3,6]].var(), lb[[1,4,7]].var(), lb[[2,5,8]].var()])
    
    std_rows = ([lb[[0,1,2]].std(), lb[[3,4,5]].std(), lb[[6,7,8]].std()])
    std_columns = ([lb[[0,3,6]].std(), lb[[1,4,7]].std(), lb[[2,5,8]].std()])
    
    max_rows = ([lb[[0,1,2]].max(), lb[[3,4,5]].max(), lb[[6,7,8]].max()])
    max_columns = ([lb[[0,3,6]].max(), lb[[1,4,7]].max(), lb[[2,5,8]].max()])
    
    min_rows = ([(lb[[0,1,2]]).min(), lb[[3,4,5]].min(), lb[[6,7,8]].min()])
    min_columns = ([(lb[[0,3,6]]).min(), lb[[1,4,7]].min(), lb[[2,5,8]].min()])
    
    sum_rows = ([(lb[[0,1,2]]).sum(), lb[[3,4,5]].sum(), lb[[6,7,8]].sum()])
    sum_columns = ([(lb[[0,3,6]]).sum(), lb[[1,4,7]].sum(), lb[[2,5,8]].sum()])

    return {
    "mean": [mean_columns, mean_rows, lb.mean()],
    "variance": [var_columns, var_rows, lb.var()],
    "standard deviation": [std_columns, std_rows, lb.std()],
    "max" : [max_columns, max_rows, lb.max()],
    "min": [min_columns, min_rows, lb.min()],
    "sum": [sum_columns, sum_rows, lb.sum()]
    }  

calculate([0,1,2,3,4,5,6,7,8])