import numpy as np

def calc_metric(matrix,metric):
    #print("calc metric")
    #print(metric)
    res = []
    axis = [0,1,None]
    for a in axis:
        if axis is None:
            res.append(metric(matrix))
        else:
            res.append(metric(matrix,axis=a).tolist())
    #print(res)
    return res


def calculate(list):
    
    #assert(len(list) == 9, ValueError("List must contain nine numbers."))
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape((3,3))
    result = {'mean': None,'variance': None,'standard deviation': None,'max': None,'min': None,'sum': None}
    for k in result.keys():
        if k == 'mean':
            result[k] = calc_metric(matrix,np.mean)
        elif k == 'variance':
            result[k] = calc_metric(matrix,np.var)
        elif k == 'standard deviation':
            result[k] = calc_metric(matrix,np.std)
        elif k == 'max':
            result[k] = calc_metric(matrix,np.max)
        elif k == 'min':
            result[k] = calc_metric(matrix,np.min)
        else:
            result[k] = calc_metric(matrix,np.sum)
        #print("in betwennn result.......")
        #print(result[k])

    print("final result.....................")
    print(result)
    return result